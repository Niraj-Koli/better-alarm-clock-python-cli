"""Injectable clock, waiting loop and a terminal status-line renderer."""

from __future__ import annotations

import math
import threading
import time as _time
from datetime import datetime, timedelta, timezone
from typing import Callable, Optional, Protocol, TextIO


class Clock(Protocol):
    """Source of time. Tests substitute a fake that never really sleeps."""

    def now(self) -> datetime:
        """Current instant as an aware UTC datetime."""
        ...

    def sleep(self, seconds: float) -> None:
        """Block for ``seconds``."""
        ...


class SystemClock:
    """The real wall clock."""

    def now(self) -> datetime:
        return datetime.now(timezone.utc)

    def sleep(self, seconds: float) -> None:
        _time.sleep(max(0.0, seconds))


def format_remaining(delta: timedelta) -> str:
    """``HH:MM:SS`` (with a ``Nd`` prefix past 24h), rounded up to the second."""
    total = max(0, math.ceil(delta.total_seconds()))
    days, rem = divmod(total, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    clock = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{days}d {clock}" if days else clock


def wait_until(
    target: datetime,
    clock: Clock,
    on_tick: Optional[Callable[[timedelta], None]] = None,
    stop_event: Optional[threading.Event] = None,
    tick: float = 1.0,
) -> bool:
    """Wait until ``clock.now() >= target``, calling ``on_tick(remaining)`` each tick.

    Re-reads the clock every tick, so system sleep / clock changes are handled.
    Returns True when the target is reached, False if ``stop_event`` was set.
    """
    while True:
        if stop_event is not None and stop_event.is_set():
            return False
        remaining = target - clock.now()
        seconds = remaining.total_seconds()
        if seconds <= 0:
            return True
        if on_tick is not None:
            on_tick(remaining)
        # Sleep to the next whole-second boundary so the display ticks evenly.
        frac = seconds - math.floor(seconds)
        clock.sleep(min(tick, seconds, frac if frac > 0.05 else tick))


class StatusLine:
    """A single self-overwriting status line on a TTY; sparse plain lines otherwise."""

    def __init__(self, stream: TextIO, plain_every: int = 15) -> None:
        self.stream = stream
        try:
            self.tty = bool(stream.isatty())
        except (AttributeError, ValueError):
            self.tty = False
        self.plain_every = plain_every
        self._width = 0
        self._bucket: Optional[int] = None

    def update(self, text: str, remaining: timedelta) -> None:
        if self.tty:
            self._width = max(self._width, len(text))
            self.stream.write("\r" + text.ljust(self._width))
            self.stream.flush()
            return
        bucket = int(math.ceil(remaining.total_seconds()) // self.plain_every)
        if bucket != self._bucket:
            self._bucket = bucket
            self.stream.write(text + "\n")
            self.stream.flush()

    def clear(self) -> None:
        if self.tty and self._width:
            self.stream.write("\r" + " " * self._width + "\r")
            self.stream.flush()
        self._width = 0
        self._bucket = None
