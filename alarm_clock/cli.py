"""Command-line interface: ``alarm set|zones|now|convert|multi``."""

from __future__ import annotations

import argparse
import sys
import threading
from dataclasses import dataclass, field
from datetime import datetime, time, timedelta, tzinfo
from typing import Callable, List, Optional, Sequence

from . import __version__
from .countdown import Clock, StatusLine, SystemClock, format_remaining, wait_until
from .ringer import SNOOZE, ring
from .timeutil import (
    AMBIGUOUS_CHOICES,
    REPEAT_CHOICES,
    AlarmError,
    Resolved,
    convert,
    describe,
    format_offset,
    get_zone,
    local_zone,
    next_occurrence,
    parse_date,
    parse_hhmm,
    search_zones,
    suggest_zones,
    zone_name,
)

# ringer(label, snooze_minutes, ring_seconds, stop_event) -> "stop" | "snooze" | ...
Ringer = Callable[[str, int, float, Optional[threading.Event]], str]


def _default_ringer(label: str, snooze: int, seconds: float, stop: Optional[threading.Event]) -> str:
    return ring(label, snooze, seconds, stop)


def _zone_or_local(name: Optional[str]) -> tzinfo:
    return get_zone(name) if name else local_zone()


def _out(text: str = "") -> None:
    print(text, flush=True)


# --------------------------------------------------------------------------- parser


def _positive_int(text: str) -> int:
    try:
        value = int(text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{text}' is not a whole number") from None
    if value < 0:
        raise argparse.ArgumentTypeError("must be 0 or more")
    return value


def _ring_seconds(text: str) -> int:
    """At least 1 second, so a firing alarm is never silent."""
    value = _positive_int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("must be at least 1, or the alarm would never be heard")
    return value


def build_parser() -> argparse.ArgumentParser:
    """Build the argparse tree for all subcommands."""
    parser = argparse.ArgumentParser(
        prog="alarm",
        description="A timezone-aware command-line alarm clock.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", metavar="COMMAND")
    sub.required = True

    ring_opts = argparse.ArgumentParser(add_help=False)
    ring_opts.add_argument("--snooze", type=_positive_int, default=5, metavar="N",
                           help="snooze length in minutes (0 disables snooze; default 5)")
    ring_opts.add_argument("--ring-seconds", type=_ring_seconds, default=60, metavar="N",
                           help="stop ringing automatically after N seconds (default 60)")
    ring_opts.add_argument("--ambiguous", choices=AMBIGUOUS_CHOICES, default="first",
                           help="which occurrence to use when a time happens twice (DST fall-back)")

    p = sub.add_parser("set", parents=[ring_opts], help="set an alarm and wait for it")
    p.add_argument("time", metavar="HH:MM", help="24-hour time")
    p.add_argument("--tz", metavar="ZONE", help="IANA timezone (default: system local)")
    p.add_argument("--date", metavar="YYYY-MM-DD", help="specific date (default: next occurrence)")
    p.add_argument("--label", default="Alarm", help="text shown when the alarm rings")
    p.add_argument("--repeat", choices=REPEAT_CHOICES, default="none")
    p.set_defaults(func=cmd_set)

    p = sub.add_parser("zones", help="list/search IANA timezones")
    p.add_argument("search", nargs="?", default="", metavar="SEARCH",
                   help="case-insensitive substring, e.g. 'kolkata' or 'america/'")
    p.set_defaults(func=cmd_zones)

    p = sub.add_parser("now", help="show the current time in one or more zones")
    p.add_argument("--tz", action="append", metavar="ZONE", help="repeatable")
    p.set_defaults(func=cmd_now)

    p = sub.add_parser("convert", help="convert a time between zones")
    p.add_argument("time", metavar="HH:MM")
    p.add_argument("--from", dest="from_zone", required=True, metavar="ZONE")
    p.add_argument("--to", dest="to_zone", required=True, metavar="ZONE")
    p.add_argument("--date", metavar="YYYY-MM-DD", help="date in the --from zone (default: today there)")
    p.add_argument("--ambiguous", choices=AMBIGUOUS_CHOICES, default="first")
    p.set_defaults(func=cmd_convert)

    p = sub.add_parser("multi", parents=[ring_opts], help="run several alarms at once")
    p.add_argument("--at", action="append", required=True, metavar="HH:MM@ZONE",
                   help="repeatable; zone optional (default local)")
    p.add_argument("--label", action="append", default=[], metavar="TEXT",
                   help="repeatable; paired with --at values in order")
    p.set_defaults(func=cmd_multi)
    return parser


# --------------------------------------------------------------------------- shared alarm loop


def _announce(label: str, resolved: Resolved, now: datetime) -> None:
    local = resolved.dt.astimezone(local_zone())
    _out(f"[{label}] rings at {describe(resolved.dt)}")
    if format_offset(local) != format_offset(resolved.dt) or local.tzname() != resolved.dt.tzname():
        _out(f"    = {describe(local)} your local time")
    _out(f"    in {format_remaining(resolved.utc - now)}")
    if resolved.note:
        _out(f"    {resolved.note}")


# --------------------------------------------------------------------------- commands


def cmd_set(args: argparse.Namespace, clock: Clock, ringer: Ringer) -> int:
    """Foreground alarm with live countdown, snooze and repeat."""
    tz = _zone_or_local(args.tz)
    at = parse_hhmm(args.time)
    on_date = parse_date(args.date) if args.date else None
    resolved = next_occurrence(at, tz, clock.now(), on_date, args.repeat, args.ambiguous)
    _announce(args.label, resolved, clock.now())
    _out("Press Ctrl+C to cancel.")

    status = StatusLine(sys.stdout)
    target = resolved.utc
    when = f"{resolved.dt:%H:%M} {resolved.dt.tzname()}"
    while True:
        wait_until(target, clock, lambda left: status.update(
            f"Ringing in {format_remaining(left)}  ({when}, {args.label})", left))
        status.clear()
        result = ringer(args.label, args.snooze, args.ring_seconds, None)
        if result == SNOOZE:
            target = clock.now() + timedelta(minutes=args.snooze)
            when = f"{target.astimezone(tz):%H:%M} {target.astimezone(tz).tzname()} (snoozed)"
            _out(f"Snoozed for {args.snooze} min, until {when}.")
            continue
        _out(f"Alarm stopped ({result}).")
        if args.repeat == "none":
            return 0
        resolved = next_occurrence(at, tz, clock.now(), None, args.repeat, args.ambiguous)
        target = resolved.utc
        when = f"{resolved.dt:%H:%M} {resolved.dt.tzname()}"
        _out(f"Repeats {args.repeat}. Next:")
        _announce(args.label, resolved, clock.now())


def cmd_zones(args: argparse.Namespace, clock: Clock, ringer: Ringer) -> int:
    """List zones matching a substring with their current offsets."""
    matches = search_zones(args.search, clock.now())
    if not matches:
        hints = suggest_zones(args.search)
        msg = f"No timezone contains '{args.search}'."
        if hints:
            msg += " Did you mean: " + ", ".join(hints) + "?"
        raise AlarmError(msg)
    width = max(len(name) for name, _ in matches)
    for name, offset in matches:
        _out(f"{name.ljust(width)}  {offset}")
    _out(f"\n{len(matches)} zone{'s' if len(matches) != 1 else ''}")
    return 0


def cmd_now(args: argparse.Namespace, clock: Clock, ringer: Ringer) -> int:
    """Print the current time in each requested zone."""
    zones = [get_zone(z) for z in args.tz] if args.tz else [local_zone()]
    now = clock.now()
    width = max(len(zone_name(z)) for z in zones)
    for tz in zones:
        here = now.astimezone(tz)
        _out(f"{zone_name(tz).ljust(width)}  {here:%a %Y-%m-%d %H:%M:%S} {here.tzname():<5} {format_offset(here)}")
    return 0


def cmd_convert(args: argparse.Namespace, clock: Clock, ringer: Ringer) -> int:
    """Convert a wall-clock time from one zone to another."""
    src, dst = get_zone(args.from_zone), get_zone(args.to_zone)
    at = parse_hhmm(args.time)
    on_date = parse_date(args.date) if args.date else clock.now().astimezone(src).date()
    result = convert(at, src, dst, on_date, args.ambiguous)
    shift = ""
    if result.day_shift:
        shift = f"  ({'+' if result.day_shift > 0 else ''}{result.day_shift} day{'s' if abs(result.day_shift) != 1 else ''})"
    _out(f"{describe(result.source)}  {zone_name(src)}")
    _out(f"{describe(result.target)}  {zone_name(dst)}{shift}")
    if result.note:
        _out(result.note)
    return 0


@dataclass
class _MultiAlarm:
    label: str
    tz: tzinfo
    resolved: Resolved
    target: datetime = field(init=False)
    done: bool = False

    def __post_init__(self) -> None:
        self.target = self.resolved.utc


def parse_at(spec: str) -> "tuple[time, Optional[str]]":
    """Split ``HH:MM@Zone`` (zone optional) into a time and zone name."""
    clock_part, sep, zone_part = spec.partition("@")
    return parse_hhmm(clock_part), (zone_part.strip() or None) if sep else None


def cmd_multi(args: argparse.Namespace, clock: Clock, ringer: Ringer) -> int:
    """Run several alarms concurrently, one thread each."""
    if len(args.label) > len(args.at):
        raise AlarmError(f"Got {len(args.label)} --label values but only {len(args.at)} --at values.")
    alarms: List[_MultiAlarm] = []
    now = clock.now()
    for i, spec in enumerate(args.at):
        at, zone = parse_at(spec)
        tz = _zone_or_local(zone)
        label = args.label[i] if i < len(args.label) else spec
        alarms.append(_MultiAlarm(label, tz, next_occurrence(at, tz, now, None, "none", args.ambiguous)))
    for alarm in alarms:
        _announce(alarm.label, alarm.resolved, now)
    _out(f"Running {len(alarms)} alarms. Press Ctrl+C to cancel all.")

    stop = threading.Event()
    console = threading.Lock()  # one alarm rings (and owns the keyboard) at a time
    status = StatusLine(sys.stdout)

    def worker(alarm: _MultiAlarm) -> None:
        while wait_until(alarm.target, clock, stop_event=stop):
            with console:
                if stop.is_set():
                    return
                status.clear()
                result = ringer(alarm.label, args.snooze, args.ring_seconds, stop)
                if result == SNOOZE:
                    alarm.target = clock.now() + timedelta(minutes=args.snooze)
                    _out(f"[{alarm.label}] snoozed {args.snooze} min.")
                    continue
                _out(f"[{alarm.label}] stopped ({result}).")
            break
        alarm.done = True

    threads = [threading.Thread(target=worker, args=(a,), daemon=True, name=a.label) for a in alarms]
    for t in threads:
        t.start()
    try:
        while True:
            alive = [t for t in threads if t.is_alive()]
            if not alive:
                break
            if console.acquire(blocking=False):
                try:
                    pending = [a for a in alarms if not a.done]
                    if pending:
                        current = clock.now()
                        soonest = min(a.target - current for a in pending)
                        status.update(" | ".join(
                            f"{a.label}: {format_remaining(a.target - current)}" for a in pending), soonest)
                finally:
                    console.release()
            alive[0].join(timeout=0.5)
    except KeyboardInterrupt:
        stop.set()
        for t in threads:
            t.join(timeout=3)
        raise
    status.clear()
    _out("All alarms finished.")
    return 0


# --------------------------------------------------------------------------- entry point


def main(
    argv: Optional[Sequence[str]] = None,
    clock: Optional[Clock] = None,
    ringer: Optional[Ringer] = None,
) -> int:
    """Run the CLI. ``clock`` and ``ringer`` are injectable for tests."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")  # type: ignore[union-attr]
        except (AttributeError, ValueError):
            pass
    args = build_parser().parse_args(argv)
    try:
        return int(args.func(args, clock or SystemClock(), ringer or _default_ringer))
    except AlarmError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\nAlarm cancelled.", flush=True)
        return 130


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
