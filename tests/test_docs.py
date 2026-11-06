"""Every `alarm ...` example in COMMANDS.md and README.md must behave as documented.

Lines ending in `# exits 2` must fail with exit code 2; every other line must succeed
(exit 0, or 130 when a --repeat alarm is stopped by the simulated Ctrl+C below).
"""

import re
import shlex
import threading
from pathlib import Path

import pytest

from alarm_clock import cli

ROOT = Path(__file__).resolve().parent.parent


def _examples():
    for doc in ("COMMANDS.md", "README.md"):
        text = (ROOT / doc).read_text(encoding="utf-8")
        for block in re.findall(r"```bash\n(.*?)```", text, re.S):
            for line in block.splitlines():
                line = line.strip()
                if line.startswith("alarm "):
                    argv = shlex.split(line, comments=True)[1:]
                elif line.startswith("python -m alarm_clock"):
                    argv = shlex.split(line, comments=True)[3:]
                else:
                    continue
                yield pytest.param(argv, "# exits 2" in line, id=f"{doc}: {line.split('  #')[0].strip()}")


@pytest.mark.parametrize("argv,want_error", list(_examples()))
def test_documented_example(argv, want_error, fake_clock, monkeypatch, capsys):
    def instant_wait(target, clock, on_tick=None, stop_event=None, tick=1.0):
        with clock._lock:
            clock._now = max(clock._now, target)
        return True

    monkeypatch.setattr(cli, "wait_until", instant_wait)
    rings = []

    def ringer(label, snooze, seconds, stop):
        rings.append(label)
        if threading.current_thread() is threading.main_thread() and len(rings) >= 3:
            raise KeyboardInterrupt  # end endless --repeat loops the way Ctrl+C would
        return "stop"

    try:
        code = cli.main(argv, clock=fake_clock, ringer=ringer)
    except SystemExit as exc:  # argparse: --help/--version exit 0, usage errors exit 2
        code = exc.code if isinstance(exc.code, int) else 0
    out, err = capsys.readouterr()

    assert "Traceback" not in out + err
    if want_error:
        assert code == 2, out + err
        assert "error" in err.lower()
    else:
        assert code in (0, 130), out + err
