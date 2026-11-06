# Supported timezones

All 597 IANA timezones accepted by `alarm` (`--tz`, `--from`, `--to`, `--at HH:MM@Zone`).

- Generated 2026-11-04 12:50 UTC from `tzdata` 2026.6 via `zoneinfo.available_timezones()`, which is the same source the app uses.
- This is a snapshot for reference. The app never reads this file. For live data use `alarm zones <search>` (and `alarm now --tz <Zone>`).
- Zone names are case-insensitive in the CLI. **Now** is the offset when this file was generated; **Jan**/**Jul** are mid-month 2026 offsets. If they differ, the zone observes daylight saving.
- `Etc/GMT+5` means UTC**-**05:00 (POSIX sign convention); prefer a city zone where possible.

## Regions

[Africa](#africa) (54) · [America](#america) (169) · [Antarctica](#antarctica) (12) · [Arctic](#arctic) (1) · [Asia](#asia) (99) · [Atlantic](#atlantic) (12) · [Australia](#australia) (23) · [Europe](#europe) (64) · [Indian](#indian) (11) · [Pacific](#pacific) (44) · [Etc](#etc) (35) · [Other (aliases & legacy names)](#other-aliases--legacy-names) (73)

## Africa

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Africa/Abidjan` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Accra` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Addis_Ababa` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Africa/Algiers` | UTC+01:00 CET | UTC+01:00 CET | UTC+01:00 CET |  | — |
| `Africa/Asmara` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Africa/Asmera` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Africa/Bamako` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Bangui` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/Banjul` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Bissau` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Blantyre` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |
| `Africa/Brazzaville` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/Bujumbura` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |
| `Africa/Cairo` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-04-30 → UTC+03:00 (EEST) |
| `Africa/Casablanca` | UTC+00:00 +00 | UTC+01:00 +01 | UTC+01:00 +01 |  | — |
| `Africa/Ceuta` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Africa/Conakry` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Dakar` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Dar_es_Salaam` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Africa/Djibouti` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Africa/Douala` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/El_Aaiun` | UTC+00:00 +00 | UTC+01:00 +01 | UTC+01:00 +01 |  | — |
| `Africa/Freetown` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Gaborone` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |
| `Africa/Harare` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |
| `Africa/Johannesburg` | UTC+02:00 SAST | UTC+02:00 SAST | UTC+02:00 SAST |  | — |
| `Africa/Juba` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |
| `Africa/Kampala` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Africa/Khartoum` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |
| `Africa/Kigali` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |
| `Africa/Kinshasa` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/Lagos` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/Libreville` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/Lome` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Luanda` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/Lubumbashi` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |
| `Africa/Lusaka` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |
| `Africa/Malabo` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/Maputo` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |
| `Africa/Maseru` | UTC+02:00 SAST | UTC+02:00 SAST | UTC+02:00 SAST |  | — |
| `Africa/Mbabane` | UTC+02:00 SAST | UTC+02:00 SAST | UTC+02:00 SAST |  | — |
| `Africa/Mogadishu` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Africa/Monrovia` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Nairobi` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Africa/Ndjamena` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/Niamey` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/Nouakchott` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Ouagadougou` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Porto-Novo` | UTC+01:00 WAT | UTC+01:00 WAT | UTC+01:00 WAT |  | — |
| `Africa/Sao_Tome` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Timbuktu` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Africa/Tripoli` | UTC+02:00 EET | UTC+02:00 EET | UTC+02:00 EET |  | — |
| `Africa/Tunis` | UTC+01:00 CET | UTC+01:00 CET | UTC+01:00 CET |  | — |
| `Africa/Windhoek` | UTC+02:00 CAT | UTC+02:00 CAT | UTC+02:00 CAT |  | — |

## America

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `America/Adak` | UTC-10:00 HST | UTC-10:00 HST | UTC-09:00 HDT | yes | 2027-03-14 → UTC-09:00 (HDT) |
| `America/Anchorage` | UTC-09:00 AKST | UTC-09:00 AKST | UTC-08:00 AKDT | yes | 2027-03-14 → UTC-08:00 (AKDT) |
| `America/Anguilla` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Antigua` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Araguaina` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/Buenos_Aires` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/Catamarca` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/ComodRivadavia` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/Cordoba` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/Jujuy` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/La_Rioja` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/Mendoza` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/Rio_Gallegos` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/Salta` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/San_Juan` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/San_Luis` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/Tucuman` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Argentina/Ushuaia` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Aruba` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Asuncion` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Atikokan` | UTC-05:00 EST | UTC-05:00 EST | UTC-05:00 EST |  | — |
| `America/Atka` | UTC-10:00 HST | UTC-10:00 HST | UTC-09:00 HDT | yes | 2027-03-14 → UTC-09:00 (HDT) |
| `America/Bahia` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Bahia_Banderas` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Barbados` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Belem` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Belize` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Blanc-Sablon` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Boa_Vista` | UTC-04:00 -04 | UTC-04:00 -04 | UTC-04:00 -04 |  | — |
| `America/Bogota` | UTC-05:00 -05 | UTC-05:00 -05 | UTC-05:00 -05 |  | — |
| `America/Boise` | UTC-07:00 MST | UTC-07:00 MST | UTC-06:00 MDT | yes | 2027-03-14 → UTC-06:00 (MDT) |
| `America/Buenos_Aires` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Cambridge_Bay` | UTC-07:00 MST | UTC-07:00 MST | UTC-06:00 MDT | yes | 2027-03-14 → UTC-06:00 (MDT) |
| `America/Campo_Grande` | UTC-04:00 -04 | UTC-04:00 -04 | UTC-04:00 -04 |  | — |
| `America/Cancun` | UTC-05:00 EST | UTC-05:00 EST | UTC-05:00 EST |  | — |
| `America/Caracas` | UTC-04:00 -04 | UTC-04:00 -04 | UTC-04:00 -04 |  | — |
| `America/Catamarca` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Cayenne` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Cayman` | UTC-05:00 EST | UTC-05:00 EST | UTC-05:00 EST |  | — |
| `America/Chicago` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/Chihuahua` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Ciudad_Juarez` | UTC-07:00 MST | UTC-07:00 MST | UTC-06:00 MDT | yes | 2027-03-14 → UTC-06:00 (MDT) |
| `America/Coral_Harbour` | UTC-05:00 EST | UTC-05:00 EST | UTC-05:00 EST |  | — |
| `America/Cordoba` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Costa_Rica` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Coyhaique` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Creston` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `America/Cuiaba` | UTC-04:00 -04 | UTC-04:00 -04 | UTC-04:00 -04 |  | — |
| `America/Curacao` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Danmarkshavn` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `America/Dawson` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `America/Dawson_Creek` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `America/Denver` | UTC-07:00 MST | UTC-07:00 MST | UTC-06:00 MDT | yes | 2027-03-14 → UTC-06:00 (MDT) |
| `America/Detroit` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Dominica` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Edmonton` | UTC-06:00 CST | UTC-07:00 MST | UTC-06:00 MDT | yes | — |
| `America/Eirunepe` | UTC-05:00 -05 | UTC-05:00 -05 | UTC-05:00 -05 |  | — |
| `America/El_Salvador` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Ensenada` | UTC-08:00 PST | UTC-08:00 PST | UTC-07:00 PDT | yes | 2027-03-14 → UTC-07:00 (PDT) |
| `America/Fort_Nelson` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `America/Fort_Wayne` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Fortaleza` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Glace_Bay` | UTC-04:00 AST | UTC-04:00 AST | UTC-03:00 ADT | yes | 2027-03-14 → UTC-03:00 (ADT) |
| `America/Godthab` | UTC-02:00 -02 | UTC-02:00 -02 | UTC-01:00 -01 | yes | 2027-03-28 → UTC-01:00 (-01) |
| `America/Goose_Bay` | UTC-04:00 AST | UTC-04:00 AST | UTC-03:00 ADT | yes | 2027-03-14 → UTC-03:00 (ADT) |
| `America/Grand_Turk` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Grenada` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Guadeloupe` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Guatemala` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Guayaquil` | UTC-05:00 -05 | UTC-05:00 -05 | UTC-05:00 -05 |  | — |
| `America/Guyana` | UTC-04:00 -04 | UTC-04:00 -04 | UTC-04:00 -04 |  | — |
| `America/Halifax` | UTC-04:00 AST | UTC-04:00 AST | UTC-03:00 ADT | yes | 2027-03-14 → UTC-03:00 (ADT) |
| `America/Havana` | UTC-04:00 CDT | UTC-05:00 CST | UTC-04:00 CDT | yes | — |
| `America/Hermosillo` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `America/Indiana/Indianapolis` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Indiana/Knox` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/Indiana/Marengo` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Indiana/Petersburg` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Indiana/Tell_City` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/Indiana/Vevay` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Indiana/Vincennes` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Indiana/Winamac` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Indianapolis` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Inuvik` | UTC-06:00 CST | UTC-07:00 MST | UTC-06:00 MDT | yes | — |
| `America/Iqaluit` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Jamaica` | UTC-05:00 EST | UTC-05:00 EST | UTC-05:00 EST |  | — |
| `America/Jujuy` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Juneau` | UTC-09:00 AKST | UTC-09:00 AKST | UTC-08:00 AKDT | yes | 2027-03-14 → UTC-08:00 (AKDT) |
| `America/Kentucky/Louisville` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Kentucky/Monticello` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Knox_IN` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/Kralendijk` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/La_Paz` | UTC-04:00 -04 | UTC-04:00 -04 | UTC-04:00 -04 |  | — |
| `America/Lima` | UTC-05:00 -05 | UTC-05:00 -05 | UTC-05:00 -05 |  | — |
| `America/Los_Angeles` | UTC-08:00 PST | UTC-08:00 PST | UTC-07:00 PDT | yes | 2027-03-14 → UTC-07:00 (PDT) |
| `America/Louisville` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Lower_Princes` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Maceio` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Managua` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Manaus` | UTC-04:00 -04 | UTC-04:00 -04 | UTC-04:00 -04 |  | — |
| `America/Marigot` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Martinique` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Matamoros` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/Mazatlan` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `America/Mendoza` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Menominee` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/Merida` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Metlakatla` | UTC-09:00 AKST | UTC-09:00 AKST | UTC-08:00 AKDT | yes | 2027-03-14 → UTC-08:00 (AKDT) |
| `America/Mexico_City` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Miquelon` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-02:00 -02 | yes | 2027-03-14 → UTC-02:00 (-02) |
| `America/Moncton` | UTC-04:00 AST | UTC-04:00 AST | UTC-03:00 ADT | yes | 2027-03-14 → UTC-03:00 (ADT) |
| `America/Monterrey` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Montevideo` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Montreal` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Montserrat` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Nassau` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/New_York` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Nipigon` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Nome` | UTC-09:00 AKST | UTC-09:00 AKST | UTC-08:00 AKDT | yes | 2027-03-14 → UTC-08:00 (AKDT) |
| `America/Noronha` | UTC-02:00 -02 | UTC-02:00 -02 | UTC-02:00 -02 |  | — |
| `America/North_Dakota/Beulah` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/North_Dakota/Center` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/North_Dakota/New_Salem` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/Nuuk` | UTC-02:00 -02 | UTC-02:00 -02 | UTC-01:00 -01 | yes | 2027-03-28 → UTC-01:00 (-01) |
| `America/Ojinaga` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/Panama` | UTC-05:00 EST | UTC-05:00 EST | UTC-05:00 EST |  | — |
| `America/Pangnirtung` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Paramaribo` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Phoenix` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `America/Port-au-Prince` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Port_of_Spain` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Porto_Acre` | UTC-05:00 -05 | UTC-05:00 -05 | UTC-05:00 -05 |  | — |
| `America/Porto_Velho` | UTC-04:00 -04 | UTC-04:00 -04 | UTC-04:00 -04 |  | — |
| `America/Puerto_Rico` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Punta_Arenas` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Rainy_River` | UTC-05:00 EST | UTC-06:00 CST | UTC-05:00 CDT | yes | — |
| `America/Rankin_Inlet` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/Recife` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Regina` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Resolute` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `America/Rio_Branco` | UTC-05:00 -05 | UTC-05:00 -05 | UTC-05:00 -05 |  | — |
| `America/Rosario` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Santa_Isabel` | UTC-08:00 PST | UTC-08:00 PST | UTC-07:00 PDT | yes | 2027-03-14 → UTC-07:00 (PDT) |
| `America/Santarem` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Santiago` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-04:00 -04 | yes | 2027-04-03 → UTC-04:00 (-04) |
| `America/Santo_Domingo` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Sao_Paulo` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `America/Scoresbysund` | UTC-02:00 -02 | UTC-02:00 -02 | UTC-01:00 -01 | yes | 2027-03-28 → UTC-01:00 (-01) |
| `America/Shiprock` | UTC-07:00 MST | UTC-07:00 MST | UTC-06:00 MDT | yes | 2027-03-14 → UTC-06:00 (MDT) |
| `America/Sitka` | UTC-09:00 AKST | UTC-09:00 AKST | UTC-08:00 AKDT | yes | 2027-03-14 → UTC-08:00 (AKDT) |
| `America/St_Barthelemy` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/St_Johns` | UTC-03:30 NST | UTC-03:30 NST | UTC-02:30 NDT | yes | 2027-03-14 → UTC-02:30 (NDT) |
| `America/St_Kitts` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/St_Lucia` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/St_Thomas` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/St_Vincent` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Swift_Current` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Tegucigalpa` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `America/Thule` | UTC-04:00 AST | UTC-04:00 AST | UTC-03:00 ADT | yes | 2027-03-14 → UTC-03:00 (ADT) |
| `America/Thunder_Bay` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Tijuana` | UTC-08:00 PST | UTC-08:00 PST | UTC-07:00 PDT | yes | 2027-03-14 → UTC-07:00 (PDT) |
| `America/Toronto` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `America/Tortola` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Vancouver` | UTC-07:00 MST | UTC-08:00 PST | UTC-07:00 PDT | yes | — |
| `America/Virgin` | UTC-04:00 AST | UTC-04:00 AST | UTC-04:00 AST |  | — |
| `America/Whitehorse` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `America/Winnipeg` | UTC-05:00 EST | UTC-06:00 CST | UTC-05:00 CDT | yes | — |
| `America/Yakutat` | UTC-09:00 AKST | UTC-09:00 AKST | UTC-08:00 AKDT | yes | 2027-03-14 → UTC-08:00 (AKDT) |
| `America/Yellowknife` | UTC-06:00 CST | UTC-07:00 MST | UTC-06:00 MDT | yes | — |

## Antarctica

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Antarctica/Casey` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Antarctica/Davis` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Antarctica/DumontDUrville` | UTC+10:00 +10 | UTC+10:00 +10 | UTC+10:00 +10 |  | — |
| `Antarctica/Macquarie` | UTC+11:00 AEDT | UTC+11:00 AEDT | UTC+10:00 AEST | yes | 2027-04-04 → UTC+10:00 (AEST) |
| `Antarctica/Mawson` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Antarctica/McMurdo` | UTC+13:00 NZDT | UTC+13:00 NZDT | UTC+12:00 NZST | yes | 2027-04-04 → UTC+12:00 (NZST) |
| `Antarctica/Palmer` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `Antarctica/Rothera` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `Antarctica/South_Pole` | UTC+13:00 NZDT | UTC+13:00 NZDT | UTC+12:00 NZST | yes | 2027-04-04 → UTC+12:00 (NZST) |
| `Antarctica/Syowa` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Antarctica/Troll` | UTC+00:00 +00 | UTC+00:00 +00 | UTC+02:00 +02 | yes | 2027-03-28 → UTC+02:00 (+02) |
| `Antarctica/Vostok` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |

## Arctic

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Arctic/Longyearbyen` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |

## Asia

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Asia/Aden` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Asia/Almaty` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Amman` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Asia/Anadyr` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Asia/Aqtau` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Aqtobe` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Ashgabat` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Ashkhabad` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Atyrau` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Baghdad` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Asia/Bahrain` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Asia/Baku` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Asia/Bangkok` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Barnaul` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Beirut` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Asia/Bishkek` | UTC+06:00 +06 | UTC+06:00 +06 | UTC+06:00 +06 |  | — |
| `Asia/Brunei` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Asia/Calcutta` | UTC+05:30 IST | UTC+05:30 IST | UTC+05:30 IST |  | — |
| `Asia/Chita` | UTC+09:00 +09 | UTC+09:00 +09 | UTC+09:00 +09 |  | — |
| `Asia/Choibalsan` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Asia/Chongqing` | UTC+08:00 CST | UTC+08:00 CST | UTC+08:00 CST |  | — |
| `Asia/Chungking` | UTC+08:00 CST | UTC+08:00 CST | UTC+08:00 CST |  | — |
| `Asia/Colombo` | UTC+05:30 +0530 | UTC+05:30 +0530 | UTC+05:30 +0530 |  | — |
| `Asia/Dacca` | UTC+06:00 +06 | UTC+06:00 +06 | UTC+06:00 +06 |  | — |
| `Asia/Damascus` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Asia/Dhaka` | UTC+06:00 +06 | UTC+06:00 +06 | UTC+06:00 +06 |  | — |
| `Asia/Dili` | UTC+09:00 +09 | UTC+09:00 +09 | UTC+09:00 +09 |  | — |
| `Asia/Dubai` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Asia/Dushanbe` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Famagusta` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Asia/Gaza` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-27 → UTC+03:00 (EEST) |
| `Asia/Harbin` | UTC+08:00 CST | UTC+08:00 CST | UTC+08:00 CST |  | — |
| `Asia/Hebron` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-27 → UTC+03:00 (EEST) |
| `Asia/Ho_Chi_Minh` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Hong_Kong` | UTC+08:00 HKT | UTC+08:00 HKT | UTC+08:00 HKT |  | — |
| `Asia/Hovd` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Irkutsk` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Asia/Istanbul` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Asia/Jakarta` | UTC+07:00 WIB | UTC+07:00 WIB | UTC+07:00 WIB |  | — |
| `Asia/Jayapura` | UTC+09:00 WIT | UTC+09:00 WIT | UTC+09:00 WIT |  | — |
| `Asia/Jerusalem` | UTC+02:00 IST | UTC+02:00 IST | UTC+03:00 IDT | yes | 2027-03-26 → UTC+03:00 (IDT) |
| `Asia/Kabul` | UTC+04:30 +0430 | UTC+04:30 +0430 | UTC+04:30 +0430 |  | — |
| `Asia/Kamchatka` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Asia/Karachi` | UTC+05:00 PKT | UTC+05:00 PKT | UTC+05:00 PKT |  | — |
| `Asia/Kashgar` | UTC+06:00 +06 | UTC+06:00 +06 | UTC+06:00 +06 |  | — |
| `Asia/Kathmandu` | UTC+05:45 +0545 | UTC+05:45 +0545 | UTC+05:45 +0545 |  | — |
| `Asia/Katmandu` | UTC+05:45 +0545 | UTC+05:45 +0545 | UTC+05:45 +0545 |  | — |
| `Asia/Khandyga` | UTC+09:00 +09 | UTC+09:00 +09 | UTC+09:00 +09 |  | — |
| `Asia/Kolkata` | UTC+05:30 IST | UTC+05:30 IST | UTC+05:30 IST |  | — |
| `Asia/Krasnoyarsk` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Kuala_Lumpur` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Asia/Kuching` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Asia/Kuwait` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Asia/Macao` | UTC+08:00 CST | UTC+08:00 CST | UTC+08:00 CST |  | — |
| `Asia/Macau` | UTC+08:00 CST | UTC+08:00 CST | UTC+08:00 CST |  | — |
| `Asia/Magadan` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Asia/Makassar` | UTC+08:00 WITA | UTC+08:00 WITA | UTC+08:00 WITA |  | — |
| `Asia/Manila` | UTC+08:00 PST | UTC+08:00 PST | UTC+08:00 PST |  | — |
| `Asia/Muscat` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Asia/Nicosia` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Asia/Novokuznetsk` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Novosibirsk` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Omsk` | UTC+06:00 +06 | UTC+06:00 +06 | UTC+06:00 +06 |  | — |
| `Asia/Oral` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Phnom_Penh` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Pontianak` | UTC+07:00 WIB | UTC+07:00 WIB | UTC+07:00 WIB |  | — |
| `Asia/Pyongyang` | UTC+09:00 KST | UTC+09:00 KST | UTC+09:00 KST |  | — |
| `Asia/Qatar` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Asia/Qostanay` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Qyzylorda` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Rangoon` | UTC+06:30 +0630 | UTC+06:30 +0630 | UTC+06:30 +0630 |  | — |
| `Asia/Riyadh` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Asia/Saigon` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Sakhalin` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Asia/Samarkand` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Seoul` | UTC+09:00 KST | UTC+09:00 KST | UTC+09:00 KST |  | — |
| `Asia/Shanghai` | UTC+08:00 CST | UTC+08:00 CST | UTC+08:00 CST |  | — |
| `Asia/Singapore` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Asia/Srednekolymsk` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Asia/Taipei` | UTC+08:00 CST | UTC+08:00 CST | UTC+08:00 CST |  | — |
| `Asia/Tashkent` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Tbilisi` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Asia/Tehran` | UTC+03:30 +0330 | UTC+03:30 +0330 | UTC+03:30 +0330 |  | — |
| `Asia/Tel_Aviv` | UTC+02:00 IST | UTC+02:00 IST | UTC+03:00 IDT | yes | 2027-03-26 → UTC+03:00 (IDT) |
| `Asia/Thimbu` | UTC+06:00 +06 | UTC+06:00 +06 | UTC+06:00 +06 |  | — |
| `Asia/Thimphu` | UTC+06:00 +06 | UTC+06:00 +06 | UTC+06:00 +06 |  | — |
| `Asia/Tokyo` | UTC+09:00 JST | UTC+09:00 JST | UTC+09:00 JST |  | — |
| `Asia/Tomsk` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Ujung_Pandang` | UTC+08:00 WITA | UTC+08:00 WITA | UTC+08:00 WITA |  | — |
| `Asia/Ulaanbaatar` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Asia/Ulan_Bator` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Asia/Urumqi` | UTC+06:00 +06 | UTC+06:00 +06 | UTC+06:00 +06 |  | — |
| `Asia/Ust-Nera` | UTC+10:00 +10 | UTC+10:00 +10 | UTC+10:00 +10 |  | — |
| `Asia/Vientiane` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Asia/Vladivostok` | UTC+10:00 +10 | UTC+10:00 +10 | UTC+10:00 +10 |  | — |
| `Asia/Yakutsk` | UTC+09:00 +09 | UTC+09:00 +09 | UTC+09:00 +09 |  | — |
| `Asia/Yangon` | UTC+06:30 +0630 | UTC+06:30 +0630 | UTC+06:30 +0630 |  | — |
| `Asia/Yekaterinburg` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Asia/Yerevan` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |

## Atlantic

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Atlantic/Azores` | UTC-01:00 -01 | UTC-01:00 -01 | UTC+00:00 +00 | yes | 2027-03-28 → UTC+00:00 (+00) |
| `Atlantic/Bermuda` | UTC-04:00 AST | UTC-04:00 AST | UTC-03:00 ADT | yes | 2027-03-14 → UTC-03:00 (ADT) |
| `Atlantic/Canary` | UTC+00:00 WET | UTC+00:00 WET | UTC+01:00 WEST | yes | 2027-03-28 → UTC+01:00 (WEST) |
| `Atlantic/Cape_Verde` | UTC-01:00 -01 | UTC-01:00 -01 | UTC-01:00 -01 |  | — |
| `Atlantic/Faeroe` | UTC+00:00 WET | UTC+00:00 WET | UTC+01:00 WEST | yes | 2027-03-28 → UTC+01:00 (WEST) |
| `Atlantic/Faroe` | UTC+00:00 WET | UTC+00:00 WET | UTC+01:00 WEST | yes | 2027-03-28 → UTC+01:00 (WEST) |
| `Atlantic/Jan_Mayen` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Atlantic/Madeira` | UTC+00:00 WET | UTC+00:00 WET | UTC+01:00 WEST | yes | 2027-03-28 → UTC+01:00 (WEST) |
| `Atlantic/Reykjavik` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Atlantic/South_Georgia` | UTC-02:00 -02 | UTC-02:00 -02 | UTC-02:00 -02 |  | — |
| `Atlantic/St_Helena` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Atlantic/Stanley` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |

## Australia

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Australia/ACT` | UTC+11:00 AEDT | UTC+11:00 AEDT | UTC+10:00 AEST | yes | 2027-04-04 → UTC+10:00 (AEST) |
| `Australia/Adelaide` | UTC+10:30 ACDT | UTC+10:30 ACDT | UTC+09:30 ACST | yes | 2027-04-04 → UTC+09:30 (ACST) |
| `Australia/Brisbane` | UTC+10:00 AEST | UTC+10:00 AEST | UTC+10:00 AEST |  | — |
| `Australia/Broken_Hill` | UTC+10:30 ACDT | UTC+10:30 ACDT | UTC+09:30 ACST | yes | 2027-04-04 → UTC+09:30 (ACST) |
| `Australia/Canberra` | UTC+11:00 AEDT | UTC+11:00 AEDT | UTC+10:00 AEST | yes | 2027-04-04 → UTC+10:00 (AEST) |
| `Australia/Currie` | UTC+11:00 AEDT | UTC+11:00 AEDT | UTC+10:00 AEST | yes | 2027-04-04 → UTC+10:00 (AEST) |
| `Australia/Darwin` | UTC+09:30 ACST | UTC+09:30 ACST | UTC+09:30 ACST |  | — |
| `Australia/Eucla` | UTC+08:45 +0845 | UTC+08:45 +0845 | UTC+08:45 +0845 |  | — |
| `Australia/Hobart` | UTC+11:00 AEDT | UTC+11:00 AEDT | UTC+10:00 AEST | yes | 2027-04-04 → UTC+10:00 (AEST) |
| `Australia/LHI` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+10:30 +1030 | yes | 2027-04-04 → UTC+10:30 (+1030) |
| `Australia/Lindeman` | UTC+10:00 AEST | UTC+10:00 AEST | UTC+10:00 AEST |  | — |
| `Australia/Lord_Howe` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+10:30 +1030 | yes | 2027-04-04 → UTC+10:30 (+1030) |
| `Australia/Melbourne` | UTC+11:00 AEDT | UTC+11:00 AEDT | UTC+10:00 AEST | yes | 2027-04-04 → UTC+10:00 (AEST) |
| `Australia/NSW` | UTC+11:00 AEDT | UTC+11:00 AEDT | UTC+10:00 AEST | yes | 2027-04-04 → UTC+10:00 (AEST) |
| `Australia/North` | UTC+09:30 ACST | UTC+09:30 ACST | UTC+09:30 ACST |  | — |
| `Australia/Perth` | UTC+08:00 AWST | UTC+08:00 AWST | UTC+08:00 AWST |  | — |
| `Australia/Queensland` | UTC+10:00 AEST | UTC+10:00 AEST | UTC+10:00 AEST |  | — |
| `Australia/South` | UTC+10:30 ACDT | UTC+10:30 ACDT | UTC+09:30 ACST | yes | 2027-04-04 → UTC+09:30 (ACST) |
| `Australia/Sydney` | UTC+11:00 AEDT | UTC+11:00 AEDT | UTC+10:00 AEST | yes | 2027-04-04 → UTC+10:00 (AEST) |
| `Australia/Tasmania` | UTC+11:00 AEDT | UTC+11:00 AEDT | UTC+10:00 AEST | yes | 2027-04-04 → UTC+10:00 (AEST) |
| `Australia/Victoria` | UTC+11:00 AEDT | UTC+11:00 AEDT | UTC+10:00 AEST | yes | 2027-04-04 → UTC+10:00 (AEST) |
| `Australia/West` | UTC+08:00 AWST | UTC+08:00 AWST | UTC+08:00 AWST |  | — |
| `Australia/Yancowinna` | UTC+10:30 ACDT | UTC+10:30 ACDT | UTC+09:30 ACST | yes | 2027-04-04 → UTC+09:30 (ACST) |

## Europe

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Europe/Amsterdam` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Andorra` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Astrakhan` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Europe/Athens` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Belfast` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+01:00 BST | yes | 2027-03-28 → UTC+01:00 (BST) |
| `Europe/Belgrade` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Berlin` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Bratislava` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Brussels` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Bucharest` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Budapest` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Busingen` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Chisinau` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Copenhagen` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Dublin` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+01:00 IST | yes | 2027-03-28 → UTC+01:00 (IST) |
| `Europe/Gibraltar` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Guernsey` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+01:00 BST | yes | 2027-03-28 → UTC+01:00 (BST) |
| `Europe/Helsinki` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Isle_of_Man` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+01:00 BST | yes | 2027-03-28 → UTC+01:00 (BST) |
| `Europe/Istanbul` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Europe/Jersey` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+01:00 BST | yes | 2027-03-28 → UTC+01:00 (BST) |
| `Europe/Kaliningrad` | UTC+02:00 EET | UTC+02:00 EET | UTC+02:00 EET |  | — |
| `Europe/Kiev` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Kirov` | UTC+03:00 MSK | UTC+03:00 MSK | UTC+03:00 MSK |  | — |
| `Europe/Kyiv` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Lisbon` | UTC+00:00 WET | UTC+00:00 WET | UTC+01:00 WEST | yes | 2027-03-28 → UTC+01:00 (WEST) |
| `Europe/Ljubljana` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/London` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+01:00 BST | yes | 2027-03-28 → UTC+01:00 (BST) |
| `Europe/Luxembourg` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Madrid` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Malta` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Mariehamn` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Minsk` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Europe/Monaco` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Moscow` | UTC+03:00 MSK | UTC+03:00 MSK | UTC+03:00 MSK |  | — |
| `Europe/Nicosia` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Oslo` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Paris` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Podgorica` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Prague` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Riga` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Rome` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Samara` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Europe/San_Marino` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Sarajevo` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Saratov` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Europe/Simferopol` | UTC+03:00 MSK | UTC+03:00 MSK | UTC+03:00 MSK |  | — |
| `Europe/Skopje` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Sofia` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Stockholm` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Tallinn` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Tirane` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Tiraspol` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Ulyanovsk` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Europe/Uzhgorod` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Vaduz` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Vatican` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Vienna` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Vilnius` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Volgograd` | UTC+03:00 MSK | UTC+03:00 MSK | UTC+03:00 MSK |  | — |
| `Europe/Warsaw` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Zagreb` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Europe/Zaporozhye` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `Europe/Zurich` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |

## Indian

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Indian/Antananarivo` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Indian/Chagos` | UTC+06:00 +06 | UTC+06:00 +06 | UTC+06:00 +06 |  | — |
| `Indian/Christmas` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Indian/Cocos` | UTC+06:30 +0630 | UTC+06:30 +0630 | UTC+06:30 +0630 |  | — |
| `Indian/Comoro` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Indian/Kerguelen` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Indian/Mahe` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Indian/Maldives` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Indian/Mauritius` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Indian/Mayotte` | UTC+03:00 EAT | UTC+03:00 EAT | UTC+03:00 EAT |  | — |
| `Indian/Reunion` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |

## Pacific

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Pacific/Apia` | UTC+13:00 +13 | UTC+13:00 +13 | UTC+13:00 +13 |  | — |
| `Pacific/Auckland` | UTC+13:00 NZDT | UTC+13:00 NZDT | UTC+12:00 NZST | yes | 2027-04-04 → UTC+12:00 (NZST) |
| `Pacific/Bougainville` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Pacific/Chatham` | UTC+13:45 +1345 | UTC+13:45 +1345 | UTC+12:45 +1245 | yes | 2027-04-04 → UTC+12:45 (+1245) |
| `Pacific/Chuuk` | UTC+10:00 +10 | UTC+10:00 +10 | UTC+10:00 +10 |  | — |
| `Pacific/Easter` | UTC-05:00 -05 | UTC-05:00 -05 | UTC-06:00 -06 | yes | 2027-04-03 → UTC-06:00 (-06) |
| `Pacific/Efate` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Pacific/Enderbury` | UTC+13:00 +13 | UTC+13:00 +13 | UTC+13:00 +13 |  | — |
| `Pacific/Fakaofo` | UTC+13:00 +13 | UTC+13:00 +13 | UTC+13:00 +13 |  | — |
| `Pacific/Fiji` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Pacific/Funafuti` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Pacific/Galapagos` | UTC-06:00 -06 | UTC-06:00 -06 | UTC-06:00 -06 |  | — |
| `Pacific/Gambier` | UTC-09:00 -09 | UTC-09:00 -09 | UTC-09:00 -09 |  | — |
| `Pacific/Guadalcanal` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Pacific/Guam` | UTC+10:00 ChST | UTC+10:00 ChST | UTC+10:00 ChST |  | — |
| `Pacific/Honolulu` | UTC-10:00 HST | UTC-10:00 HST | UTC-10:00 HST |  | — |
| `Pacific/Johnston` | UTC-10:00 HST | UTC-10:00 HST | UTC-10:00 HST |  | — |
| `Pacific/Kanton` | UTC+13:00 +13 | UTC+13:00 +13 | UTC+13:00 +13 |  | — |
| `Pacific/Kiritimati` | UTC+14:00 +14 | UTC+14:00 +14 | UTC+14:00 +14 |  | — |
| `Pacific/Kosrae` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Pacific/Kwajalein` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Pacific/Majuro` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Pacific/Marquesas` | UTC-09:30 -0930 | UTC-09:30 -0930 | UTC-09:30 -0930 |  | — |
| `Pacific/Midway` | UTC-11:00 SST | UTC-11:00 SST | UTC-11:00 SST |  | — |
| `Pacific/Nauru` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Pacific/Niue` | UTC-11:00 -11 | UTC-11:00 -11 | UTC-11:00 -11 |  | — |
| `Pacific/Norfolk` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+11:00 +11 | yes | 2027-04-04 → UTC+11:00 (+11) |
| `Pacific/Noumea` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Pacific/Pago_Pago` | UTC-11:00 SST | UTC-11:00 SST | UTC-11:00 SST |  | — |
| `Pacific/Palau` | UTC+09:00 +09 | UTC+09:00 +09 | UTC+09:00 +09 |  | — |
| `Pacific/Pitcairn` | UTC-08:00 -08 | UTC-08:00 -08 | UTC-08:00 -08 |  | — |
| `Pacific/Pohnpei` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Pacific/Ponape` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Pacific/Port_Moresby` | UTC+10:00 +10 | UTC+10:00 +10 | UTC+10:00 +10 |  | — |
| `Pacific/Rarotonga` | UTC-10:00 -10 | UTC-10:00 -10 | UTC-10:00 -10 |  | — |
| `Pacific/Saipan` | UTC+10:00 ChST | UTC+10:00 ChST | UTC+10:00 ChST |  | — |
| `Pacific/Samoa` | UTC-11:00 SST | UTC-11:00 SST | UTC-11:00 SST |  | — |
| `Pacific/Tahiti` | UTC-10:00 -10 | UTC-10:00 -10 | UTC-10:00 -10 |  | — |
| `Pacific/Tarawa` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Pacific/Tongatapu` | UTC+13:00 +13 | UTC+13:00 +13 | UTC+13:00 +13 |  | — |
| `Pacific/Truk` | UTC+10:00 +10 | UTC+10:00 +10 | UTC+10:00 +10 |  | — |
| `Pacific/Wake` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Pacific/Wallis` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Pacific/Yap` | UTC+10:00 +10 | UTC+10:00 +10 | UTC+10:00 +10 |  | — |

## Etc

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Etc/GMT` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Etc/GMT+0` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Etc/GMT+1` | UTC-01:00 -01 | UTC-01:00 -01 | UTC-01:00 -01 |  | — |
| `Etc/GMT+10` | UTC-10:00 -10 | UTC-10:00 -10 | UTC-10:00 -10 |  | — |
| `Etc/GMT+11` | UTC-11:00 -11 | UTC-11:00 -11 | UTC-11:00 -11 |  | — |
| `Etc/GMT+12` | UTC-12:00 -12 | UTC-12:00 -12 | UTC-12:00 -12 |  | — |
| `Etc/GMT+2` | UTC-02:00 -02 | UTC-02:00 -02 | UTC-02:00 -02 |  | — |
| `Etc/GMT+3` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `Etc/GMT+4` | UTC-04:00 -04 | UTC-04:00 -04 | UTC-04:00 -04 |  | — |
| `Etc/GMT+5` | UTC-05:00 -05 | UTC-05:00 -05 | UTC-05:00 -05 |  | — |
| `Etc/GMT+6` | UTC-06:00 -06 | UTC-06:00 -06 | UTC-06:00 -06 |  | — |
| `Etc/GMT+7` | UTC-07:00 -07 | UTC-07:00 -07 | UTC-07:00 -07 |  | — |
| `Etc/GMT+8` | UTC-08:00 -08 | UTC-08:00 -08 | UTC-08:00 -08 |  | — |
| `Etc/GMT+9` | UTC-09:00 -09 | UTC-09:00 -09 | UTC-09:00 -09 |  | — |
| `Etc/GMT-0` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Etc/GMT-1` | UTC+01:00 +01 | UTC+01:00 +01 | UTC+01:00 +01 |  | — |
| `Etc/GMT-10` | UTC+10:00 +10 | UTC+10:00 +10 | UTC+10:00 +10 |  | — |
| `Etc/GMT-11` | UTC+11:00 +11 | UTC+11:00 +11 | UTC+11:00 +11 |  | — |
| `Etc/GMT-12` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Etc/GMT-13` | UTC+13:00 +13 | UTC+13:00 +13 | UTC+13:00 +13 |  | — |
| `Etc/GMT-14` | UTC+14:00 +14 | UTC+14:00 +14 | UTC+14:00 +14 |  | — |
| `Etc/GMT-2` | UTC+02:00 +02 | UTC+02:00 +02 | UTC+02:00 +02 |  | — |
| `Etc/GMT-3` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `Etc/GMT-4` | UTC+04:00 +04 | UTC+04:00 +04 | UTC+04:00 +04 |  | — |
| `Etc/GMT-5` | UTC+05:00 +05 | UTC+05:00 +05 | UTC+05:00 +05 |  | — |
| `Etc/GMT-6` | UTC+06:00 +06 | UTC+06:00 +06 | UTC+06:00 +06 |  | — |
| `Etc/GMT-7` | UTC+07:00 +07 | UTC+07:00 +07 | UTC+07:00 +07 |  | — |
| `Etc/GMT-8` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Etc/GMT-9` | UTC+09:00 +09 | UTC+09:00 +09 | UTC+09:00 +09 |  | — |
| `Etc/GMT0` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Etc/Greenwich` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Etc/UCT` | UTC+00:00 UTC | UTC+00:00 UTC | UTC+00:00 UTC |  | — |
| `Etc/UTC` | UTC+00:00 UTC | UTC+00:00 UTC | UTC+00:00 UTC |  | — |
| `Etc/Universal` | UTC+00:00 UTC | UTC+00:00 UTC | UTC+00:00 UTC |  | — |
| `Etc/Zulu` | UTC+00:00 UTC | UTC+00:00 UTC | UTC+00:00 UTC |  | — |

## Other (aliases & legacy names)

| Zone | Now | Jan | Jul | DST | Next clock change (within 1 year) |
|---|---|---|---|---|---|
| `Brazil/Acre` | UTC-05:00 -05 | UTC-05:00 -05 | UTC-05:00 -05 |  | — |
| `Brazil/DeNoronha` | UTC-02:00 -02 | UTC-02:00 -02 | UTC-02:00 -02 |  | — |
| `Brazil/East` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-03:00 -03 |  | — |
| `Brazil/West` | UTC-04:00 -04 | UTC-04:00 -04 | UTC-04:00 -04 |  | — |
| `CET` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `CST6CDT` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `Canada/Atlantic` | UTC-04:00 AST | UTC-04:00 AST | UTC-03:00 ADT | yes | 2027-03-14 → UTC-03:00 (ADT) |
| `Canada/Central` | UTC-05:00 EST | UTC-06:00 CST | UTC-05:00 CDT | yes | — |
| `Canada/Eastern` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `Canada/Mountain` | UTC-06:00 CST | UTC-07:00 MST | UTC-06:00 MDT | yes | — |
| `Canada/Newfoundland` | UTC-03:30 NST | UTC-03:30 NST | UTC-02:30 NDT | yes | 2027-03-14 → UTC-02:30 (NDT) |
| `Canada/Pacific` | UTC-07:00 MST | UTC-08:00 PST | UTC-07:00 PDT | yes | — |
| `Canada/Saskatchewan` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `Canada/Yukon` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `Chile/Continental` | UTC-03:00 -03 | UTC-03:00 -03 | UTC-04:00 -04 | yes | 2027-04-03 → UTC-04:00 (-04) |
| `Chile/EasterIsland` | UTC-05:00 -05 | UTC-05:00 -05 | UTC-06:00 -06 | yes | 2027-04-03 → UTC-06:00 (-06) |
| `Cuba` | UTC-04:00 CDT | UTC-05:00 CST | UTC-04:00 CDT | yes | — |
| `EET` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-03-28 → UTC+03:00 (EEST) |
| `EST` | UTC-05:00 EST | UTC-05:00 EST | UTC-05:00 EST |  | — |
| `EST5EDT` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `Egypt` | UTC+02:00 EET | UTC+02:00 EET | UTC+03:00 EEST | yes | 2027-04-30 → UTC+03:00 (EEST) |
| `Eire` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+01:00 IST | yes | 2027-03-28 → UTC+01:00 (IST) |
| `GB` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+01:00 BST | yes | 2027-03-28 → UTC+01:00 (BST) |
| `GB-Eire` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+01:00 BST | yes | 2027-03-28 → UTC+01:00 (BST) |
| `GMT` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `GMT+0` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `GMT-0` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `GMT0` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Greenwich` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `HST` | UTC-10:00 HST | UTC-10:00 HST | UTC-10:00 HST |  | — |
| `Hongkong` | UTC+08:00 HKT | UTC+08:00 HKT | UTC+08:00 HKT |  | — |
| `Iceland` | UTC+00:00 GMT | UTC+00:00 GMT | UTC+00:00 GMT |  | — |
| `Iran` | UTC+03:30 +0330 | UTC+03:30 +0330 | UTC+03:30 +0330 |  | — |
| `Israel` | UTC+02:00 IST | UTC+02:00 IST | UTC+03:00 IDT | yes | 2027-03-26 → UTC+03:00 (IDT) |
| `Jamaica` | UTC-05:00 EST | UTC-05:00 EST | UTC-05:00 EST |  | — |
| `Japan` | UTC+09:00 JST | UTC+09:00 JST | UTC+09:00 JST |  | — |
| `Kwajalein` | UTC+12:00 +12 | UTC+12:00 +12 | UTC+12:00 +12 |  | — |
| `Libya` | UTC+02:00 EET | UTC+02:00 EET | UTC+02:00 EET |  | — |
| `MET` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `MST` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `MST7MDT` | UTC-07:00 MST | UTC-07:00 MST | UTC-06:00 MDT | yes | 2027-03-14 → UTC-06:00 (MDT) |
| `Mexico/BajaNorte` | UTC-08:00 PST | UTC-08:00 PST | UTC-07:00 PDT | yes | 2027-03-14 → UTC-07:00 (PDT) |
| `Mexico/BajaSur` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `Mexico/General` | UTC-06:00 CST | UTC-06:00 CST | UTC-06:00 CST |  | — |
| `NZ` | UTC+13:00 NZDT | UTC+13:00 NZDT | UTC+12:00 NZST | yes | 2027-04-04 → UTC+12:00 (NZST) |
| `NZ-CHAT` | UTC+13:45 +1345 | UTC+13:45 +1345 | UTC+12:45 +1245 | yes | 2027-04-04 → UTC+12:45 (+1245) |
| `Navajo` | UTC-07:00 MST | UTC-07:00 MST | UTC-06:00 MDT | yes | 2027-03-14 → UTC-06:00 (MDT) |
| `PRC` | UTC+08:00 CST | UTC+08:00 CST | UTC+08:00 CST |  | — |
| `PST8PDT` | UTC-08:00 PST | UTC-08:00 PST | UTC-07:00 PDT | yes | 2027-03-14 → UTC-07:00 (PDT) |
| `Poland` | UTC+01:00 CET | UTC+01:00 CET | UTC+02:00 CEST | yes | 2027-03-28 → UTC+02:00 (CEST) |
| `Portugal` | UTC+00:00 WET | UTC+00:00 WET | UTC+01:00 WEST | yes | 2027-03-28 → UTC+01:00 (WEST) |
| `ROC` | UTC+08:00 CST | UTC+08:00 CST | UTC+08:00 CST |  | — |
| `ROK` | UTC+09:00 KST | UTC+09:00 KST | UTC+09:00 KST |  | — |
| `Singapore` | UTC+08:00 +08 | UTC+08:00 +08 | UTC+08:00 +08 |  | — |
| `Turkey` | UTC+03:00 +03 | UTC+03:00 +03 | UTC+03:00 +03 |  | — |
| `UCT` | UTC+00:00 UTC | UTC+00:00 UTC | UTC+00:00 UTC |  | — |
| `US/Alaska` | UTC-09:00 AKST | UTC-09:00 AKST | UTC-08:00 AKDT | yes | 2027-03-14 → UTC-08:00 (AKDT) |
| `US/Aleutian` | UTC-10:00 HST | UTC-10:00 HST | UTC-09:00 HDT | yes | 2027-03-14 → UTC-09:00 (HDT) |
| `US/Arizona` | UTC-07:00 MST | UTC-07:00 MST | UTC-07:00 MST |  | — |
| `US/Central` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `US/East-Indiana` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `US/Eastern` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `US/Hawaii` | UTC-10:00 HST | UTC-10:00 HST | UTC-10:00 HST |  | — |
| `US/Indiana-Starke` | UTC-06:00 CST | UTC-06:00 CST | UTC-05:00 CDT | yes | 2027-03-14 → UTC-05:00 (CDT) |
| `US/Michigan` | UTC-05:00 EST | UTC-05:00 EST | UTC-04:00 EDT | yes | 2027-03-14 → UTC-04:00 (EDT) |
| `US/Mountain` | UTC-07:00 MST | UTC-07:00 MST | UTC-06:00 MDT | yes | 2027-03-14 → UTC-06:00 (MDT) |
| `US/Pacific` | UTC-08:00 PST | UTC-08:00 PST | UTC-07:00 PDT | yes | 2027-03-14 → UTC-07:00 (PDT) |
| `US/Samoa` | UTC-11:00 SST | UTC-11:00 SST | UTC-11:00 SST |  | — |
| `UTC` | UTC+00:00 UTC | UTC+00:00 UTC | UTC+00:00 UTC |  | — |
| `Universal` | UTC+00:00 UTC | UTC+00:00 UTC | UTC+00:00 UTC |  | — |
| `W-SU` | UTC+03:00 MSK | UTC+03:00 MSK | UTC+03:00 MSK |  | — |
| `WET` | UTC+00:00 WET | UTC+00:00 WET | UTC+01:00 WEST | yes | 2027-03-28 → UTC+01:00 (WEST) |
| `Zulu` | UTC+00:00 UTC | UTC+00:00 UTC | UTC+00:00 UTC |  | — |
