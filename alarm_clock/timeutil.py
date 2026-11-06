"""Pure time/timezone logic: parsing, zone lookup, DST resolution, next-occurrence.

Nothing in this module sleeps, prints, or reads the system clock implicitly;
callers pass ``now`` explicitly so everything is deterministic and testable.
"""

from __future__ import annotations

import difflib
import math
import os
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone, tzinfo
from functools import lru_cache
from typing import List, Optional, Tuple
from zoneinfo import ZoneInfo, available_timezones

UTC = timezone.utc
REPEAT_CHOICES = ("none", "daily", "weekdays")
AMBIGUOUS_CHOICES = ("first", "second")


class AlarmError(Exception):
    """A user-facing error with a friendly message (no traceback shown)."""


@dataclass(frozen=True)
class Resolved:
    """A wall-clock time pinned to a real instant, plus an optional DST note.

    ``dt`` is aware and expressed in the alarm's zone; ``note`` explains any
    DST adjustment in plain language (``None`` when nothing unusual happened).
    """

    dt: datetime
    note: Optional[str] = None

    @property
    def utc(self) -> datetime:
        """The same instant in UTC (safe for comparisons across zones)."""
        return self.dt.astimezone(UTC)


@dataclass(frozen=True)
class Conversion:
    """Result of converting a wall-clock time from one zone to another."""

    source: datetime
    target: datetime
    day_shift: int
    note: Optional[str] = None


# --------------------------------------------------------------------------- parsing

_HHMM = re.compile(r"^\s*(\d{1,2}):(\d{2})\s*$")


def parse_hhmm(text: str) -> time:
    """Parse a 24-hour ``HH:MM`` string into a :class:`datetime.time`."""
    match = _HHMM.match(text or "")
    if not match:
        raise AlarmError(
            f"'{text}' is not a valid time. Use 24-hour HH:MM, e.g. 07:30 or 18:05."
        )
    hour, minute = int(match.group(1)), int(match.group(2))
    if hour > 23 or minute > 59:
        raise AlarmError(
            f"'{text}' is out of range. Hours go 00-23 and minutes 00-59."
        )
    return time(hour, minute)


def parse_date(text: str) -> date:
    """Parse a ``YYYY-MM-DD`` string."""
    try:
        return date.fromisoformat(text.strip())
    except (ValueError, AttributeError):
        raise AlarmError(
            f"'{text}' is not a valid date. Use YYYY-MM-DD, e.g. 2026-12-31."
        ) from None


# --------------------------------------------------------------------------- zones


_NOT_REAL_ZONES = frozenset({"localtime", "Factory"})


@lru_cache(maxsize=1)
def all_zones() -> Tuple[str, ...]:
    """All IANA zone names known to zoneinfo, sorted (minus non-location placeholders)."""
    return tuple(sorted(z for z in available_timezones() if z not in _NOT_REAL_ZONES))


@lru_cache(maxsize=1)
def _lower_index() -> dict:
    return {z.lower(): z for z in all_zones()}


def suggest_zones(name: str, limit: int = 3) -> List[str]:
    """Return up to ``limit`` zone names that look like ``name``.

    Matches against full names (``Asia/Kolkatta``) and against the city part
    alone (``kolkata``, ``new york``).
    """
    query = (name or "").strip().lower().replace(" ", "_")
    if not query:
        return []
    index = _lower_index()
    found: List[str] = []

    def add(names: List[str]) -> None:
        for n in names:
            if n not in found:
                found.append(n)

    add([index[m] for m in difflib.get_close_matches(query, list(index), n=limit, cutoff=0.6)])

    cities: dict = {}
    for full in all_zones():
        cities.setdefault(full.rsplit("/", 1)[-1].lower(), []).append(full)
    for city in difflib.get_close_matches(query.rsplit("/", 1)[-1], list(cities), n=limit, cutoff=0.75):
        add(cities[city])

    if len(found) < limit:
        add([z for z in all_zones() if query in z.lower()])
    return found[:limit]


def get_zone(name: str) -> ZoneInfo:
    """Look up an IANA zone (case-insensitive), with suggestions on failure."""
    key = (name or "").strip()
    canonical = _lower_index().get(key.lower())
    if canonical:
        return ZoneInfo(canonical)
    hints = suggest_zones(key)
    msg = f"Unknown timezone '{name}'."
    if hints:
        msg += " Did you mean: " + ", ".join(hints) + "?"
    msg += " Run 'alarm zones <search>' to browse zones."
    raise AlarmError(msg)


# Windows registry zone key -> IANA (common zones; CLDR windowsZones, territory 001).
WINDOWS_TO_IANA = {
    "UTC": "UTC",
    "Coordinated Universal Time": "UTC",
    "India Standard Time": "Asia/Kolkata",
    "Nepal Standard Time": "Asia/Kathmandu",
    "Sri Lanka Standard Time": "Asia/Colombo",
    "Bangladesh Standard Time": "Asia/Dhaka",
    "Pakistan Standard Time": "Asia/Karachi",
    "Afghanistan Standard Time": "Asia/Kabul",
    "West Asia Standard Time": "Asia/Tashkent",
    "Central Asia Standard Time": "Asia/Almaty",
    "Myanmar Standard Time": "Asia/Yangon",
    "SE Asia Standard Time": "Asia/Bangkok",
    "China Standard Time": "Asia/Shanghai",
    "Singapore Standard Time": "Asia/Singapore",
    "Taipei Standard Time": "Asia/Taipei",
    "Tokyo Standard Time": "Asia/Tokyo",
    "Korea Standard Time": "Asia/Seoul",
    "Arabian Standard Time": "Asia/Dubai",
    "Arab Standard Time": "Asia/Riyadh",
    "Iran Standard Time": "Asia/Tehran",
    "Israel Standard Time": "Asia/Jerusalem",
    "Turkey Standard Time": "Europe/Istanbul",
    "Russian Standard Time": "Europe/Moscow",
    "GMT Standard Time": "Europe/London",
    "Greenwich Standard Time": "Atlantic/Reykjavik",
    "W. Europe Standard Time": "Europe/Berlin",
    "Romance Standard Time": "Europe/Paris",
    "Central Europe Standard Time": "Europe/Budapest",
    "Central European Standard Time": "Europe/Warsaw",
    "E. Europe Standard Time": "Europe/Chisinau",
    "FLE Standard Time": "Europe/Kiev",
    "GTB Standard Time": "Europe/Bucharest",
    "Egypt Standard Time": "Africa/Cairo",
    "South Africa Standard Time": "Africa/Johannesburg",
    "W. Central Africa Standard Time": "Africa/Lagos",
    "E. Africa Standard Time": "Africa/Nairobi",
    "AUS Eastern Standard Time": "Australia/Sydney",
    "E. Australia Standard Time": "Australia/Brisbane",
    "Cen. Australia Standard Time": "Australia/Adelaide",
    "AUS Central Standard Time": "Australia/Darwin",
    "W. Australia Standard Time": "Australia/Perth",
    "New Zealand Standard Time": "Pacific/Auckland",
    "Hawaiian Standard Time": "Pacific/Honolulu",
    "Alaskan Standard Time": "America/Anchorage",
    "Pacific Standard Time": "America/Los_Angeles",
    "Mountain Standard Time": "America/Denver",
    "US Mountain Standard Time": "America/Phoenix",
    "Central Standard Time": "America/Chicago",
    "Central Standard Time (Mexico)": "America/Mexico_City",
    "Eastern Standard Time": "America/New_York",
    "Atlantic Standard Time": "America/Halifax",
    "Newfoundland Standard Time": "America/St_Johns",
    "SA Pacific Standard Time": "America/Bogota",
    "Venezuela Standard Time": "America/Caracas",
    "Pacific SA Standard Time": "America/Santiago",
    "E. South America Standard Time": "America/Sao_Paulo",
    "Argentina Standard Time": "America/Buenos_Aires",
}


def _windows_zone_key() -> Optional[str]:
    try:
        import winreg  # type: ignore[import-not-found]

        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Control\TimeZoneInformation",
        ) as key:
            value, _ = winreg.QueryValueEx(key, "TimeZoneKeyName")
            return str(value).rstrip("\x00").strip()
    except OSError:
        return None


def local_zone() -> tzinfo:
    """Best-effort system local timezone as a DST-aware ZoneInfo.

    Order: ``$TZ``, the OS setting (``/etc/localtime`` or the Windows registry),
    then a fixed UTC offset as a last resort.
    """
    env = os.environ.get("TZ", "").lstrip(":").strip()
    if env and env.lower() in _lower_index():
        return ZoneInfo(_lower_index()[env.lower()])

    if sys.platform == "win32":
        iana = WINDOWS_TO_IANA.get(_windows_zone_key() or "")
        if iana:
            return ZoneInfo(iana)
    else:
        link = os.path.realpath("/etc/localtime")
        if "zoneinfo/" in link:
            candidate = link.split("zoneinfo/", 1)[1]
            if candidate.lower() in _lower_index():
                return ZoneInfo(_lower_index()[candidate.lower()])
        try:
            with open("/etc/timezone", encoding="utf-8") as fh:
                candidate = fh.read().strip()
            if candidate.lower() in _lower_index():
                return ZoneInfo(_lower_index()[candidate.lower()])
        except OSError:
            pass

    fallback = datetime.now().astimezone().tzinfo
    return fallback if fallback is not None else UTC


def zone_name(tz: tzinfo) -> str:
    """Human-readable zone identifier (IANA key when available)."""
    return getattr(tz, "key", None) or str(tz)


# --------------------------------------------------------------------------- formatting


def format_offset(dt: datetime) -> str:
    """Format a datetime's UTC offset as ``UTC+05:30``."""
    offset = dt.utcoffset() or timedelta(0)
    minutes = int(offset.total_seconds() // 60)
    sign = "+" if minutes >= 0 else "-"
    hours, mins = divmod(abs(minutes), 60)
    return f"UTC{sign}{hours:02d}:{mins:02d}"


def describe(dt: datetime) -> str:
    """e.g. ``Wed 2026-11-04 07:00 IST (UTC+05:30)``."""
    return f"{dt:%a %Y-%m-%d %H:%M} {dt.tzname()} ({format_offset(dt)})"


def humanize(delta: timedelta) -> str:
    """Rough human duration like ``2 days 3 h`` or ``5 min``."""
    total = abs(int(delta.total_seconds()))
    days, rem = divmod(total, 86400)
    hours, rem = divmod(rem, 3600)
    minutes = math.ceil(rem / 60) if not (days or hours) else rem // 60
    parts = []
    if days:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours:
        parts.append(f"{hours} h")
    if minutes and not days:
        parts.append(f"{minutes} min")
    return " ".join(parts) or "less than a minute"


# --------------------------------------------------------------------------- DST


def _same_wall(dt: datetime, naive: datetime, tz: tzinfo) -> bool:
    return dt.astimezone(UTC).astimezone(tz).replace(tzinfo=None, fold=0) == naive


def resolve_local(day: date, at: time, tz: tzinfo, prefer: str = "first") -> Resolved:
    """Attach ``tz`` to a wall-clock date+time, handling DST transitions.

    * Nonexistent time (clocks spring forward over it): shift forward by the
      size of the gap, e.g. 02:30 -> 03:30.
    * Ambiguous time (clocks fall back, so it happens twice): use the first
      occurrence unless ``prefer == "second"``.
    """
    if prefer not in AMBIGUOUS_CHOICES:
        raise AlarmError(f"--ambiguous must be one of {', '.join(AMBIGUOUS_CHOICES)}.")
    naive = datetime.combine(day, at)
    first = naive.replace(tzinfo=tz, fold=0)
    second = naive.replace(tzinfo=tz, fold=1)
    if first.utcoffset() == second.utcoffset():
        return Resolved(first)

    where = zone_name(tz)
    hhmm = at.strftime("%H:%M")

    if not _same_wall(first, naive, tz):
        # In a gap: fold=0 uses the pre-transition offset, which lands *after*
        # the gap once normalised -- exactly "shift forward by the gap".
        moved = first.astimezone(UTC).astimezone(tz)
        gap = abs((second.utcoffset() or timedelta(0)) - (first.utcoffset() or timedelta(0)))
        note = (
            f"Heads up: {hhmm} doesn't exist on {day.isoformat()} in {where} - clocks "
            f"spring forward {humanize(gap)} for daylight saving, skipping it. "
            f"The alarm will ring at {moved:%H:%M} {moved.tzname()} instead."
        )
        return Resolved(moved, note)

    chosen = first if prefer == "first" else second
    other = second if prefer == "first" else first
    note = (
        f"Heads up: {hhmm} happens twice on {day.isoformat()} in {where} because clocks "
        f"fall back for the end of daylight saving. Using the {prefer} one "
        f"({hhmm} {chosen.tzname()}, {format_offset(chosen)}); the other is "
        f"{hhmm} {other.tzname()} ({format_offset(other)}). "
        f"Use --ambiguous {'second' if prefer == 'first' else 'first'} to switch."
    )
    return Resolved(chosen, note)


# --------------------------------------------------------------------------- scheduling


def next_occurrence(
    at: time,
    tz: tzinfo,
    now: datetime,
    on_date: Optional[date] = None,
    repeat: str = "none",
    prefer: str = "first",
) -> Resolved:
    """Find the next instant (strictly after ``now``) when ``at`` occurs in ``tz``.

    With ``on_date`` the alarm is pinned to that day and must be in the future.
    ``repeat == "weekdays"`` skips Saturdays and Sundays.
    """
    if repeat not in REPEAT_CHOICES:
        raise AlarmError(f"--repeat must be one of {', '.join(REPEAT_CHOICES)}.")
    now_utc = now.astimezone(UTC)

    if on_date is not None:
        resolved = resolve_local(on_date, at, tz, prefer)
        if resolved.utc <= now_utc:
            raise AlarmError(
                f"{on_date.isoformat()} {at:%H:%M} in {zone_name(tz)} is in the past "
                f"({humanize(now_utc - resolved.utc)} ago). Pick a future date, or drop "
                f"--date to use the next occurrence."
            )
        return resolved

    day = now_utc.astimezone(tz).date()
    for _ in range(10):
        if not (repeat == "weekdays" and day.weekday() >= 5):
            resolved = resolve_local(day, at, tz, prefer)
            if resolved.utc > now_utc:
                return resolved
        day += timedelta(days=1)
    raise AlarmError("Could not find a next occurrence for that time.")  # pragma: no cover


def convert(at: time, src: tzinfo, dst: tzinfo, on_date: date, prefer: str = "first") -> Conversion:
    """Convert wall-clock ``at`` on ``on_date`` in ``src`` to the ``dst`` zone."""
    resolved = resolve_local(on_date, at, src, prefer)
    target = resolved.dt.astimezone(dst)
    return Conversion(
        source=resolved.dt,
        target=target,
        day_shift=(target.date() - resolved.dt.date()).days,
        note=resolved.note,
    )


def search_zones(query: str, now: datetime) -> List[Tuple[str, str]]:
    """Zones whose name contains ``query`` (case-insensitive; spaces match ``_``),
    each paired with its current UTC offset."""
    needle = (query or "").strip().lower()
    alt = needle.replace(" ", "_")
    results = []
    for name in all_zones():
        low = name.lower()
        if needle in low or alt in low:
            results.append((name, format_offset(now.astimezone(ZoneInfo(name)))))
    return results
