# Internshala Python Course

A comprehensive Python learning repository for the Internshala Python course, containing assignments and practical implementations.

## 📁 Project Structure

```
Internshala_Python/
├── README.md
├── Assignments/
│   ├── assignment 1/
│   │   ├── cricket_player_stats.py
│   │   ├── ASSIGNMENT_DOCUMENTATION.md
│   │   └── DATA_FIELDS_QUICK_REFERENCE.md
│   ├── assignment 2/
│   │   ├── assignment2_main.py
│   │   ├── match_points.py
│   │   └── OUTPUT.md
│   ├── assignment 3/
│   │   ├── assignment3_main.py
│   │   ├── books.py
│   │   └── OUTPUT.md
│   ├── assignment 4/
│   │   ├── create_db.py
│   │   ├── bookstore.py
│   │   ├── test_bookstore.py
│   │   └── OUTPUT.md
│   └── assignment 5/
│       ├── bookstore_gui.py
│       ├── bookstore_gui.ui
│       ├── setup_database.py
│       └── OUTPUT.md
└── Final Project/
    ├── DATABASE_DESIGN.md
    ├── fantasy_cricket.py
    ├── fantasy_cricket.ui
    ├── fantasy_cricket_ui.py
    ├── scoring_rules.py
    ├── setup_database.py
    └── test_functionality.py
```

## 🎯 Assignments

### Assignment 1: Cricket Player Statistics Data Structure

**Objective**: Design a data structure to display individual player statistics for cricket players who may have represented multiple teams and played in different formats.

**Key Features**:
- ✅ Support for multiple teams representation
- ✅ Statistics across 3 cricket formats (Test, ODI, T20)
- ✅ Comprehensive personal and career information
- ✅ Type-safe Python implementation with dataclasses

**Files**:
- `cricket_player_stats.py` - Full Python implementation with sample data
- `ASSIGNMENT_DOCUMENTATION.md` - Detailed documentation with all 35 data fields and their types
- `DATA_FIELDS_QUICK_REFERENCE.md` - Quick reference summary table

**Data Structure Overview**:
- **CricketPlayer** - Main dataclass containing all player information
- **FormatStats** - Nested dataclass for Test/ODI/T20 statistics
- **TeamRecord** - Nested dataclass for team history tracking

**Data Fields Summary**:
| Category | Count | Examples |
|----------|-------|----------|
| Personal Information | 5 | player_id, first_name, date_of_birth, nationality |
| Physical Attributes | 3 | height_cm, batting_hand, bowling_hand |
| Career Information | 4 | career_start_year, primary_role, is_active |
| Team History | 7 | teams_represented, team_name, joining_date, jersey_number |
| Format Statistics | 24 | matches_played, runs_scored, batting_average, strike_rate |
| Achievements | 4 | international_caps, century_count, man_of_the_match_awards |

**Total**: 47 comprehensive data fields across 6 categories

**Python Data Types Used**:
- `int` - For counters, years, and numerical IDs
- `str` - For names, roles, and text information
- `float` - For averages and percentages
- `date` - For date tracking
- `bool` - For status indicators
- `List[T]` - For collections (teams)
- Custom Classes - FormatStats, TeamRecord

### Running the Assignment

```powershell
cd "Assignments\assignment 1"
python cricket_player_stats.py
```

This will display:
- Complete cricket player profile with sample data (Virat Kohli)
- Test, ODI, and T20 statistics
- Team history and representation
- Achievement metrics

### Assignment 2: Match Points Calculation

**Objective**: Calculate points for players based on their performance in a match to determine the Man of the Match.

**Key Features**:
- ✅ Batting point calculation based on runs scored
- ✅ Bowling point calculation based on wickets taken
- ✅ Fielding point calculation for catches, stumpings, and run-outs
- ✅ Man of the Match determination based on highest points

**Files**:
- `assignment2_main.py` - Main script to calculate and display points
- `match_points.py` - Core logic for point calculations
- `OUTPUT.md` - Sample output and results

**Point Calculation Rules**:
- **Batting**: Points based on runs scored with bonuses for boundaries and milestones
- **Bowling**: Points based on wickets taken with bonuses for multiple wickets
- **Fielding**: Fixed points for catches, stumpings, and run-outs

### Running the Assignment

```powershell
cd "Assignments\assignment 2"
python assignment2_main.py
```

### Assignment 3: Book & EBook Royalty Calculation

**Objective**: Calculate royalties for authors based on book sales with different schemes for physical books and eBooks.

**Key Features**:
- ✅ Tiered royalty calculation for physical books
- ✅ EBook royalty calculation with GST deduction
- ✅ Object-oriented design with inheritance
- ✅ Price update functionality

**Files**:
- `assignment3_main.py` - Main script to demonstrate royalty calculations
- `books.py` - Class definitions for Book and EBook
- `OUTPUT.md` - Sample output and results

**Royalty Structure**:
- **Physical Books**: 
  - 10% on first 500 copies
  - 12.5% on next 1,000 copies
  - 15% on further copies
- **EBooks**: Same tiers minus 12% GST

### Running the Assignment

```powershell
cd "Assignments\assignment 3"
python assignment3_main.py
```

### Assignment 4: Bookstore Database Application

**Objective**: Create a SQLite database application for managing bookstore inventory and calculating purchase totals.

**Key Features**:
- ✅ SQLite database creation and population
- ✅ Interactive bookstore application with user input
- ✅ Database queries for book information
- ✅ Purchase total calculation

**Files**:
- `create_db.py` - Script to create and populate the database
- `bookstore.py` - Interactive bookstore application
- `test_bookstore.py` - Non-interactive test script
- `OUTPUT.md` - Sample output and results

**Database Schema**:
```sql
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL
)
```

### Running the Assignment

1. Setup Database (first time only):
   ```powershell
   cd "Assignments\assignment 4"
   python create_db.py
   ```

2. Run Interactive Application:
   ```powershell
   python bookstore.py
   ```

3. Test Without User Input:
   ```powershell
   python test_bookstore.py
   ```

### Assignment 5: PyQt5 Bookstore GUI Application

**Objective**: Create a fully functional PyQt5 GUI application for managing bookstore book searches and purchase calculations with SQLite database backend.

**Key Features**:
- ✅ PyQt5 GUI with form layout
- ✅ Database integration with SQLite
- ✅ Button event handlers for price lookup and total calculation
- ✅ Input validation and error handling
- ✅ Professional UI design

**Files**:
- `bookstore_gui.py` - Main PyQt5 application with event handlers
- `bookstore_gui.ui` - Qt Designer UI file
- `setup_database.py` - Database initialization script
- `OUTPUT.md` - Sample output and results

**GUI Components**:
- QLineEdit for book title input
- QLineEdit (read-only) for price display
- QSpinBox for quantity input
- QLineEdit (read-only) for total display
- Push buttons: Find Price, Find Total Amount, Clear

### Running the Assignment

1. Setup Database (first time only):
   ```powershell
   cd "Assignments\assignment 5"
   python setup_database.py
   ```

2. Run GUI Application:
   ```powershell
   python bookstore_gui.py
   ```

## 🏆 Final Project: Fantasy Cricket Game

**Objective**: Create a complete Fantasy Cricket game application with team management, player selection, and scoring based on real performance.

**Key Features**:
- ✅ Database design with match, stats, and teams tables
- ✅ PyQt5 GUI with player categorization
- ✅ Team management (create, save, load)
- ✅ Player selection with point budget constraints
- ✅ Comprehensive scoring system based on real performance
- ✅ Error handling and validation

**Files**:
- `fantasy_cricket.py` - Main application
- `fantasy_cricket.ui` - GUI design file
- `fantasy_cricket_ui.py` - Generated GUI code
- `scoring_rules.py` - Scoring calculation logic
- `setup_database.py` - Database creation and initialization
- `DATABASE_DESIGN.md` - Database schema documentation

**Game Rules**:
- 11-player teams with category constraints
- 1000-point budget for player selection
- Scoring based on batting, bowling, and fielding performance
- Team evaluation against real match data

### Running the Final Project

1. Install dependencies:
   ```powershell
   pip install PyQt5
   ```

2. Run the application:
   ```powershell
   cd "Final Project"
   python fantasy_cricket.py
   ```

## 🔧 Technologies Used

- **Python 3.x**
- **PyQt5** - For GUI applications
- **SQLite3** - For database management
- **Type Hints** - For type safety
- **Dataclasses** - For structured data organization
- **datetime.date** - For date handling

## 📚 Course Content

This repository demonstrates:
1. Data structure design and planning
2. Python dataclasses and type hints
3. Object-oriented programming concepts
4. Database integration with SQLite
5. GUI development with PyQt5
6. Error handling and validation
7. Real-world problem modeling
8. Best practices for code organization

## 🚀 Getting Started

1. Clone or download the repository
2. Navigate to the assignment or project folder
3. Run the Python scripts to see the implementations in action
4. Review the documentation for detailed explanations

## 📝 Notes

All assignments follow Python best practices including:
- Type hints for better IDE support
- Docstrings for documentation
- Clear variable naming conventions
- Modular and scalable design