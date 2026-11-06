import io
import threading
from datetime import timedelta

from alarm_clock.countdown import StatusLine, format_remaining, wait_until


def test_wait_until_reaches_target_without_real_sleep(fake_clock):
    target = fake_clock.now() + timedelta(seconds=90.5)
    ticks = []
    assert wait_until(target, fake_clock, ticks.append) is True
    assert fake_clock.now() >= target
    assert 85 <= len(ticks) <= 95
    assert ticks[0] > ticks[-1]


def test_wait_until_past_target_returns_immediately(fake_clock):
    assert wait_until(fake_clock.now() - timedelta(seconds=1), fake_clock) is True
    assert fake_clock.slept == 0


def test_wait_until_stop_event_cancels(fake_clock):
    stop = threading.Event()
    target = fake_clock.now() + timedelta(hours=1)

    def tick(_left):
        if fake_clock.slept >= 5:
            stop.set()

    assert wait_until(target, fake_clock, tick, stop) is False
    assert fake_clock.now() < target


def test_format_remaining():
    assert format_remaining(timedelta(seconds=59.2)) == "00:01:00"
    assert format_remaining(timedelta(hours=26, minutes=3, seconds=4)) == "1d 02:03:04"
    assert format_remaining(timedelta(seconds=-5)) == "00:00:00"


def test_status_line_non_tty_prints_sparse_lines():
    buf = io.StringIO()
    line = StatusLine(buf, plain_every=15)
    for s in range(60, 0, -1):
        line.update(f"left {s}", timedelta(seconds=s))
    assert 3 <= buf.getvalue().count("\n") <= 5
