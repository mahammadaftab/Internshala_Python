"""
create_db.py

Assignment 4 - Part 1: Create SQLite database and insert book data

This script creates a 'bookstore.db' database with a 'books' table containing
book_id (primary key), title, author, and price. Populates the table with
sample book data using INSERT queries.
"""
import sqlite3
from pathlib import Path


def create_and_populate_db(db_path: str = 'bookstore.db') -> None:
    """Create bookstore database and populate with sample book data."""

    # Connect to database (creates if doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print(f"Creating database: {db_path}")

    # Drop table if exists (for fresh start)
    cursor.execute("DROP TABLE IF EXISTS books")

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
    print("✓ Table 'books' created successfully.")

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

    print(f"✓ Inserted {len(books_data)} books into the database.")

    # Display inserted data
    print("\nBooks in database:")
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    print(f"{'ID':<5} {'Title':<40} {'Author':<25} {'Price':<10}")
    print("-" * 80)
    for row in rows:
        book_id, title, author, price = row
        print(f"{book_id:<5} {title:<40} {author:<25} Rs.{price:<10.2f}")

    conn.close()
    print(f"\n✓ Database setup complete: {db_path}")


if __name__ == '__main__':
    create_and_populate_db()
