# Cricket Player Statistics Data Structure - Assignment 1

## Problem Statement
Design a data structure to display individual player stats for cricket players. A player may have represented more than one team and may have played in more than one format (Test, ODI, and T20).

---

## Data Fields and Python Data Types

### 1. Personal Information Fields

| Field Name | Python Data Type | Description | Example |
|------------|-----------------|-------------|---------|
| player_id | `int` | Unique identifier for the player | 1001 |
| first_name | `str` | Player's first name | "Virat" |
| last_name | `str` | Player's last name | "Kohli" |
| date_of_birth | `date` | Player's date of birth | date(1988, 11, 5) |
| nationality | `str` | Player's country/nationality | "India" |

### 2. Physical Attributes Fields

| Field Name | Python Data Type | Description | Example |
|------------|-----------------|-------------|---------|
| height_cm | `float` | Height in centimeters | 175.5 |
| batting_hand | `str` | Dominant batting hand | "Right" / "Left" |
| bowling_hand | `str` | Dominant bowling hand | "Right" / "Left" |

### 3. Career Information Fields

| Field Name | Python Data Type | Description | Example |
|------------|-----------------|-------------|---------|
| career_start_year | `int` | Year when international career started | 2008 |
| career_end_year | `int` | Year of retirement (0 if still active) | 0 |
| primary_role | `str` | Primary role in cricket | "Batsman" / "Bowler" / "All-rounder" / "Wicket-keeper" |
| is_active | `bool` | Whether player is currently active | True |

### 4. Team History Fields

| Field Name | Python Data Type | Description | Example |
|------------|-----------------|-------------|---------|
| teams_represented | `List[TeamRecord]` | List of teams player has represented | [{team1}, {team2}] |
| team_name | `str` | Name of the team | "India" / "Mumbai Indians" |
| joining_date | `date` | Date when joined the team | date(2008, 8, 19) |
| departure_date | `date` | Date when left the team (None if current) | None |
| role | `str` | Player's role in specific team | "Batsman" / "Bowler" |
| jersey_number | `int` | Jersey number with the team | 18 |
| matches_for_team | `int` | Total matches played for that team | 250 |

### 5. Format-wise Statistics Fields

| Field Name | Python Data Type | Description | Example |
|------------|-----------------|-------------|---------|
| test_stats | `FormatStats` | Complete statistics for Test format | {stats_object} |
| odi_stats | `FormatStats` | Complete statistics for ODI format | {stats_object} |
| t20_stats | `FormatStats` | Complete statistics for T20 format | {stats_object} |
| format_name | `str` | Name of cricket format | "Test" / "ODI" / "T20" |
| matches_played | `int` | Number of matches in format | 99 |
| runs_scored | `int` | Total runs scored in format | 8200 |
| wickets_taken | `int` | Total wickets taken in format | 25 |
| batting_average | `float` | Average runs per match | 50.61 |
| bowling_average | `float` | Average runs per wicket | 32.45 |
| strike_rate | `float` | Runs per 100 balls | 58.45 |
| highest_score | `int` | Highest individual score | 254 |
| best_bowling | `str` | Best bowling figures | "5/32" |

### 6. Achievement and Aggregate Fields

| Field Name | Python Data Type | Description | Example |
|------------|-----------------|-------------|---------|
| international_caps | `int` | Total international matches played | 498 |
| century_count | `int` | Total centuries (100+ runs) | 48 |
| half_century_count | `int` | Total half-centuries (50+ runs) | 67 |
| man_of_the_match_awards | `int` | Total Player of Match awards | 42 |

---

## Data Structure Design (Nested Objects)

### CricketPlayer (Main Object)
```
CricketPlayer
├── Personal Info (str, int, date)
├── Physical Attributes (float, str)
├── Career Info (int, str, bool)
├── Teams (List[TeamRecord])
│   └── TeamRecord
│       ├── team_name (str)
│       ├── dates (date, date)
│       ├── role (str)
│       ├── jersey_number (int)
│       └── matches_for_team (int)
├── Format Statistics (FormatStats × 3)
│   └── FormatStats
│       ├── format_name (str)
│       ├── matches_played (int)
│       ├── runs_scored (int)
│       ├── wickets_taken (int)
│       ├── batting_average (float)
│       ├── bowling_average (float)
│       ├── strike_rate (float)
│       ├── highest_score (int)
│       └── best_bowling (str)
└── Achievements (int × 4)
```

---

## Rationale for Data Types

1. **`int`**: Used for countable metrics like matches, runs, wickets, jersey numbers, years, and awards
2. **`str`**: Used for names, nationalities, roles, team names, and other textual information
3. **`float`**: Used for averages, strike rates, and physical measurements (height) where decimal precision is needed
4. **`date`**: Used for dates of birth and career milestones for proper date handling and calculations
5. **`bool`**: Used for binary states like active/inactive status
6. **`List[...]`**: Used to represent multiple teams a player has represented
7. **`Dataclass`**: Used to create structured, reusable objects with type hints and automatic `__init__` method

---

## Advantages of This Design

1. **Scalability**: Can easily add new fields or teams
2. **Type Safety**: Python type hints enable IDE support and error detection
3. **Organization**: Related data is grouped into logical structures
4. **Reusability**: FormatStats and TeamRecord can be used for multiple players
5. **Flexibility**: Supports multiple formats and teams for each player
6. **Extensibility**: Can be extended with methods for calculations and comparisons
7. **Data Integrity**: Dataclasses provide automatic validation support

---

## Usage Example

```python
# Create a player instance
player = CricketPlayer(
    player_id=1001,
    first_name="Virat",
    last_name="Kohli",
    # ... other fields ...
    teams_represented=[
        TeamRecord("India", date(2008, 8, 19), None, "Batsman", 18, 250),
        TeamRecord("RCB", date(2008, 4, 18), None, "Batsman", 18, 180)
    ],
    # ... format stats ...
)

# Access nested data
print(player.first_name)  # "Virat"
print(player.teams_represented[0].team_name)  # "India"
print(player.test_stats.highest_score)  # 254
```

---

**Assignment Completed**: This design structure comprehensively covers individual player statistics, supporting multiple teams and formats as required.
