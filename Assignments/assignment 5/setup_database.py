"""
setup_database.py

Setup script for Assignment 5: Create bookstore database if not already present.
This is a helper script to ensure the database exists before running the GUI app.
"""
import sqlite3
from pathlib import Path


def setup_bookstore_db(db_path: str = 'bookstore.db') -> None:
    """Create bookstore database with sample data if it doesn't exist."""
    
    if Path(db_path).exists():
        print(f"Database '{db_path}' already exists.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"Creating database: {db_path}")
    
    # Create books table
    create_table_query = """
    CREATE TABLE books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        price REAL NOT NULL
    )
    """
    cursor.execute(create_table_query)
    
    # Sample book data
    books_data = [
        ("Think Python", "Allen B. Downey", 475.00),
        ("Python Crash Course", "Eric Matthes", 599.99),
        ("Fluent Python", "Luciano Ramalho", 799.50),
        ("Learning Python", "Mark Lutz", 850.00),
        ("Automate the Boring Stuff with Python", "Al Sweigart", 525.00),
        ("Python for Data Analysis", "Wes McKinney", 650.00),
        ("Effective Python", "Brett Slatkin", 725.00),
        ("Clean Code", "Robert C. Martin", 695.00),
    ]
    
    # Insert data
    insert_query = "INSERT INTO books (title, author, price) VALUES (?, ?, ?)"
    cursor.executemany(insert_query, books_data)
    conn.commit()
    conn.close()
    
    print(f"✓ Database created with {len(books_data)} books.")


if __name__ == '__main__':
    setup_bookstore_db()
