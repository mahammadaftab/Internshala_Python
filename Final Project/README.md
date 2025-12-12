# Fantasy Cricket Game

A Python application for creating and managing fantasy cricket teams with scoring based on real player performance.

## Project Overview

This project implements a Fantasy Cricket game where users can:
- Create and manage cricket teams within a point budget
- Select players from different categories (Batsmen, Bowlers, All-rounders, Wicket-keepers)
- Evaluate team performance based on real match data
- Save and load teams

## Features

- **Team Management**: Create, save, and load fantasy cricket teams
- **Player Selection**: Choose players from different categories with point constraints
- **Scoring System**: Calculate team scores based on real player performance
- **Database Integration**: SQLite database for storing player stats and teams
- **GUI Interface**: User-friendly interface built with PyQt5

## Project Structure

```
Final Project/
├── DATABASE_DESIGN.md          # Database schema documentation
├── README.md                   # This file
├── fantasy_cricket.db          # SQLite database (created on first run)
├── fantasy_cricket.py          # Main application
├── fantasy_cricket.ui          # GUI design file
├── fantasy_cricket_ui.py       # Generated GUI code
├── scoring_rules.py            # Scoring calculation logic
├── setup_database.py           # Database creation and initialization
└── test_functionality.py       # Test script
```

## Requirements

- Python 3.x
- PyQt5
- SQLite3 (usually included with Python)

## Installation

1. Install the required packages:
   ```
   pip install PyQt5
   ```

2. Run the database setup script (optional, as it will be created automatically):
   ```
   python setup_database.py
   ```

## Usage

Run the main application:
```
python fantasy_cricket.py
```

### Creating a Team

1. Click "Manage Teams" → "New Team" to create a new team
2. Enter a team name
3. Select players from different categories by double-clicking on them
4. Ensure your team follows the constraints:
   - 11 players total
   - 2-5 Batsmen
   - 2-5 Bowlers
   - 1-3 All-rounders
   - 1 Wicket-keeper
5. Save your team using "Manage Teams" → "Save Team"

### Evaluating a Team

1. Open a saved team using "Manage Teams" → "Open Team"
2. Click "Manage Teams" → "Evaluate Team" to calculate the team's score

## Scoring Rules

### Batting
- 1 point for every 2 runs scored
- Additional 5 points for half-century (50+ runs)
- Additional 10 points for century (100+ runs)
- 2 points for strike rate between 80-100
- Additional 4 points for strike rate above 100
- 1 point for each four
- 2 points for each six

### Bowling
- 10 points for each wicket
- Additional 5 points for 3+ wickets in an innings
- Additional 10 points for 5+ wickets in an innings
- 4 points for economy rate between 3.5-4.5
- 7 points for economy rate between 2-3.5
- 10 points for economy rate below 2

### Fielding
- 10 points for each catch
- 10 points for each stumping
- 10 points for each run-out

## Database Schema

The application uses three tables:

### match
Stores player performance data for matches:
- Player (TEXT, PRIMARY KEY)
- Scored (INTEGER)
- Faced (INTEGER)
- Fours (INTEGER)
- Sixes (INTEGER)
- Bowled (INTEGER)
- Maiden (INTEGER)
- Given (INTEGER)
- Wkts (INTEGER)
- Catches (INTEGER)
- Stumping (INTEGER)
- RO (INTEGER)

### stats
Stores player statistics:
- player (TEXT, PRIMARY KEY)
- matches (INTEGER)
- runs (INTEGER)
- 100s (INTEGER)
- 50s (INTEGER)
- value (INTEGER)
- ctg (TEXT)

### teams
Stores fantasy cricket teams:
- name (TEXT, PRIMARY KEY)
- players (TEXT)
- value (INTEGER)

## Testing

Run the test suite to verify functionality:
```
python test_functionality.py
```

## License

This project is for educational purposes as part of the Internshala Python Training program.