"""
books.py

Defines Book and EBook classes for Assignment 3.

Book:
- instance variables: title, author, publisher, price, author_royalty
- getter/setter properties for each
- royalty(copies_sold) -> float: computes royalty amount using tiered rates

EBook (inherits Book):
- additional instance variable: format (EPUB, PDF, MOBI, etc.)
- overrides royalty() to deduct GST @ 12% on ebooks
"""
from typing import Optional


class Book:
    def __init__(self, title: str, author: str, publisher: str, price: float, author_royalty: Optional[float] = None):
        self._title = None
        self._author = None
        self._publisher = None
        self._price = None
        self._author_royalty = None

        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.author_royalty = author_royalty

    # Title
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value.strip()

    # Author
    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Author must be a non-empty string")
        self._author = value.strip()

    # Publisher
    @property
    def publisher(self) -> str:
        return self._publisher

    @publisher.setter
    def publisher(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Publisher must be a non-empty string")
        self._publisher = value.strip()

    # Price
    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        try:
            v = float(value)
        except Exception:
            raise ValueError("Price must be a number")
        if v < 0:
            raise ValueError("Price cannot be negative")
        self._price = v

    # Author royalty (optional numeric field)
    @property
    def author_royalty(self) -> Optional[float]:
        return self._author_royalty

    @author_royalty.setter
    def author_royalty(self, value: Optional[float]) -> None:
        if value is None:
            self._author_royalty = None
            return
        try:
            v = float(value)
        except Exception:
            raise ValueError("author_royalty must be a number or None")
        if v < 0:
            raise ValueError("author_royalty cannot be negative")
        self._author_royalty = v

    def royalty(self, copies_sold: int) -> float:
        """Calculate royalty amount for the given number of copies sold.

        Rules:
        - 10% of retail price on the first 500 copies
        - 12.5% for the next 1,000 copies sold (i.e., copies 501-1500)
        - 15% for all further copies sold (1501+)

        Returns a float rounded to 2 decimals.
        """
        if not isinstance(copies_sold, int) or copies_sold < 0:
            raise ValueError("copies_sold must be a non-negative integer")

        remaining = copies_sold
        total = 0.0

        # First 500 at 10%
        tier1 = min(remaining, 500)
        total += tier1 * self.price * 0.10
        remaining -= tier1

        # Next 1000 at 12.5%
        if remaining > 0:
            tier2 = min(remaining, 1000)
            total += tier2 * self.price * 0.125
            remaining -= tier2

        # Remaining at 15%
        if remaining > 0:
            total += remaining * self.price * 0.15

        return round(total, 2)

    def __repr__(self):
        return f"<Book title={self.title!r} author={self.author!r} price={self.price}>"


class EBook(Book):
    def __init__(self, title: str, author: str, publisher: str, price: float, ebook_format: str, author_royalty: Optional[float] = None):
        super().__init__(title, author, publisher, price, author_royalty)
        self._format = None
        self.format = ebook_format

    @property
    def format(self) -> str:
        return self._format

    @format.setter
    def format(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("format must be a non-empty string (e.g., EPUB, PDF, MOBI)")
        self._format = value.strip().upper()

    def royalty(self, copies_sold: int) -> float:
        """Compute ebook royalty but deduct GST at 12% from the royalty amount.

        Uses the same tiered base calculation as Book, then applies 12% GST deduction.
        """
        base = super().royalty(copies_sold)
        gst = 0.12
        net = base * (1 - gst)
        return round(net, 2)

    def __repr__(self):
        return f"<EBook title={self.title!r} author={self.author!r} format={self.format} price={self.price}>"
