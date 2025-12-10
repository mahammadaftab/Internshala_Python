"""
test_bookstore.py

Test script that simulates user interactions with the bookstore.py application
for demonstration purposes without requiring interactive input.
"""
import sqlite3


def test_bookstore_queries(db_path: str = 'bookstore.db') -> None:
    """Demonstrate bookstore queries without interactive input."""

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("=" * 70)
    print("BOOKSTORE QUERY DEMONSTRATION")
    print("=" * 70)

    # Test case 1: Think Python, 2 copies
    print("\n--- Test Case 1: Think Python (2 copies) ---")
    book_title = "Think Python"
    quantity = 2
    cursor.execute("SELECT price FROM books WHERE LOWER(title) = LOWER(?)", (book_title,))
    result = cursor.fetchone()

    if result:
        price = result[0]
        total = price * quantity
        print(f"Book Title: {book_title}")
        print(f"Unit Price: Rs.{price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total Amount: Rs.{total:.2f}")
    else:
        print(f"Book not found: {book_title}")

    # Test case 2: Python Crash Course, 3 copies
    print("\n--- Test Case 2: Python Crash Course (3 copies) ---")
    book_title = "Python Crash Course"
    quantity = 3
    cursor.execute("SELECT price FROM books WHERE LOWER(title) = LOWER(?)", (book_title,))
    result = cursor.fetchone()

    if result:
        price = result[0]
        total = price * quantity
        print(f"Book Title: {book_title}")
        print(f"Unit Price: Rs.{price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total Amount: Rs.{total:.2f}")
    else:
        print(f"Book not found: {book_title}")

    # Test case 3: Fluent Python, 1 copy
    print("\n--- Test Case 3: Fluent Python (1 copy) ---")
    book_title = "Fluent Python"
    quantity = 1
    cursor.execute("SELECT price FROM books WHERE LOWER(title) = LOWER(?)", (book_title,))
    result = cursor.fetchone()

    if result:
        price = result[0]
        total = price * quantity
        print(f"Book Title: {book_title}")
        print(f"Unit Price: Rs.{price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total Amount: Rs.{total:.2f}")
    else:
        print(f"Book not found: {book_title}")

    # Test case 4: Book not in stock
    print("\n--- Test Case 4: Non-existent book ---")
    book_title = "Unknown Book"
    cursor.execute("SELECT price FROM books WHERE LOWER(title) = LOWER(?)", (book_title,))
    result = cursor.fetchone()

    if result:
        price = result[0]
        total = price * 2
        print(f"Book Title: {book_title}")
        print(f"Total Amount: Rs.{total:.2f}")
    else:
        print(f"Sorry, '{book_title}' is not in stock.")

    # Display all books for reference
    print("\n" + "=" * 70)
    print("All Books in Database:")
    print("=" * 70)
    cursor.execute("SELECT book_id, title, author, price FROM books ORDER BY title")
    rows = cursor.fetchall()
    print(f"{'ID':<5} {'Title':<40} {'Author':<20} {'Price':<10}")
    print("-" * 75)
    for book_id, title, author, price in rows:
        print(f"{book_id:<5} {title:<40} {author:<20} Rs.{price:.2f}")

    conn.close()
    print("\n✓ Test demonstration complete.")


if __name__ == '__main__':
    test_bookstore_queries()
