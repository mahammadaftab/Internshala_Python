import sqlite3
import os

def create_database():
    """Create the fantasy cricket database with required tables and sample data."""
    
    # Connect to database (creates it if it doesn't exist)
    conn = sqlite3.connect('fantasy_cricket.db')
    cursor = conn.cursor()
    
    # Create match table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS match (
            Player TEXT PRIMARY KEY,
            Scored INTEGER,
            Faced INTEGER,
            Fours INTEGER,
            Sixes INTEGER,
            Bowled INTEGER,
            Maiden INTEGER,
            Given INTEGER,
            Wkts INTEGER,
            Catches INTEGER,
            Stumping INTEGER,
            RO INTEGER
        )
    ''')
    
    # Create stats table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            player TEXT PRIMARY KEY,
            matches INTEGER,
            runs INTEGER,
            "100s" INTEGER,
            "50s" INTEGER,
            value INTEGER,
            ctg TEXT
        )
    ''')
    
    # Create teams table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            name TEXT PRIMARY KEY,
            players TEXT,
            value INTEGER
        )
    ''')
    
    # Insert sample data into stats table
    stats_data = [
        ('Virat Kohli', 120, 8000, 28, 42, 120, 'BAT'),
        ('MS Dhoni', 90, 5000, 10, 30, 100, 'WK'),
        ('Yuvraj Singh', 75, 4500, 8, 25, 90, 'AR'),
        ('Bhuvneshwar Kumar', 50, 1000, 2, 5, 80, 'BWL'),
        ('Rohit Sharma', 110, 7500, 25, 38, 110, 'BAT'),
        ('Jasprit Bumrah', 40, 800, 1, 3, 95, 'BWL'),
        ('Ravindra Jadeja', 85, 3500, 5, 20, 95, 'AR'),
        ('Dinesh Karthik', 60, 2000, 3, 12, 80, 'WK'),
        ('Shikhar Dhawan', 95, 6000, 15, 35, 100, 'BAT'),
        ('Hardik Pandya', 80, 2500, 4, 18, 105, 'AR'),
        ('Kuldeep Yadav', 35, 600, 0, 2, 85, 'BWL'),
        ('KL Rahul', 85, 4000, 12, 22, 100, 'BAT'),
        ('Rishabh Pant', 55, 1800, 4, 10, 85, 'WK'),
        ('Washington Sundar', 45, 1200, 2, 8, 75, 'AR'),
        ('Mohammed Shami', 30, 500, 0, 1, 90, 'BWL')
    ]
    
    cursor.executemany('''
        INSERT OR REPLACE INTO stats (player, matches, runs, "100s", "50s", value, ctg)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', stats_data)
    
    # Insert sample data into match table
    match_data = [
        ('Virat Kohli', 120, 85, 12, 3, 0, 0, 0, 0, 0, 0, 0),
        ('MS Dhoni', 45, 30, 5, 1, 0, 0, 0, 0, 1, 1, 0),
        ('Yuvraj Singh', 60, 40, 6, 2, 10, 1, 20, 2, 1, 0, 1),
        ('Bhuvneshwar Kumar', 0, 0, 0, 0, 24, 2, 15, 3, 1, 0, 0),
        ('Rohit Sharma', 85, 60, 10, 4, 0, 0, 0, 0, 0, 0, 0),
        ('Jasprit Bumrah', 0, 0, 0, 0, 20, 1, 10, 4, 2, 0, 1),
        ('Ravindra Jadeja', 35, 25, 3, 1, 15, 1, 12, 2, 1, 0, 1),
        ('Dinesh Karthik', 25, 18, 2, 1, 0, 0, 0, 0, 1, 0, 0),
        ('Shikhar Dhawan', 70, 50, 8, 2, 0, 0, 0, 0, 0, 0, 0),
        ('Hardik Pandya', 40, 30, 4, 2, 12, 0, 18, 1, 0, 0, 1),
        ('Kuldeep Yadav', 0, 0, 0, 0, 18, 2, 14, 3, 0, 0, 0),
        ('KL Rahul', 65, 45, 7, 3, 0, 0, 0, 0, 0, 0, 0),
        ('Rishabh Pant', 30, 22, 3, 1, 0, 0, 0, 0, 1, 0, 0),
        ('Washington Sundar', 20, 15, 2, 0, 10, 0, 8, 1, 0, 0, 0),
        ('Mohammed Shami', 0, 0, 0, 0, 16, 1, 12, 2, 1, 0, 0)
    ]
    
    cursor.executemany('''
        INSERT OR REPLACE INTO match (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', match_data)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Database created successfully with sample data!")

if __name__ == "__main__":
    create_database()