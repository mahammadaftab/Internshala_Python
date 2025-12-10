"""
bookstore_gui.py

Assignment 5: PyQt5 GUI application for Bookstore
Features:
- Find book price from database
- Accept integer quantity input (via QSpinBox)
- Calculate total amount (price × quantity)
- Display error messages if book not found
- Clear all fields
"""
import sys
import sqlite3
from pathlib import Path
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QGroupBox, QFormLayout,
                             QSpinBox, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class BookstoreApplication(QMainWindow):
    """Main Bookstore GUI Application."""
    
    def __init__(self, db_path: str = 'bookstore.db'):
        super().__init__()
        self.db_path = db_path
        self.current_price = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI components."""
        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        
        # Title
        title_label = QLabel("Bookstore Application")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Group box for form
        group_box = QGroupBox("Book Details")
        form_layout = QFormLayout()
        
        # Book Title Input
        self.book_title_label = QLabel("Book Title:")
        self.book_title_input = QLineEdit()
        self.book_title_input.setPlaceholderText("Enter book title")
        form_layout.addRow(self.book_title_label, self.book_title_input)
        
        # Price Display
        self.price_label = QLabel("Price (Rs.):")
        self.price_display = QLineEdit()
        self.price_display.setReadOnly(True)
        self.price_display.setPlaceholderText("Price will be displayed here")
        form_layout.addRow(self.price_label, self.price_display)
        
        # Quantity Input (QSpinBox for integer-only input)
        self.quantity_label = QLabel("Quantity:")
        self.quantity_input = QSpinBox()
        self.quantity_input.setMinimum(1)
        self.quantity_input.setMaximum(999)
        self.quantity_input.setValue(1)
        form_layout.addRow(self.quantity_label, self.quantity_input)
        
        # Total Amount Display
        self.total_label = QLabel("Total Amount (Rs.):")
        self.total_display = QLineEdit()
        self.total_display.setReadOnly(True)
        self.total_display.setPlaceholderText("Total will be calculated here")
        form_layout.addRow(self.total_label, self.total_display)
        
        group_box.setLayout(form_layout)
        main_layout.addWidget(group_box)
        
        # Buttons layout
        buttons_layout = QHBoxLayout()
        
        # Find Price button
        self.find_price_btn = QPushButton("Find Price")
        self.find_price_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 5px; "
                                          "border-radius: 3px; font-weight: bold; min-width: 100px;")
        self.find_price_btn.clicked.connect(self.find_price)
        buttons_layout.addWidget(self.find_price_btn)
        
        # Find Total button
        self.find_total_btn = QPushButton("Find Total Amount")
        self.find_total_btn.setStyleSheet("background-color: #2196F3; color: white; padding: 5px; "
                                          "border-radius: 3px; font-weight: bold; min-width: 100px;")
        self.find_total_btn.clicked.connect(self.find_total_amount)
        buttons_layout.addWidget(self.find_total_btn)
        
        # Clear button
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setStyleSheet("background-color: #f44336; color: white; padding: 5px; "
                                     "border-radius: 3px; font-weight: bold; min-width: 100px;")
        self.clear_btn.clicked.connect(self.clear_fields)
        buttons_layout.addWidget(self.clear_btn)
        
        # Spacer
        buttons_layout.addStretch()
        
        main_layout.addLayout(buttons_layout)
        
        # Message label
        self.message_label = QLabel()
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setStyleSheet("color: #d32f2f; font-weight: bold; margin: 10px;")
        main_layout.addWidget(self.message_label)
        
        # Vertical spacer
        main_layout.addStretch()
        
        central_widget.setLayout(main_layout)
        
        # Window properties
        self.setWindowTitle("Bookstore - Find Book Price and Total")
        self.setGeometry(100, 100, 600, 400)
    
    def find_price(self):
        """Fetch price from database when Find Price button is clicked."""
        book_title = self.book_title_input.text().strip()
        
        if not book_title:
            self.show_message("Please enter a book title.", error=True)
            return
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Query database for book price
            cursor.execute("SELECT price FROM books WHERE LOWER(title) = LOWER(?)", (book_title,))
            result = cursor.fetchone()
            conn.close()
            
            if result is None:
                self.show_message(f"Book '{book_title}' is not found.", error=True)
                self.price_display.clear()
                self.current_price = None
            else:
                self.current_price = result[0]
                self.price_display.setText(f"{self.current_price:.2f}")
                self.message_label.clear()
        
        except sqlite3.Error as e:
            self.show_message(f"Database error: {e}", error=True)
    
    def find_total_amount(self):
        """Calculate and display total amount when Find Total Amount button is clicked."""
        if self.current_price is None:
            self.show_message("Please find the price first.", error=True)
            return
        
        quantity = self.quantity_input.value()
        
        if quantity <= 0:
            self.show_message("Quantity must be greater than 0.", error=True)
            return
        
        total = self.current_price * quantity
        self.total_display.setText(f"{total:.2f}")
        self.message_label.clear()
    
    def clear_fields(self):
        """Clear all input and display fields."""
        self.book_title_input.clear()
        self.price_display.clear()
        self.quantity_input.setValue(1)
        self.total_display.clear()
        self.message_label.clear()
        self.current_price = None
        self.book_title_input.setFocus()
    
    def show_message(self, message: str, error: bool = False):
        """Display message in the message label or as dialog."""
        if error:
            self.message_label.setText(f"⚠ {message}")
            self.message_label.setStyleSheet("color: #d32f2f; font-weight: bold; margin: 10px;")
        else:
            self.message_label.setText(message)
            self.message_label.setStyleSheet("color: #388E3C; font-weight: bold; margin: 10px;")


def main():
    """Main entry point for the application."""
    # Check if database exists
    if not Path('bookstore.db').exists():
        print("Database not found. Running setup_database.py first...")
        import subprocess
        subprocess.run([sys.executable, 'setup_database.py'], cwd=Path(__file__).parent)
    
    app = QApplication(sys.argv)
    window = BookstoreApplication()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
