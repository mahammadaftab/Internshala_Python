"""
bookstore.py

Assignment 4 - Part 2: Bookstore query application

This script connects to the bookstore.db database and allows the user to:
1. Input a book title
2. Input the quantity desired
3. Fetch the price from the database using SELECT query
4. Calculate and display the total amount
"""
import sqlite3
from pathlib import Path


def bookstore_query(db_path: str = 'bookstore.db') -> None:
    """Interactive bookstore application for querying books and calculating totals."""

    # Check if database exists
    if not Path(db_path).exists():
        print(f"Error: Database '{db_path}' not found.")
        print("Please run 'create_db.py' first to create the database.")
        return

    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("=" * 60)
    print("Welcome to the Bookstore!")
    print("=" * 60)

    while True:
        # Display available books
        print("\nAvailable Books:")
        print("-" * 60)
        cursor.execute("SELECT book_id, title, author, price FROM books ORDER BY title")
        books = cursor.fetchall()

        if not books:
            print("No books in database.")
            break

        for book_id, title, author, price in books:
            print(f"{book_id}. {title:<40} by {author:<20} Rs.{price:.2f}")

        print("-" * 60)

        # Get user input
        try:
            book_title = input("\nEnter book title (or 'quit' to exit): ").strip()

            if book_title.lower() == 'quit':
                print("Thank you for visiting! Goodbye.")
                break

            if not book_title:
                print("Please enter a valid book title.")
                continue

            quantity_str = input("Enter quantity: ").strip()
            quantity = int(quantity_str)

            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue

            # Query database for book price
            cursor.execute("SELECT price FROM books WHERE LOWER(title) = LOWER(?)", (book_title,))
            result = cursor.fetchone()

            if result is None:
                print(f"Sorry, '{book_title}' is not in stock.")
                continue

            price = result[0]
            total_amount = price * quantity

            # Display receipt
            print("\n" + "=" * 60)
            print("RECEIPT")
            print("=" * 60)
            print(f"Book Title: {book_title}")
            print(f"Unit Price: Rs.{price:.2f}")
            print(f"Quantity: {quantity}")
            print(f"Total Amount: Rs.{total_amount:.2f}")
            print("=" * 60)

        except ValueError:
            print("Invalid input. Please enter a valid quantity (number).")
        except Exception as e:
            print(f"An error occurred: {e}")

    conn.close()


if __name__ == '__main__':
    bookstore_query()
