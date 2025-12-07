# Cricket Player Statistics - Data Fields Summary Table

## Quick Reference: All Data Fields with Types

| # | Field Name | Data Type | Category | Purpose |
|----|-----------|-----------|----------|---------|
| 1 | player_id | `int` | Personal | Unique identifier |
| 2 | first_name | `str` | Personal | Player's first name |
| 3 | last_name | `str` | Personal | Player's last name |
| 4 | date_of_birth | `date` | Personal | Birth date for age calculation |
| 5 | nationality | `str` | Personal | Country representation |
| 6 | height_cm | `float` | Physical | Height measurement |
| 7 | batting_hand | `str` | Physical | Dominant batting hand |
| 8 | bowling_hand | `str` | Physical | Dominant bowling hand |
| 9 | career_start_year | `int` | Career | International debut year |
| 10 | career_end_year | `int` | Career | Retirement year (0 if active) |
| 11 | primary_role | `str` | Career | Main playing role |
| 12 | is_active | `bool` | Career | Current active status |
| 13 | teams_represented | `List[TeamRecord]` | Teams | All teams represented |
| 14 | team_name | `str` | Team Details | Name of specific team |
| 15 | joining_date | `date` | Team Details | Date joined team |
| 16 | departure_date | `date` | Team Details | Date left team |
| 17 | team_role | `str` | Team Details | Role in specific team |
| 18 | jersey_number | `int` | Team Details | Jersey number |
| 19 | matches_for_team | `int` | Team Details | Matches played for team |
| 20 | test_stats | `FormatStats` | Format Stats | Test cricket statistics |
| 21 | odi_stats | `FormatStats` | Format Stats | ODI cricket statistics |
| 22 | t20_stats | `FormatStats` | Format Stats | T20 cricket statistics |
| 23 | format_name | `str` | Format Details | Format name (Test/ODI/T20) |
| 24 | matches_played | `int` | Format Details | Matches in format |
| 25 | runs_scored | `int` | Format Details | Total runs in format |
| 26 | wickets_taken | `int` | Format Details | Total wickets in format |
| 27 | batting_average | `float` | Format Details | Average runs per match |
| 28 | bowling_average | `float` | Format Details | Average runs per wicket |
| 29 | strike_rate | `float` | Format Details | Runs per 100 balls |
| 30 | highest_score | `int` | Format Details | Highest individual score |
| 31 | best_bowling | `str` | Format Details | Best bowling figures |
| 32 | international_caps | `int` | Achievements | Total international matches |
| 33 | century_count | `int` | Achievements | Total centuries |
| 34 | half_century_count | `int` | Achievements | Total half-centuries |
| 35 | man_of_the_match_awards | `int` | Achievements | Total MOTM awards |

## Python Data Types Used

| Type | Count | Usage |
|------|-------|-------|
| `int` | 15 | Counters, years, numbers, IDs |
| `str` | 8 | Names, roles, team names, formats |
| `float` | 4 | Averages, strike rates, physical measurements |
| `date` | 4 | Dates of birth and career milestones |
| `bool` | 1 | Active/inactive status |
| `List[T]` | 1 | Collection of teams |
| Custom Classes | 2 | FormatStats, TeamRecord |

**Total Fields**: 35
**Primary Data Types**: 7

## Implementation Features

✓ Supports multiple teams representation
✓ Tracks statistics across 3 cricket formats
✓ Comprehensive personal and career information
✓ Date-based timeline tracking
✓ Achievement and performance metrics
✓ Type-safe with Python dataclasses
✓ Extensible structure for additional fields
