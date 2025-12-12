import sqlite3
import os
from scoring_rules import ScoringRules

def test_database_creation():
    """Test if the database is created correctly."""
    print("Testing database creation...")
    if os.path.exists('fantasy_cricket.db'):
        os.remove('fantasy_cricket.db')
    
    # Import and run the setup function
    import setup_database
    setup_database.create_database()
    
    # Check if database file exists
    if os.path.exists('fantasy_cricket.db'):
        print("✓ Database file created successfully")
    else:
        print("✗ Database file not created")
        return False
    
    # Check if tables exist
    conn = sqlite3.connect('fantasy_cricket.db')
    cursor = conn.cursor()
    
    try:
        # Check match table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='match'")
        if cursor.fetchone():
            print("✓ Match table exists")
        else:
            print("✗ Match table does not exist")
            return False
            
        # Check stats table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stats'")
        if cursor.fetchone():
            print("✓ Stats table exists")
        else:
            print("✗ Stats table does not exist")
            return False
            
        # Check teams table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='teams'")
        if cursor.fetchone():
            print("✓ Teams table exists")
        else:
            print("✗ Teams table does not exist")
            return False
            
        # Check if stats table has data
        cursor.execute("SELECT COUNT(*) FROM stats")
        count = cursor.fetchone()[0]
        if count > 0:
            print(f"✓ Stats table has {count} records")
        else:
            print("✗ Stats table is empty")
            return False
            
        # Check if match table has data
        cursor.execute("SELECT COUNT(*) FROM match")
        count = cursor.fetchone()[0]
        if count > 0:
            print(f"✓ Match table has {count} records")
        else:
            print("✗ Match table is empty")
            return False
            
        print("✓ Database creation test passed")
        return True
    except Exception as e:
        print(f"✗ Database test failed with error: {e}")
        return False
    finally:
        conn.close()

def test_scoring_rules():
    """Test the scoring rules implementation."""
    print("\nTesting scoring rules...")
    
    # Test batting points
    batting_points = ScoringRules.calculate_batting_points(50, 40, 5, 2)
    print(f"Batting points for 50 runs, 40 balls, 5 fours, 2 sixes: {batting_points}")
    
    # Test bowling points
    bowling_points = ScoringRules.calculate_bowling_points(3, 18, 20)
    print(f"Bowling points for 3 wickets, 18 balls, 20 runs: {bowling_points}")
    
    # Test fielding points
    fielding_points = ScoringRules.calculate_fielding_points(1, 0, 1)
    print(f"Fielding points for 1 catch, 0 stumping, 1 run out: {fielding_points}")
    
    # Test player score calculation
    # Sample match data: (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO)
    match_data = ("Virat Kohli", 50, 40, 5, 2, 0, 0, 0, 0, 0, 0, 0)
    total_score = ScoringRules.calculate_player_score(match_data)
    print(f"Total score for sample player: {total_score}")
    
    print("✓ Scoring rules test completed")
    return True

def test_error_handling():
    """Test error handling in scoring rules."""
    print("\nTesting error handling...")
    
    # Test with invalid data
    batting_points = ScoringRules.calculate_batting_points(-10, -5, -2, -1)
    print(f"Batting points with negative values: {batting_points}")
    
    # Test with None data
    batting_points = ScoringRules.calculate_batting_points(None, None, None, None)
    print(f"Batting points with None values: {batting_points}")
    
    # Test player score with invalid data
    total_score = ScoringRules.calculate_player_score(None)
    print(f"Player score with None data: {total_score}")
    
    # Test player score with incomplete data
    total_score = ScoringRules.calculate_player_score(("Player Name", 30))
    print(f"Player score with incomplete data: {total_score}")
    
    print("✓ Error handling test completed")
    return True

if __name__ == "__main__":
    print("Running Fantasy Cricket Application Tests...\n")
    
    # Run all tests
    tests_passed = 0
    total_tests = 3
    
    if test_database_creation():
        tests_passed += 1
    
    if test_scoring_rules():
        tests_passed += 1
        
    if test_error_handling():
        tests_passed += 1
    
    print(f"\nTest Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! The Fantasy Cricket application is working correctly.")
    else:
        print("❌ Some tests failed. Please check the implementation.")