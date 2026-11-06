"""Make noise and wait for the user: Enter stops, 's' snoozes."""

from __future__ import annotations

import os
import queue
import shutil
import subprocess
import sys
import threading
import time
from typing import List, Optional, TextIO

STOP, SNOOZE, TIMEOUT, CANCELLED = "stop", "snooze", "timeout", "cancelled"

_MAC_SOUND = "/System/Library/Sounds/Glass.aiff"
_LINUX_SOUNDS = [
    ("paplay", "/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga"),
    ("paplay", "/usr/share/sounds/freedesktop/stereo/complete.oga"),
    ("aplay", "/usr/share/sounds/alsa/Front_Center.wav"),
]


def sound_command() -> Optional[List[str]]:
    """External player command for this platform, or None (Windows / nothing found)."""
    if sys.platform == "darwin" and shutil.which("afplay") and os.path.exists(_MAC_SOUND):
        return ["afplay", _MAC_SOUND]
    if sys.platform.startswith("linux"):
        for player, path in _LINUX_SOUNDS:
            if shutil.which(player) and os.path.exists(path):
                return [player, path]
    return None


def _bell(stream: TextIO) -> None:
    try:
        stream.write("\a")
        stream.flush()
    except (OSError, ValueError):
        pass


def play_once(stream: TextIO) -> None:
    """Play one chime (blocking for roughly its length)."""
    if sys.platform == "win32":
        try:
            import winsound

            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            return
        except Exception:  # noqa: BLE001 - any audio failure falls back to the bell
            pass
    cmd = sound_command()
    if cmd:
        try:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10, check=False)
            return
        except (OSError, subprocess.SubprocessError):
            pass
    _bell(stream)


def sound_loop(stop: threading.Event, stream: TextIO, gap: float = 0.6) -> None:
    """Chime repeatedly until ``stop`` is set."""
    while not stop.is_set():
        play_once(stream)
        stop.wait(gap)


# --------------------------------------------------------------------------- keys

_stdin_lines: "Optional[queue.Queue[str]]" = None
_stdin_lock = threading.Lock()


def _piped_lines() -> "queue.Queue[str]":
    """Lines from a non-TTY stdin, read by one shared background thread."""
    global _stdin_lines
    with _stdin_lock:
        if _stdin_lines is None:
            _stdin_lines = queue.Queue()

            def pump(q: "queue.Queue[str]") -> None:
                for line in sys.stdin:
                    q.put(line)

            threading.Thread(target=pump, args=(_stdin_lines,), daemon=True).start()
        return _stdin_lines


def _classify(ch: str) -> Optional[str]:
    if ch in ("\r", "\n", ""):
        return STOP
    if ch.strip().lower().startswith("s"):
        return SNOOZE
    return None


class KeyReader:
    """Context manager polling for Enter / 's' without blocking forever."""

    def __init__(self) -> None:
        try:
            self.tty = sys.stdin is not None and sys.stdin.isatty()
        except (AttributeError, ValueError):
            self.tty = False
        self._saved = None

    def __enter__(self) -> "KeyReader":
        if not self.tty:
            if sys.stdin is not None:
                _piped_lines()
            return self
        if sys.platform == "win32":
            import msvcrt

            while msvcrt.kbhit():  # discard keys typed during the countdown
                msvcrt.getwch()
        else:
            import termios
            import tty

            fd = sys.stdin.fileno()
            self._saved = termios.tcgetattr(fd)
            tty.setcbreak(fd)
            termios.tcflush(fd, termios.TCIFLUSH)
        return self

    def __exit__(self, *exc: object) -> None:
        if self._saved is not None:
            import termios

            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self._saved)

    def read(self, timeout: float) -> Optional[str]:
        """Return STOP, SNOOZE or None if nothing relevant arrived within ``timeout``."""
        if not self.tty:
            if sys.stdin is None:
                time.sleep(timeout)
                return None
            try:
                line = _piped_lines().get(timeout=timeout)
            except queue.Empty:
                return None
            return _classify(line.strip() or "\n")
        if sys.platform == "win32":
            import msvcrt

            end = time.monotonic() + timeout
            while time.monotonic() < end:
                if msvcrt.kbhit():
                    return _classify(msvcrt.getwch())
                time.sleep(0.03)
            return None
        import select

        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            return _classify(os.read(sys.stdin.fileno(), 1).decode(errors="ignore"))
        return None


# --------------------------------------------------------------------------- ring


def ring(
    label: str,
    snooze_minutes: int,
    ring_seconds: float = 60.0,
    stop_event: Optional[threading.Event] = None,
    stream: Optional[TextIO] = None,
) -> str:
    """Ring until Enter (STOP), 's' (SNOOZE), ``ring_seconds`` elapse (TIMEOUT)
    or ``stop_event`` is set (CANCELLED)."""
    out = stream or sys.stdout
    hint = "press Enter to stop"
    if snooze_minutes > 0:
        snooze_key = "'s'" if KeyReader().tty else "'s' + Enter"
        hint += f", {snooze_key} to snooze {snooze_minutes} min"
    out.write(f"\n*** ALARM *** {label}\n    ({hint}; auto-stops after {int(ring_seconds)}s)\n")
    out.flush()

    stop_sound = threading.Event()
    player = threading.Thread(target=sound_loop, args=(stop_sound, out), daemon=True)
    player.start()
    try:
        deadline = time.monotonic() + ring_seconds
        with KeyReader() as keys:
            while time.monotonic() < deadline:
                if stop_event is not None and stop_event.is_set():
                    return CANCELLED
                key = keys.read(min(0.2, max(0.0, deadline - time.monotonic())))
                if key == STOP:
                    return STOP
                if key == SNOOZE and snooze_minutes > 0:
                    return SNOOZE
        return TIMEOUT
    finally:
        stop_sound.set()
        player.join(timeout=2)
