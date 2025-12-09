"""
Demo script for Assignment 3: Book and EBook classes

Creates sample Book and EBook instances and prints royalty calculations
for a variety of copies sold to demonstrate tiered calculations and GST
on ebooks.
"""
from books import Book, EBook


def main():
    # Create a sample physical book
    b = Book(title="Learning Python", author="A. Developer", publisher="TechPress", price=500.0)

    # Create a sample ebook
    eb = EBook(title="Learning Python (Ebook)", author="A. Developer", publisher="TechPress", price=300.0, ebook_format="EPUB")

    test_copies = [0, 100, 500, 800, 1500, 2500]

    print("Physical Book Royalties for different copies sold:")
    for c in test_copies:
        print(f"copies={c:5d} -> royalty={b.royalty(c):10.2f}")

    print("\nEBook Royalties (after 12% GST) for different copies sold:")
    for c in test_copies:
        print(f"copies={c:5d} -> royalty={eb.royalty(c):10.2f}")

    # Show properties working
    print("\nBook properties:")
    print("Title:", b.title)
    print("Author:", b.author)
    print("Publisher:", b.publisher)
    print("Price:", b.price)

    # Modify price via setter
    b.price = 550.0
    print("Updated Price:", b.price)
    print("Royalty for 1000 copies (after price update):", b.royalty(1000))


if __name__ == '__main__':
    main()
