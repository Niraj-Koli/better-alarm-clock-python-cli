"""Shared fixtures: a fake clock that advances instantly instead of sleeping."""

from __future__ import annotations

import threading
from datetime import datetime, timedelta, timezone

import pytest


class FakeClock:
    """Thread-safe clock whose ``sleep`` just moves time forward."""

    def __init__(self, start: datetime) -> None:
        self._now = start.astimezone(timezone.utc)
        self._lock = threading.Lock()
        self.slept = 0.0

    def now(self) -> datetime:
        with self._lock:
            return self._now

    def sleep(self, seconds: float) -> None:
        with self._lock:
            self._now += timedelta(seconds=seconds)
            self.slept += seconds


@pytest.fixture
def fake_clock() -> FakeClock:
    return FakeClock(datetime(2026, 11, 4, 10, 0, tzinfo=timezone.utc))
