from datetime import timedelta

import pytest

from alarm_clock.cli import main, parse_at
from alarm_clock.timeutil import AlarmError


class FakeRinger:
    """Records rings and replays scripted responses ("stop" / "snooze")."""

    def __init__(self, clock, responses=("stop",)):
        self.clock = clock
        self.responses = list(responses)
        self.calls = []

    def __call__(self, label, snooze, seconds, stop_event):
        self.calls.append((label, self.clock.now()))
        return self.responses.pop(0) if self.responses else "stop"


def test_zones_kolkata(capsys, fake_clock):
    assert main(["zones", "kolkata"], clock=fake_clock) == 0
    out = capsys.readouterr().out
    assert "Asia/Kolkata" in out and "UTC+05:30" in out and "1 zone" in out


def test_zones_no_match_suggests(capsys, fake_clock):
    assert main(["zones", "kolkatta"], clock=fake_clock) == 2
    assert "Asia/Kolkata" in capsys.readouterr().err


def test_now_multiple_zones(capsys, fake_clock):
    assert main(["now", "--tz", "Asia/Kolkata", "--tz", "America/New_York"], clock=fake_clock) == 0
    out = capsys.readouterr().out
    assert "2026-11-04 15:30:00 IST" in out
    assert "2026-11-04 05:00:00 EST" in out


def test_convert(capsys, fake_clock):
    code = main(["convert", "09:00", "--from", "Asia/Kolkata", "--to", "America/New_York",
                 "--date", "2026-11-04"], clock=fake_clock)
    assert code == 0
    out = capsys.readouterr().out
    assert "22:30 EST" in out and "(-1 day)" in out


def test_unknown_zone_friendly_error(capsys, fake_clock):
    assert main(["now", "--tz", "Asia/Kolkatta"], clock=fake_clock) == 2
    err = capsys.readouterr().err
    assert err.startswith("error: Unknown timezone") and "Did you mean" in err


def test_invalid_time_friendly_error(capsys, fake_clock):
    assert main(["set", "25:00", "--tz", "UTC"], clock=fake_clock) == 2
    assert "out of range" in capsys.readouterr().err


def test_past_date_error(capsys, fake_clock):
    assert main(["set", "07:00", "--tz", "UTC", "--date", "2026-01-01"], clock=fake_clock) == 2
    assert "in the past" in capsys.readouterr().err


def test_set_rings_at_target(capsys, fake_clock):
    ringer = FakeRinger(fake_clock)
    start = fake_clock.now()
    assert main(["set", "10:01", "--tz", "UTC", "--label", "Tea"], clock=fake_clock, ringer=ringer) == 0
    assert [label for label, _ in ringer.calls] == ["Tea"]
    assert ringer.calls[0][1] == start + timedelta(minutes=1)


def test_set_snooze_then_stop(capsys, fake_clock):
    ringer = FakeRinger(fake_clock, ["snooze", "stop"])
    main(["set", "10:01", "--tz", "UTC", "--snooze", "3"], clock=fake_clock, ringer=ringer)
    first, second = ringer.calls[0][1], ringer.calls[1][1]
    assert second - first == timedelta(minutes=3)
    assert "Snoozed for 3 min" in capsys.readouterr().out


def test_set_dst_note_shown(capsys, fake_clock):
    fake_clock._now = fake_clock._now.replace(year=2026, month=3, day=7)
    main(["set", "02:30", "--tz", "America/New_York", "--date", "2026-03-08"],
         clock=fake_clock, ringer=FakeRinger(fake_clock))
    assert "doesn't exist" in capsys.readouterr().out


def test_multi_runs_all(capsys, fake_clock):
    ringer = FakeRinger(fake_clock)
    code = main(["multi", "--at", "10:02@UTC", "--at", "15:31@Asia/Kolkata",
                 "--label", "Two", "--label", "Kolkata"], clock=fake_clock, ringer=ringer)
    assert code == 0
    assert sorted(label for label, _ in ringer.calls) == ["Kolkata", "Two"]
    assert "All alarms finished" in capsys.readouterr().out


def test_parse_at():
    t, zone = parse_at("07:30@Europe/Paris")
    assert (t.hour, t.minute, zone) == (7, 30, "Europe/Paris")
    assert parse_at("07:30")[1] is None
    with pytest.raises(AlarmError):
        parse_at("7h30@UTC")
