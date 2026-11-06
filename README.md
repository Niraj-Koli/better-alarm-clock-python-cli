# alarm — a timezone-aware CLI alarm clock

Set alarms in any of the ~600 IANA timezones, convert times between zones, and get a plain-language
explanation when daylight saving shifts or duplicates your alarm time.

- **Requirements:** Python 3.9+. The only dependency is `tzdata`, which supplies timezone data on Windows.
- **No setup or storage:** there's no database, server, network access or config file. Alarms live in memory while the command runs.

## Install

The project already has a virtual environment in `.venv`:

```powershell
.\.venv\Scripts\Activate.ps1      # Windows PowerShell
source .venv/bin/activate         # macOS / Linux
alarm --help
```

If PowerShell blocks the activate script, run
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once. You can also skip activation and call
`.\.venv\Scripts\alarm.exe` directly.

To set up from scratch on another machine:

```bash
python -m venv .venv
# activate it as above, then:
pip install -e ".[dev]"           # the `alarm` command + pytest
```

`python -m alarm_clock ...` always works, even if `alarm` isn't on your `PATH`.

## Commands

| Command | What it does |
|---|---|
| `alarm set HH:MM` | One alarm in the foreground with a live countdown |
| `alarm multi --at "HH:MM@Zone" ...` | Several alarms at once, each with its own label |
| `alarm now [--tz Zone ...]` | Current time in one or more zones |
| `alarm convert HH:MM --from Zone --to Zone` | Convert a time between zones |
| `alarm zones [SEARCH]` | List or search zones with their current UTC offset |

```bash
alarm set 07:30 --label "Wake up"                       # next 07:30, local time
alarm set 09:00 --tz Asia/Kolkata --date 2026-12-01 --label Standup --snooze 10
alarm set 06:45 --repeat weekdays                       # repeat: none | daily | weekdays
alarm multi --at "09:00@Asia/Kolkata" --at "14:30@Europe/London" --label Standup --label Review
alarm now --tz Asia/Kolkata --tz America/New_York
alarm convert 09:00 --from Asia/Kolkata --to America/New_York   # date defaults to today in --from
alarm zones kolkata                                     # case-insensitive substring
```

**[COMMANDS.md](COMMANDS.md)** has every option and value, the combinations that interact, and all
error cases (129 examples, each checked against the CLI).
**[ZONES.md](ZONES.md)** lists every supported zone with its offsets and next clock change. It's a
snapshot from Nov 2026; `alarm zones` always shows live data.

### When an alarm rings

- **Stop:** press **Enter**.
- **Snooze:** press **s** to snooze for `--snooze` minutes (default 5; `0` disables snooze).
- **Piped input:** if input comes from a pipe rather than a terminal, an empty line stops and `s` + Enter snoozes.
- **Auto-stop:** ringing stops by itself after `--ring-seconds` (default 60).
- **Cancel:** **Ctrl+C** cancels at any time, including all alarms in `multi`.
- **Sound:** `winsound` on Windows, `afplay` on macOS, `paplay`/`aplay` on Linux, or the terminal bell if none of those are available.

Exit codes: `0` success, `2` invalid input (with a "did you mean …?" hint for misspelled zones),
`130` cancelled.

## Daylight saving time

- **Times that don't exist** move forward by the size of the jump, and the CLI says so. For
  example, 02:30 in New York on 2027-03-14 becomes 03:30 EDT.
- **Times that happen twice** use the first occurrence. Pass `--ambiguous second` for the later
  one, e.g. 01:30 in New York on 2027-11-07.
- **Daily repeats** keep the same wall-clock time, so across a change the gap between alarms is 23
  or 25 real hours.

**Local time:** without `--tz`, alarms use your system timezone. That comes from `$TZ`, then
`/etc/localtime`, then (on Windows) the registry setting, mapped to an IANA name. Uncommon Windows
zones fall back to a fixed UTC offset that ignores daylight saving. In that case, pass `--tz`
explicitly.

## Development

```bash
python -m pytest -q                       # full suite; fake clock, so it runs in about a second
python -m pytest tests/test_timeutil.py -q
uv run --no-project --python 3.9 --with pytest --with tzdata python -m pytest -q -p no:cacheprovider   # check 3.9
```

| Path | Purpose |
|---|---|
| `alarm_clock/timeutil.py` | Parsing, zone lookup and suggestions, DST resolution, next occurrence (pure, no I/O) |
| `alarm_clock/countdown.py` | Injectable `Clock`, `wait_until`, status line |
| `alarm_clock/ringer.py` | Sound playback and Enter/snooze key handling |
| `alarm_clock/cli.py` | argparse subcommands |
| `tests/` | pytest suite (fake clock and fake ringer, never sleeps or plays sound) |
