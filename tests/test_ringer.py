"""Ringer tests: sound and keyboard are faked, so nothing plays and nothing waits."""

import io
import threading

import pytest

from alarm_clock import ringer
from alarm_clock.ringer import CANCELLED, SNOOZE, STOP, TIMEOUT, _classify, ring


class FakeKeys:
    """Stands in for KeyReader; ``read`` replays scripted keys, then None."""

    script: list = []

    def __init__(self) -> None:
        self.tty = True

    def __enter__(self) -> "FakeKeys":
        return self

    def __exit__(self, *exc: object) -> None:
        pass

    def read(self, timeout: float):
        return FakeKeys.script.pop(0) if FakeKeys.script else None


@pytest.fixture(autouse=True)
def silent(monkeypatch):
    monkeypatch.setattr(ringer, "play_once", lambda stream: None)
    monkeypatch.setattr(ringer, "KeyReader", FakeKeys)
    FakeKeys.script = []


@pytest.mark.parametrize("key,expected", [
    ("\r", STOP), ("\n", STOP), ("s", SNOOZE), ("S", SNOOZE), ("snooze", SNOOZE), ("x", None),
])
def test_classify(key, expected):
    assert _classify(key) == expected


def test_enter_stops():
    FakeKeys.script = [None, STOP]
    out = io.StringIO()
    assert ring("Tea", 5, 30, stream=out) == STOP
    assert "*** ALARM *** Tea" in out.getvalue() and "snooze 5 min" in out.getvalue()


def test_s_snoozes():
    FakeKeys.script = [SNOOZE]
    assert ring("Tea", 5, 30, stream=io.StringIO()) == SNOOZE


def test_snooze_ignored_when_disabled():
    FakeKeys.script = [SNOOZE, STOP]
    out = io.StringIO()
    assert ring("Tea", 0, 30, stream=out) == STOP
    assert "snooze" not in out.getvalue()


def test_auto_stop_after_ring_seconds():
    assert ring("Tea", 5, 0, stream=io.StringIO()) == TIMEOUT


def test_stop_event_cancels():
    stop = threading.Event()
    stop.set()
    assert ring("Tea", 5, 30, stop_event=stop, stream=io.StringIO()) == CANCELLED
