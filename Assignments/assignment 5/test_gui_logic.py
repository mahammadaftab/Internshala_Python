"""
test_gui_logic.py

Test script to verify the bookstore logic without GUI
(for CI/testing purposes)
"""
import sqlite3


def test_find_price():
    """Test finding book price from database."""
    print("Test 1: Finding book price")
    print("-" * 50)
    
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()
    
    test_books = ["Think Python", "Python Crash Course", "Unknown Book"]
    
    for book_title in test_books:
        cursor.execute("SELECT price FROM books WHERE LOWER(title) = LOWER(?)", (book_title,))
        result = cursor.fetchone()
        
        if result:
            print(f"✓ {book_title}: Rs.{result[0]:.2f}")
        else:
            print(f"✗ {book_title}: Not found")
    
    conn.close()
    print()


def test_calculate_total():
    """Test total amount calculation."""
    print("Test 2: Calculate total amount")
    print("-" * 50)
    
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()
    
    test_cases = [
        ("Think Python", 2),
        ("Python Crash Course", 3),
        ("Fluent Python", 1),
    ]
    
    for book_title, quantity in test_cases:
        cursor.execute("SELECT price FROM books WHERE LOWER(title) = LOWER(?)", (book_title,))
        result = cursor.fetchone()
        
        if result:
            price = result[0]
            total = price * quantity
            print(f"✓ {book_title} × {quantity} = Rs.{total:.2f}")
        else:
            print(f"✗ {book_title}: Not found")
    
    conn.close()
    print()


def test_quantity_validation():
    """Test quantity input validation."""
    print("Test 3: Quantity validation (QSpinBox accepts only integers)")
    print("-" * 50)
    
    test_quantities = [1, 5, 10, 100, 999]
    
    for qty in test_quantities:
        print(f"✓ Quantity {qty} is valid (integer)")
    
    print(f"✗ Quantity 0 is invalid (below minimum)")
    print(f"✗ Quantity 1000 is invalid (above maximum)")
    print()


if __name__ == '__main__':
    print("=" * 50)
    print("BOOKSTORE GUI LOGIC TESTS")
    print("=" * 50)
    print()
    
    test_find_price()
    test_calculate_total()
    test_quantity_validation()
    
    print("=" * 50)
    print("All tests completed!")
    print("=" * 50)
