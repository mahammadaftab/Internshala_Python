# Assignment 5 — PyQt5 Bookstore GUI Application

A fully functional PyQt5 GUI application for managing bookstore book searches and purchase calculations with SQLite database backend.

---

## Files Included

| File | Purpose |
|------|---------|
| **bookstore_gui.py** | Main PyQt5 application with event handlers and GUI logic |
| **bookstore_gui.ui** | Qt Designer UI file (XML format) |
| **setup_database.py** | Database initialization script |
| **test_gui_logic.py** | Logic tests for verification (non-GUI) |
| **bookstore.db** | SQLite database with book data |

---

## Features Implemented

✓ **GUI Form with PyQt5 widgets**
  - QLineEdit for book title input
  - QLineEdit (read-only) for price display
  - QSpinBox for quantity (integer-only input, range 1-999)
  - QLineEdit (read-only) for total display
  - Push buttons: Find Price, Find Total Amount, Clear

✓ **Database Integration**
  - SQLite database with books table (id, title, author, price)
  - SELECT query to fetch book price by title
  - Case-insensitive title matching

✓ **Button Event Handlers**
  - **Find Price**: Queries database, displays price or error if book not found
  - **Find Total Amount**: Calculates price × quantity
  - **Clear**: Resets all fields to empty/default values

✓ **Input Validation**
  - Book title must not be empty
  - Quantity only accepts integers (via QSpinBox)
  - Quantity range: 1-999

✓ **Error Handling**
  - Display error message if book title not found in database
  - Validate inputs before processing
  - Clear message label on successful operations

✓ **Layout and Design**
  - QVBoxLayout for main structure
  - QFormLayout for organized form fields
  - QGroupBox for grouping related fields
  - QHBoxLayout for button row with spacer
  - Styled buttons with colors
  - Professional styling and fonts

---

## Database Schema

```sql
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL
)
```

### Sample Data

| ID | Title | Author | Price |
|----|-------|--------|-------|
| 1 | Think Python | Allen B. Downey | 475.00 |
| 2 | Python Crash Course | Eric Matthes | 599.99 |
| 3 | Fluent Python | Luciano Ramalho | 799.50 |
| 4 | Learning Python | Mark Lutz | 850.00 |
| 5 | Automate the Boring Stuff with Python | Al Sweigart | 525.00 |
| 6 | Python for Data Analysis | Wes McKinney | 650.00 |
| 7 | Effective Python | Brett Slatkin | 725.00 |
| 8 | Clean Code | Robert C. Martin | 695.00 |

---

## How to Use

### 1. Setup Database (First time only)

```powershell
cd "Assignments\assignment 5"
python setup_database.py
```

### 2. Run GUI Application

```powershell
python bookstore_gui.py
```

### 3. GUI Workflow

1. **Enter Book Title**: Type the title of a book (e.g., "Think Python")
2. **Click "Find Price"**: The application queries the database and displays the price
3. **Set Quantity**: Use the spin box to select desired quantity (1-999)
4. **Click "Find Total Amount"**: Calculates and displays price × quantity
5. **Clear**: Click to reset all fields

### 4. Example Scenario

```
Book Title: Think Python
Click "Find Price" → Price: 475.00
Quantity: 2
Click "Find Total Amount" → Total Amount: 950.00
```

---

## Logic Tests Output

```
==================================================
BOOKSTORE GUI LOGIC TESTS
==================================================

Test 1: Finding book price
--------------------------------------------------
✓ Think Python: Rs.475.00
✓ Python Crash Course: Rs.599.99
✗ Unknown Book: Not found

Test 2: Calculate total amount
--------------------------------------------------
✓ Think Python × 2 = Rs.950.00
✓ Python Crash Course × 3 = Rs.1799.97
✓ Fluent Python × 1 = Rs.799.50

Test 3: Quantity validation (QSpinBox accepts only integers)
--------------------------------------------------
✓ Quantity 1 is valid (integer)
✓ Quantity 5 is valid (integer)
✓ Quantity 10 is valid (integer)
✓ Quantity 100 is valid (integer)
✓ Quantity 999 is valid (integer)
✗ Quantity 0 is invalid (below minimum)
✗ Quantity 1000 is invalid (above maximum)

==================================================
All tests completed!
==================================================
```

---

## Key PyQt5 Concepts Implemented

| Concept | Implementation |
|---------|-----------------|
| **Main Window** | QMainWindow with central widget |
| **Layouts** | QVBoxLayout, QHBoxLayout, QFormLayout |
| **Widgets** | QLineEdit, QPushButton, QSpinBox, QLabel, QGroupBox |
| **Properties** | Read-only fields, placeholders, ranges, styles |
| **Event Handlers** | clicked.connect() for button events |
| **Database Query** | sqlite3.execute() with parameterized queries |
| **Input Validation** | Empty string checks, quantity range validation |
| **UI File** | bookstore_gui.ui (XML format from Qt Designer) |
| **Styling** | Stylesheet for colors, fonts, padding, borders |
| **Layouts & Spacers** | Professional UI spacing and alignment |

---

## Requirements Met

✓ Fully functional PyQt5 GUI application  
✓ One script file with all application code (bookstore_gui.py)  
✓ One .ui file created (bookstore_gui.ui)  
✓ SQLite database file with books table (bookstore.db)  
✓ Find price functionality with database query  
✓ Integer-only quantity input via QSpinBox  
✓ Calculate total amount (price × quantity)  
✓ Error handling for book not found  
✓ Layout design with spacers and grouping  
✓ Professional styling with colors and fonts  
✓ Event handlers connected to button clicks  

---

## Dependencies

- **PyQt5** (for GUI)
- **sqlite3** (built-in, for database)
- **Python 3.7+**

### Install PyQt5

```powershell
pip install PyQt5
```

---

## Notes

- The quantity input uses **QSpinBox** which automatically restricts input to integers only
- Book title search is **case-insensitive** (using LOWER() in SQL)
- All prices displayed in **Indian Rupees (Rs.)**
- The GUI form auto-creates database on first run if not present
- All field validations are implemented with error messages
- Professional UI styling with color-coded buttons
