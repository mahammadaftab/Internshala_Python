# Assignment 4 — Bookstore Database Application Output

SQLite database application for managing bookstore inventory and calculating purchase totals.

## Files Included

1. **create_db.py** — Creates and populates the SQLite database
2. **bookstore.py** — Interactive bookstore application (user-input driven)
3. **test_bookstore.py** — Non-interactive test script demonstrating functionality
4. **bookstore.db** — SQLite database file (created at runtime)

---

## Part 1: Database Creation

### Command
```powershell
cd "Assignments\assignment 4"
python create_db.py
```

### Output
```
Creating database: bookstore.db
✓ Table 'books' created successfully.
✓ Inserted 8 books into the database.

Books in database:
ID    Title                                    Author                    Price     
--------------------------------------------------------------------------------
1     Think Python                             Allen B. Downey           Rs.475.00    
2     Python Crash Course                      Eric Matthes              Rs.599.99    
3     Fluent Python                            Luciano Ramalho           Rs.799.50    
4     Learning Python                          Mark Lutz                 Rs.850.00    
5     Automate the Boring Stuff with Python    Al Sweigart               Rs.525.00    
6     Python for Data Analysis                 Wes McKinney              Rs.650.00
7     Effective Python                         Brett Slatkin             Rs.725.00
8     Clean Code                               Robert C. Martin          Rs.695.00

✓ Database setup complete: bookstore.db
```

### Database Schema

```sql
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    price REAL NOT NULL
)
```

---

## Part 2: Interactive Bookstore Query

### Command
```powershell
python bookstore.py
```

### Features
- Displays all available books in the database
- Accepts user input for book title and quantity
- Executes SELECT query to fetch price from database
- Calculates and displays total amount
- Loops until user enters 'quit'

### Sample User Interaction
```
============================================================
Welcome to the Bookstore!
============================================================

Available Books:
...
---

Enter book title (or 'quit' to exit): Think Python
Enter quantity: 2

============================================================
RECEIPT
============================================================
Book Title: Think Python
Unit Price: Rs.475.00
Quantity: 2
Total Amount: Rs.950.00
============================================================
```

---

## Test Demonstration

### Command
```powershell
python test_bookstore.py
```

### Output
```
======================================================================
BOOKSTORE QUERY DEMONSTRATION
======================================================================

--- Test Case 1: Think Python (2 copies) ---
Book Title: Think Python
Unit Price: Rs.475.00
Quantity: 2
Total Amount: Rs.950.00

--- Test Case 2: Python Crash Course (3 copies) ---
Book Title: Python Crash Course
Unit Price: Rs.599.99
Quantity: 3
Total Amount: Rs.1799.97

--- Test Case 3: Fluent Python (1 copy) ---
Book Title: Fluent Python
Unit Price: Rs.799.50
Quantity: 1
Total Amount: Rs.799.50

--- Test Case 4: Non-existent book ---
Sorry, 'Unknown Book' is not in stock.

======================================================================
All Books in Database:
======================================================================
ID    Title                                    Author               Price
---------------------------------------------------------------------------
5     Automate the Boring Stuff with Python    Al Sweigart          Rs.525.00
8     Clean Code                               Robert C. Martin     Rs.695.00
7     Effective Python                         Brett Slatkin        Rs.725.00
3     Fluent Python                            Luciano Ramalho      Rs.799.50
4     Learning Python                          Mark Lutz            Rs.850.00
2     Python Crash Course                      Eric Matthes         Rs.599.99
6     Python for Data Analysis                 Wes McKinney         Rs.650.00
1     Think Python                             Allen B. Downey      Rs.475.00

✓ Test demonstration complete.
```

---

## Key Features Implemented

✓ **Part 1**: Creates SQLite database and inserts book data using INSERT queries  
✓ **Part 2**: Accepts user input (book title and quantity)  
✓ **Part 2**: Executes SELECT queries to fetch price from database  
✓ **Part 2**: Calculates total amount (price × quantity)  
✓ **Error Handling**: Handles invalid input and books not in stock  
✓ **Database File**: `bookstore.db` generated at runtime  

---

## How to Use

1. **Setup Database** (first time only):
   ```powershell
   python create_db.py
   ```

2. **Run Interactive Application**:
   ```powershell
   python bookstore.py
   ```
   Then enter book titles and quantities as prompted.

3. **Test Without User Input**:
   ```powershell
   python test_bookstore.py
   ```

---

## Notes

- The database is case-insensitive for book title searches (uses LOWER() in SQL)
- All prices are displayed in Indian Rupees (Rs.)
- Quantities must be positive integers
- Non-existent books display "not in stock" message
