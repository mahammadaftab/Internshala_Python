# Internshala Python Course

A comprehensive Python learning repository for the Internshala Python course, containing assignments and practical implementations.

## 📁 Project Structure

```
Internshala_Python/
├── README.md
└── Assignments/
    └── assignment 1/
        ├── cricket_player_stats.py
        ├── ASSIGNMENT_DOCUMENTATION.md
        └── DATA_FIELDS_QUICK_REFERENCE.md
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

## 🔧 Technologies Used

- **Python 3.x**
- **Type Hints** - For type safety
- **Dataclasses** - For structured data organization
- **datetime.date** - For date handling

## 📚 Course Content

This repository demonstrates:
1. Data structure design and planning
2. Python dataclasses and type hints
3. Organizing complex nested data
4. Real-world problem modeling
5. Best practices for code organization

## 🚀 Getting Started

1. Clone or download the repository
2. Navigate to the assignment folder
3. Run the Python scripts to see the data structures in action
4. Review the documentation for detailed explanations

## 📝 Notes

All assignments follow Python best practices including:
- Type hints for better IDE support
- Docstrings for documentation
- Clear variable naming conventions
- Modular and scalable design