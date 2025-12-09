# Assignment 3 — Book & EBook Royalty Output

This file records sample output from `assignment3_main.py` (royalty calculations).

## Command

```powershell
cd "Assignments\assignment 3"
python assignment3_main.py
```

## Output

```
Physical Book Royalties for different copies sold:
copies=    0 -> royalty=      0.00
copies=  100 -> royalty=   5000.00
copies=  500 -> royalty=  25000.00
copies=  800 -> royalty=  43750.00
copies= 1500 -> royalty=  87500.00
copies= 2500 -> royalty= 162500.00

EBook Royalties (after 12% GST) for different copies sold:
copies=    0 -> royalty=      0.00
copies=  100 -> royalty=   2640.00
copies=  500 -> royalty=  13200.00
copies=  800 -> royalty=  23100.00
copies= 1500 -> royalty=  46200.00
copies= 2500 -> royalty=  85800.00

Book properties:
Title: Learning Python
Author: A. Developer
Publisher: TechPress
Price: 500.0
Updated Price: 550.0
Royalty for 1000 copies (after price update): 61875.0
```

## Notes
- `Book.royalty(copies_sold)` computes royalties using the tiered scheme:
  - 10% on first 500 copies
  - 12.5% on the next 1,000 copies
  - 15% on further copies
- `EBook.royalty` applies the same tiered base calculation and then deducts GST @12%.
- All monetary results are rounded to 2 decimal places where appropriate.
