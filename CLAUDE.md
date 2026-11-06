# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

A Python command-line alarm clock with full IANA timezone support. CLI only.

## Hard constraints (from the original spec)

- Runtime dependencies are the stdlib plus `tzdata` only. Ask before adding anything else.
- No database, server, network calls or config files. All state is in memory for the life of the process. Never write alarms to disk.
- All IANA zones come from `zoneinfo.available_timezones()`. Never hardcode a zone list. `ZONES.md` is a human reference only, and code must never read it.
- Python 3.9+ must keep working. That rules out `match`, `X | Y` in runtime annotations, and parenthesised context managers. Keep `from __future__ import annotations` at the top of modules.

## Commands

The venv is at `.venv` (check its version with `.\.venv\Scripts\python.exe --version`). Call its executables directly instead of activating it:

- Install/refresh: `.\.venv\Scripts\python.exe -m pip install -e ".[dev]"`
- All tests: `.\.venv\Scripts\python.exe -m pytest -q`
- One test: `.\.venv\Scripts\python.exe -m pytest tests/test_timeutil.py::test_ambiguous_time_fall_back_first_and_second -q`
- Python 3.9 check (uv is installed; this downloads a throwaway 3.9 and doesn't touch `.venv`): `uv run --no-project --python 3.9 --with pytest --with tzdata python -m pytest -q -p no:cacheprovider`
- Run the CLI: `.\.venv\Scripts\alarm.exe <command>` or `python -m alarm_clock <command>`

There's no linter or formatter configured. The version lives only in `alarm_clock/__init__.py` (`pyproject.toml` reads it dynamically). `.gitattributes` keeps text files LF.

The repo is on a OneDrive-synced Desktop, so pip can fail with "WinError 32 … used by another process" when OneDrive locks files during a sync. If that happens, retry, or pause OneDrive. Don't self-upgrade pip in the venv: an interrupted upgrade left pip broken once already.

## Architecture

`alarm_clock/` is split so that the time logic is pure and all I/O is injectable:

- `timeutil.py` holds the pure logic. It never reads the clock itself: every function that needs the time takes `now` as an argument. Key pieces:
  - `resolve_local(day, time, tz, prefer)` is the single place where DST is handled. It compares the fold=0 and fold=1 UTC offsets. If they differ and a UTC round-trip changes the wall time, the time is in a spring-forward gap, so it moves forward by the gap. Otherwise the time is ambiguous (fall-back) and it picks the first or second occurrence. It returns a `Resolved(dt, note)`, where `note` is the plain-language explanation shown to the user.
  - `next_occurrence` and `convert` both go through `resolve_local`. Always compare instants via `Resolved.utc`. Comparing aware datetimes that share a tzinfo ignores the offset and gets fold cases wrong.
  - `all_zones()` is the cached zone list that everything uses, so search, lookup and suggestions agree. It drops the non-location placeholders in `_NOT_REAL_ZONES` (`localtime`, `Factory`).
  - `AlarmError` is the only user-facing exception. `cli.main` prints it as `error: …` and exits with code 2. argparse usage errors also exit 2, and Ctrl+C exits 130. Unknown zones get `difflib` suggestions (`suggest_zones`), matched on both the full name and the city segment.
  - `local_zone()` checks `$TZ`, then `/etc/localtime` (POSIX), then the Windows registry key mapped through `WINDOWS_TO_IANA`. Any Windows zone missing from that map falls back to a fixed offset, which doesn't follow DST.
- `countdown.py` defines the `Clock` protocol (`now()` returns aware UTC; `sleep()`) and `SystemClock`. `wait_until` re-reads the clock every tick. `StatusLine` redraws one line with `\r` on a TTY, and prints a line every ~15 s when output is piped.
- `ringer.py` handles sound and key input. Sound runs in a daemon thread: `winsound` on Windows, then `afplay`, `paplay`, `aplay`, then the terminal bell. `KeyReader` uses `msvcrt` on Windows, termios+select on POSIX, or a shared background line reader when stdin isn't a TTY. `ring()` returns `stop`, `snooze`, `timeout` or `cancelled`, and always auto-stops after `ring_seconds`, so it never hangs unattended.
- `cli.py` builds the argparse subcommands; each one is `cmd_*(args, clock, ringer)`. `main(argv, clock=None, ringer=None)` is the injection point that tests use. `multi` runs one worker thread per alarm. A shared `console` lock means only one alarm rings and reads keys at a time, and the main thread only redraws the status line when it can take that lock. A shared `stop` event handles Ctrl+C.

## Conventions

- Type hints and short docstrings on all public functions.
- User-facing errors are plain-language, with a "did you mean ...?" suggestion for bad zone names.
- Keep functions small. Don't add features that weren't asked for.

## Docs that must track the CLI

- `COMMANDS.md` documents every option and value and all error cases. Lines ending in `# exits 2` are expected errors; every other `alarm …` line must succeed. `tests/test_docs.py` enforces this by running every `alarm …` line in ```` ```bash ```` blocks of `COMMANDS.md` and `README.md` (with an instant clock and a silent ringer). When you add, rename or remove an option, choice or error message, update `COMMANDS.md`, the README command table, and the README's ringing and exit-code notes.
- The example dates in `COMMANDS.md` (Dec 2026 to Nov 2027) must stay in the future: `set --date` rejects past dates. Pick a later year once they pass.
- `ZONES.md` is a generated snapshot (Nov 2026, tzdata 2026.6) of all zones with offsets and next clock change. Its generator wasn't kept in the repo. Regenerate it only when asked.

## Testing

`tests/conftest.py` provides a thread-safe `FakeClock` (fixture `fake_clock`, starting at 2026-11-04 10:00 UTC) whose `sleep` advances time instantly. Tests must never really sleep or ring:
- **CLI tests:** pass `clock=` and a fake `ringer=` to `main()` (see `FakeRinger` in `tests/test_cli.py`).
- **Ringer tests:** monkeypatch `ringer.play_once` and `ringer.KeyReader` (see `FakeKeys` in `tests/test_ringer.py`).

DST tests use real 2026 transitions: America/New_York changes on 2026-03-08 and 2026-11-01, Europe/London on 2026-03-29.

Run the full test suite after every change to time logic, and fix failures before moving on.
