from datetime import date, datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo

import pytest

from alarm_clock.timeutil import (
    AlarmError,
    convert,
    format_offset,
    get_zone,
    next_occurrence,
    parse_date,
    parse_hhmm,
    resolve_local,
    search_zones,
    suggest_zones,
)

UTC = timezone.utc
NY = ZoneInfo("America/New_York")
KOLKATA = ZoneInfo("Asia/Kolkata")
LONDON = ZoneInfo("Europe/London")


# ---------------------------------------------------------------- parsing

@pytest.mark.parametrize("text,expected", [("07:05", time(7, 5)), ("7:05", time(7, 5)), ("23:59", time(23, 59)), ("00:00", time(0, 0))])
def test_parse_hhmm_valid(text, expected):
    assert parse_hhmm(text) == expected


@pytest.mark.parametrize("text", ["24:00", "12:60", "7:5", "noon", "", "12-30"])
def test_parse_hhmm_invalid(text):
    with pytest.raises(AlarmError):
        parse_hhmm(text)


def test_parse_date_invalid():
    with pytest.raises(AlarmError, match="YYYY-MM-DD"):
        parse_date("2026-13-01")


# ---------------------------------------------------------------- conversion

def test_convert_kolkata_to_new_york_previous_day():
    result = convert(time(9, 0), KOLKATA, NY, date(2026, 11, 4))
    assert result.target.strftime("%Y-%m-%d %H:%M %Z") == "2026-11-03 22:30 EST"
    assert result.day_shift == -1


def test_convert_new_york_to_kolkata_next_day():
    result = convert(time(20, 0), NY, KOLKATA, date(2026, 7, 1))  # EDT, UTC-4
    assert result.target.strftime("%Y-%m-%d %H:%M") == "2026-07-02 05:30"
    assert result.day_shift == 1


def test_convert_quarter_hour_offset():
    result = convert(time(12, 0), ZoneInfo("UTC"), ZoneInfo("Asia/Kathmandu"), date(2026, 11, 4))
    assert result.target.strftime("%H:%M") == "17:45"
    assert format_offset(result.target) == "UTC+05:45"


def test_format_offset_negative():
    assert format_offset(datetime(2026, 1, 1, tzinfo=ZoneInfo("America/St_Johns"))) == "UTC-03:30"


# ---------------------------------------------------------------- next occurrence

NOW = datetime(2026, 11, 4, 10, 0, tzinfo=UTC)  # a Wednesday


def test_next_occurrence_later_today():
    assert next_occurrence(time(11, 0), UTC, NOW).dt == datetime(2026, 11, 4, 11, 0, tzinfo=UTC)


def test_next_occurrence_already_passed_is_tomorrow():
    assert next_occurrence(time(9, 0), UTC, NOW).dt.date() == date(2026, 11, 5)


def test_next_occurrence_exactly_now_is_tomorrow():
    assert next_occurrence(time(10, 0), UTC, NOW).dt.date() == date(2026, 11, 5)


def test_next_occurrence_uses_zone_local_date():
    # 10:00 UTC is 15:30 in Kolkata; 15:00 Kolkata has passed -> tomorrow there.
    r = next_occurrence(time(15, 0), KOLKATA, NOW)
    assert r.dt.date() == date(2026, 11, 5) and r.utc == datetime(2026, 11, 5, 9, 30, tzinfo=UTC)


def test_weekdays_from_friday_skips_weekend():
    friday_noon = datetime(2026, 11, 6, 12, 0, tzinfo=UTC)
    assert next_occurrence(time(9, 0), UTC, friday_noon, repeat="weekdays").dt.date() == date(2026, 11, 9)


def test_weekdays_from_saturday_skips_to_monday():
    saturday = datetime(2026, 11, 7, 8, 0, tzinfo=UTC)
    assert next_occurrence(time(9, 0), UTC, saturday, repeat="weekdays").dt.date() == date(2026, 11, 9)


def test_explicit_future_date():
    r = next_occurrence(time(7, 0), KOLKATA, NOW, on_date=date(2026, 12, 25))
    assert r.dt == datetime(2026, 12, 25, 7, 0, tzinfo=KOLKATA)


def test_explicit_past_date_errors():
    with pytest.raises(AlarmError, match="in the past"):
        next_occurrence(time(7, 0), UTC, NOW, on_date=date(2026, 11, 1))


# ---------------------------------------------------------------- DST

def test_nonexistent_time_spring_forward_moves_later():
    r = resolve_local(date(2026, 3, 8), time(2, 30), NY)
    assert r.dt.strftime("%H:%M %Z") == "03:30 EDT"
    assert r.utc == datetime(2026, 3, 8, 7, 30, tzinfo=UTC)
    assert "doesn't exist" in r.note and "03:30" in r.note


def test_nonexistent_time_london():
    r = resolve_local(date(2026, 3, 29), time(1, 15), LONDON)
    assert r.dt.strftime("%H:%M %Z") == "02:15 BST"
    assert r.note


def test_ambiguous_time_fall_back_first_and_second():
    first = resolve_local(date(2026, 11, 1), time(1, 30), NY, "first")
    second = resolve_local(date(2026, 11, 1), time(1, 30), NY, "second")
    assert first.utc == datetime(2026, 11, 1, 5, 30, tzinfo=UTC)   # EDT
    assert second.utc == datetime(2026, 11, 1, 6, 30, tzinfo=UTC)  # EST
    assert "happens twice" in first.note and "--ambiguous second" in first.note
    assert first.dt.tzname() == "EDT" and second.dt.tzname() == "EST"


def test_ordinary_time_has_no_note():
    assert resolve_local(date(2026, 3, 8), time(12, 0), NY).note is None
    assert resolve_local(date(2026, 3, 8), time(2, 30), KOLKATA).note is None


def test_next_occurrence_across_spring_forward():
    now = datetime(2026, 3, 7, 12, 0, tzinfo=NY)
    r = next_occurrence(time(2, 30), NY, now, repeat="daily")
    assert r.dt.strftime("%Y-%m-%d %H:%M %Z") == "2026-03-08 03:30 EDT"
    # The day after, 02:30 exists again.
    later = next_occurrence(time(2, 30), NY, r.dt + timedelta(minutes=1), repeat="daily")
    assert later.dt.strftime("%Y-%m-%d %H:%M %Z") == "2026-03-09 02:30 EDT" and later.note is None


def test_daily_alarm_is_24_wall_clock_hours_not_utc_hours_across_dst():
    before = next_occurrence(time(7, 0), NY, datetime(2026, 10, 31, 6, 0, tzinfo=NY))
    after = next_occurrence(time(7, 0), NY, before.dt)
    assert (before.dt.tzname(), after.dt.tzname()) == ("EDT", "EST")
    assert after.utc - before.utc == timedelta(hours=25)


# ---------------------------------------------------------------- zones

def test_search_zones_substring_case_insensitive():
    now = NOW
    assert [z for z, _ in search_zones("kolkata", now)] == ["Asia/Kolkata"]
    assert search_zones("KOLKATA", now) == search_zones("kolkata", now)
    assert search_zones("kolkata", now)[0][1] == "UTC+05:30"


def test_search_zones_prefix_and_spaces():
    results = [z for z, _ in search_zones("america/", NOW)]
    assert results and all(z.lower().startswith("america/") for z in results)
    assert "America/New_York" in [z for z, _ in search_zones("new york", NOW)]


def test_search_zones_no_match():
    assert search_zones("atlantis", NOW) == []


def test_placeholder_zones_hidden():
    assert search_zones("factory", NOW) == []
    assert search_zones("localtime", NOW) == []


def test_get_zone_case_insensitive():
    assert get_zone("asia/kolkata").key == "Asia/Kolkata"


def test_get_zone_unknown_suggests_close_match():
    with pytest.raises(AlarmError) as exc:
        get_zone("Asia/Kolkatta")
    assert "Asia/Kolkata" in str(exc.value)


def test_suggest_by_city_name():
    assert "Asia/Kolkata" in suggest_zones("Kolkatta")
    assert "America/New_York" in suggest_zones("New Yrok")
