# Assignment 5 — PyQt5 Bookstore GUI Application

## Quick Start

### 1. Install PyQt5 (if not already installed)
```powershell
pip install PyQt5
```

### 2. Run the application
```powershell
cd "Assignments\assignment 5"
python bookstore_gui.py
```

The GUI window will open with the bookstore form.

## How to Use the Application

1. **Enter Book Title**: Type a book title from the database (e.g., "Think Python")
2. **Click "Find Price"**: The app fetches the price from the database
3. **Set Quantity**: Use the spinner to select quantity (1-999)
4. **Click "Find Total Amount"**: Calculates price × quantity
5. **View Results**: Total amount is displayed in the "Total Amount" field
6. **Clear**: Click to reset all fields and start over

## Features

- ✓ PyQt5 GUI with professional styling
- ✓ SQLite database integration
- ✓ Integer-only quantity input (QSpinBox)
- ✓ Error handling (book not found, invalid input)
- ✓ Qt Designer .ui file
- ✓ Layout design with spacers
- ✓ Event handlers for all buttons

## Files

- `bookstore_gui.py` — Main application
- `bookstore_gui.ui` — UI file (Qt Designer format)
- `setup_database.py` — Database setup script
- `bookstore.db` — SQLite database
- `test_gui_logic.py` — Logic tests (non-GUI)
- `OUTPUT.md` — Complete documentation

## Test Without GUI

To test the logic without running the GUI:
```powershell
python test_gui_logic.py
```

This will verify database queries and calculations work correctly.
