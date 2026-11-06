# alarm — every command, with examples

Every subcommand, option and option value, the combinations that interact, and the error
cases. Lines marked `# exits 2` are deliberate mistakes that show the friendly error.
`tests/test_docs.py` runs every example here, so the file stays in step with the CLI.

**Running it:**
- **With the venv activated** (`.\.venv\Scripts\Activate.ps1`): type `alarm ...` as shown.
- **Without activating:** use `.\.venv\Scripts\alarm.exe ...` or `python -m alarm_clock ...`.
- **Quoting:** examples use double quotes, which work the same in PowerShell, cmd and bash.

Dates below are in the future relative to Nov 2026; pick your own future dates when you run them.

---

## 1. Help and version

```bash
alarm --help
alarm --version
alarm set --help
alarm zones --help
alarm now --help
alarm convert --help
alarm multi --help
python -m alarm_clock --help          # same CLI without the alarm.exe launcher
```

---

## 2. `alarm zones [SEARCH]` — list/search timezones

Case-insensitive substring match; spaces match underscores. Each zone shows its current UTC offset.

```bash
alarm zones                           # all ~600 zones
alarm zones kolkata                   # Asia/Kolkata  UTC+05:30
alarm zones KOLKATA                   # case doesn't matter
alarm zones america/                  # every America/... zone
alarm zones europe/                   # every Europe/... zone
alarm zones "new york"                # space matches underscore -> America/New_York
alarm zones new_york                  # same result
alarm zones london
alarm zones australia
alarm zones etc/gmt                   # fixed-offset Etc/GMT±N zones
alarm zones utc
alarm zones us/                       # legacy aliases like US/Eastern
```

Errors:

```bash
alarm zones kolkatta                  # exits 2: no match, "Did you mean: Asia/Kolkata ...?"
alarm zones atlantis                  # exits 2: no match, no suggestions
```

---

## 3. `alarm now [--tz ZONE ...]` — current time in one or more zones

```bash
alarm now                                             # system local zone
alarm now --tz Asia/Kolkata
alarm now --tz asia/kolkata                           # case-insensitive
alarm now --tz Asia/Kolkata --tz America/New_York
alarm now --tz UTC --tz Europe/London --tz Asia/Tokyo --tz Australia/Sydney --tz America/Los_Angeles
alarm now --tz Asia/Kathmandu                         # UTC+05:45 (45-minute offset)
alarm now --tz America/St_Johns                       # UTC-03:30 / -02:30
alarm now --tz Australia/Lord_Howe                    # 30-minute DST shift
alarm now --tz Etc/GMT+5                              # note: means UTC-05:00
alarm now --tz US/Eastern                             # legacy alias works too
```

Errors:

```bash
alarm now --tz Asia/Kolkatta                          # exits 2: "Did you mean: Asia/Kolkata?"
alarm now --tz "New York"                             # exits 2: suggests America/New_York
alarm now --tz Mars/Olympus_Mons                      # exits 2: unknown timezone
```

---

## 4. `alarm convert HH:MM --from ZONE --to ZONE [--date YYYY-MM-DD] [--ambiguous first|second]`

`--date` is the date in the `--from` zone (default: today there). A day change is shown as `(+1 day)` / `(-1 day)`.

```bash
alarm convert 09:00 --from Asia/Kolkata --to America/New_York               # today
alarm convert 09:00 --from Asia/Kolkata --to America/New_York --date 2026-12-01
alarm convert 20:00 --from America/New_York --to Asia/Kolkata --date 2026-12-01   # (+1 day)
alarm convert 09:00 --from Asia/Kolkata --to America/Los_Angeles --date 2026-12-01 # (-1 day)
alarm convert 12:00 --from UTC --to Asia/Kathmandu --date 2026-12-01        # 17:45
alarm convert 12:00 --from Europe/London --to Europe/London --date 2026-12-01   # same zone
alarm convert 7:05 --from utc --to asia/tokyo --date 2026-12-01            # 1-digit hour, lowercase zones
alarm convert 00:00 --from Pacific/Kiritimati --to Pacific/Pago_Pago --date 2026-12-01  # 25 h apart (-2 days)
alarm convert 09:00 --from Asia/Kolkata --to America/New_York --date 2027-07-01 # summer: EDT, not EST
alarm convert 09:00 --from Asia/Kolkata --to America/New_York --date 2026-01-15 # past dates are fine here
```

DST edge cases:

```bash
# Nonexistent time (clocks jump 02:00 -> 03:00): treated as 03:30, with an explanation
alarm convert 02:30 --from America/New_York --to UTC --date 2027-03-14

# Ambiguous time (01:30 happens twice): first (EDT) by default, or the second (EST)
alarm convert 01:30 --from America/New_York --to UTC --date 2027-11-07
alarm convert 01:30 --from America/New_York --to UTC --date 2027-11-07 --ambiguous first
alarm convert 01:30 --from America/New_York --to UTC --date 2027-11-07 --ambiguous second

# Europe/London: gap and overlap
alarm convert 01:30 --from Europe/London --to Asia/Kolkata --date 2027-03-28
alarm convert 01:30 --from Europe/London --to Asia/Kolkata --date 2027-10-31 --ambiguous second
```

Errors:

```bash
alarm convert 09:00 --from Asia/Kolkata                         # exits 2: --to is required
alarm convert 09:00 --to UTC                                    # exits 2: --from is required
alarm convert 9am --from UTC --to Asia/Tokyo                    # exits 2: not HH:MM
alarm convert 24:00 --from UTC --to Asia/Tokyo                  # exits 2: hour out of range
alarm convert 09:00 --from Asia/Kolkatta --to UTC               # exits 2: unknown zone + suggestion
alarm convert 09:00 --from UTC --to Asia/Tokyo --date 2026-02-30   # exits 2: invalid date
alarm convert 09:00 --from UTC --to Asia/Tokyo --ambiguous last    # exits 2: invalid choice
```

---

## 5. `alarm set HH:MM [options]` — one alarm in the foreground

Options:

| Option | Values | Default |
|---|---|---|
| `--tz ZONE` | any IANA zone | system local zone |
| `--date YYYY-MM-DD` | a future date | next occurrence of HH:MM |
| `--label TEXT` | any text | `Alarm` |
| `--repeat` | `none`, `daily`, `weekdays` | `none` |
| `--snooze N` | minutes, `0` disables snooze | `5` |
| `--ring-seconds N` | seconds before ringing stops by itself (1 or more) | `60` |
| `--ambiguous` | `first`, `second` (only matters on a DST fall-back day) | `first` |

While ringing: **Enter** stops, **s** snoozes (with piped input: an empty line stops, `s` + Enter snoozes). **Ctrl+C** cancels at any time (exit code 130).

Time formats:

```bash
alarm set 07:30
alarm set 7:30                        # leading zero optional
alarm set 00:00                       # midnight
alarm set 23:59
```

Each option on its own:

```bash
alarm set 07:30 --tz Asia/Kolkata
alarm set 07:30 --tz america/new_york                # case-insensitive
alarm set 07:30 --date 2026-12-25
alarm set 07:30 --label "Wake up"
alarm set 07:30 --repeat none
alarm set 07:30 --repeat daily
alarm set 07:30 --repeat weekdays                    # skips Saturday and Sunday
alarm set 07:30 --snooze 10
alarm set 07:30 --snooze 1
alarm set 07:30 --snooze 0                           # snooze disabled, only Enter stops
alarm set 07:30 --ring-seconds 5
alarm set 07:30 --ring-seconds 300
alarm set 07:30 --ambiguous second
```

Pairs and combinations:

```bash
alarm set 09:00 --tz Asia/Kolkata --date 2026-12-01
alarm set 09:00 --tz Asia/Kolkata --label Standup
alarm set 09:00 --tz Asia/Kolkata --repeat daily
alarm set 09:00 --tz Asia/Kolkata --repeat weekdays --label Standup
alarm set 09:00 --date 2026-12-01 --label "Dentist"
alarm set 09:00 --date 2026-12-01 --repeat daily     # starts on that date, then every day
alarm set 09:00 --date 2026-12-07 --repeat weekdays  # starts Monday 7 Dec, then Mon-Fri
alarm set 06:00 --repeat daily --snooze 9 --ring-seconds 120
alarm set 06:00 --repeat weekdays --snooze 0 --label "No snoozing"
alarm set 14:00 --tz Europe/London --label "Call London" --snooze 2 --ring-seconds 30
alarm set 21:00 --tz Asia/Tokyo --date 2026-12-31 --label "New Year in Tokyo" --ring-seconds 600
alarm set --tz Asia/Tokyo --label Call 21:00         # options may come before the time
```

Everything at once:

```bash
alarm set 06:45 --tz Europe/London --date 2026-12-01 --label "Morning run" --repeat weekdays --snooze 10 --ring-seconds 120 --ambiguous second
```

DST edge cases (the CLI explains what happened in plain language):

```bash
# Spring forward, so the time doesn't exist; the alarm moves to 03:30 EDT
alarm set 02:30 --tz America/New_York --date 2027-03-14
alarm set 01:30 --tz Europe/London --date 2027-03-28          # moves to 02:30 BST
alarm set 02:15 --tz Australia/Lord_Howe --date 2027-10-03    # 30-minute jump, moves to 02:45

# Fall back, so the time happens twice; first by default, or pick the second
alarm set 01:30 --tz America/New_York --date 2027-11-07
alarm set 01:30 --tz America/New_York --date 2027-11-07 --ambiguous first
alarm set 01:30 --tz America/New_York --date 2027-11-07 --ambiguous second
alarm set 01:30 --tz Europe/London --date 2027-10-31 --ambiguous second

# Daily repeat through a DST change keeps the same wall-clock time (gap is 23 or 25 real hours)
alarm set 02:30 --tz America/New_York --repeat daily
alarm set 07:00 --tz Europe/London --repeat weekdays --ambiguous second
```

Errors:

```bash
alarm set                                         # exits 2: time is required
alarm set 25:00                                   # exits 2: hour out of range
alarm set 12:60                                   # exits 2: minute out of range
alarm set 7pm                                     # exits 2: not HH:MM
alarm set 7:5                                     # exits 2: minutes need two digits
alarm set 07:30 --date 2026-01-01                 # exits 2: date in the past
alarm set 07:30 --date 2026-13-01                 # exits 2: invalid date
alarm set 07:30 --date 01/12/2026                 # exits 2: wrong date format
alarm set 07:30 --tz Asia/Kolkatta                # exits 2: unknown zone + "Did you mean"
alarm set 07:30 --repeat hourly                   # exits 2: invalid choice
alarm set 07:30 --snooze -5                       # exits 2: must be 0 or more
alarm set 07:30 --snooze abc                      # exits 2: not a whole number
alarm set 07:30 --ring-seconds ten                # exits 2: not a whole number
alarm set 07:30 --ring-seconds 0                  # exits 2: must be at least 1 (a 0 s alarm is silent)
alarm set 07:30 --ambiguous last                  # exits 2: invalid choice
```

---

## 6. `alarm multi --at "HH:MM@ZONE" ... [--label TEXT ...] [options]` — several alarms at once

- **Times and zones:** each `--at` is `HH:MM@Zone`. The zone is optional (`HH:MM` alone uses local time).
- **Labels:** `--label` values pair with the `--at` values in order. Any `--at` without a label uses its own text as the label.
- **Shared options:** `--snooze`, `--ring-seconds` and `--ambiguous` apply to every alarm.
- **Ringing:** alarms ring one at a time, and Ctrl+C cancels all of them.

```bash
alarm multi --at "09:00@Asia/Kolkata"
alarm multi --at "09:00@Asia/Kolkata" --at "14:30@Europe/London"
alarm multi --at "09:00@Asia/Kolkata" --at "14:30@Europe/London" --label Standup --label Review
alarm multi --at "09:00@Asia/Kolkata" --at "14:30@Europe/London" --label Standup   # 2nd label = "14:30@Europe/London"
alarm multi --at "07:00" --at "07:15"                                               # local time, no zone
alarm multi --at "07:00" --at "18:00@America/New_York" --label "Local" --label "NY close"
alarm multi --at "09:00@asia/kolkata" --at "09:00@europe/london"                    # same time, different zones
alarm multi --at "08:00@Asia/Tokyo" --at "08:00@Europe/Paris" --at "08:00@America/Chicago" --at "08:00@Australia/Sydney" --label Tokyo --label Paris --label Chicago --label Sydney
```

With shared options:

```bash
alarm multi --at "09:00@Asia/Kolkata" --at "14:30@Europe/London" --snooze 10
alarm multi --at "09:00@Asia/Kolkata" --at "14:30@Europe/London" --snooze 0
alarm multi --at "09:00@Asia/Kolkata" --at "14:30@Europe/London" --ring-seconds 15
alarm multi --at "01:30@America/New_York" --at "01:30@Europe/London" --ambiguous second
alarm multi --at "09:00@Asia/Kolkata" --at "14:30@Europe/London" --label A --label B --snooze 3 --ring-seconds 20 --ambiguous first
```

Errors:

```bash
alarm multi                                                     # exits 2: at least one --at is required
alarm multi --at "7h30@UTC"                                     # exits 2: not HH:MM
alarm multi --at "09:00@Asia/Kolkatta"                          # exits 2: unknown zone + suggestion
alarm multi --at "09:00@UTC" --label One --label Two            # exits 2: more labels than --at values
alarm multi --at "09:00@UTC" --snooze -1                        # exits 2: must be 0 or more
```

---

## 7. Exit codes

| Code | Meaning |
|---|---|
| `0` | Success (alarm rang and was stopped/timed out, or a query command finished) |
| `2` | Invalid input: bad time/date/zone, past date, or a usage error |
| `130` | Cancelled with Ctrl+C |
