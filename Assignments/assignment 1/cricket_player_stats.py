"""
Cricket Player Statistics Data Structure
Assignment 1 - Internshala Python Course

This module defines the data structure for storing individual cricket player statistics.
A player can represent multiple teams and play in multiple formats (Test, ODI, T20).
"""

from typing import List, Dict, Tuple
from dataclasses import dataclass
from datetime import date


# Data Structure for Cricket Player Statistics
@dataclass
class FormatStats:
    """Statistics for a specific cricket format (Test, ODI, T20)"""
    format_name: str  # str: Name of format (Test, ODI, T20)
    matches_played: int  # int: Number of matches played in this format
    runs_scored: int  # int: Total runs scored in this format
    wickets_taken: int  # int: Total wickets taken in this format
    batting_average: float  # float: Average runs per match (runs / matches)
    bowling_average: float  # float: Average runs per wicket given up
    strike_rate: float  # float: Runs per 100 balls
    highest_score: int  # int: Highest individual score
    best_bowling: str  # str: Best bowling figures (e.g., "5/32")


@dataclass
class TeamRecord:
    """Record of player's tenure with a specific team"""
    team_name: str  # str: Name of the team
    joining_date: date  # date: Date when player joined the team
    departure_date: date  # date: Date when player left the team (None if current)
    role: str  # str: Player's role in team (Batsman, Bowler, All-rounder, Wicket-keeper)
    jersey_number: int  # int: Jersey number with this team
    matches_for_team: int  # int: Total matches played for this team


@dataclass
class CricketPlayer:
    """Complete data structure for a cricket player"""
    # Personal Information
    player_id: int  # int: Unique identifier for the player
    first_name: str  # str: Player's first name
    last_name: str  # str: Player's last name
    date_of_birth: date  # date: Player's date of birth
    nationality: str  # str: Player's country
    
    # Physical Attributes
    height_cm: float  # float: Height in centimeters
    batting_hand: str  # str: Dominant batting hand (Left/Right)
    bowling_hand: str  # str: Dominant bowling hand (Left/Right)
    
    # Career Information
    career_start_year: int  # int: Year when player started international career
    career_end_year: int  # int: Year when player retired (0 if still active)
    primary_role: str  # str: Primary role (Batsman, Bowler, All-rounder, Wicket-keeper)
    
    # Team History
    teams_represented: List[TeamRecord]  # List[TeamRecord]: Teams the player has played for
    
    # Format-wise Statistics
    test_stats: FormatStats  # FormatStats: Test cricket statistics
    odi_stats: FormatStats  # FormatStats: ODI (One Day International) statistics
    t20_stats: FormatStats  # FormatStats: T20 cricket statistics
    
    # Additional Metrics
    international_caps: int  # int: Total international matches played
    century_count: int  # int: Total centuries (100+ runs in a match)
    half_century_count: int  # int: Total half-centuries (50+ runs in a match)
    man_of_the_match_awards: int  # int: Total Player of the Match awards
    is_active: bool  # bool: Whether player is currently active


# Example Usage and Sample Data
def create_sample_player() -> CricketPlayer:
    """Create a sample cricket player for demonstration"""
    
    player = CricketPlayer(
        player_id=1001,
        first_name="Virat",
        last_name="Kohli",
        date_of_birth=date(1988, 11, 5),
        nationality="India",
        height_cm=175.5,
        batting_hand="Right",
        bowling_hand="Right",
        career_start_year=2008,
        career_end_year=0,  # Still active
        primary_role="Batsman",
        teams_represented=[
            TeamRecord(
                team_name="India",
                joining_date=date(2008, 8, 19),
                departure_date=None,
                role="Batsman",
                jersey_number=18,
                matches_for_team=250
            ),
            TeamRecord(
                team_name="Royal Challengers Bangalore",
                joining_date=date(2008, 4, 18),
                departure_date=None,
                role="Batsman",
                jersey_number=18,
                matches_for_team=180
            )
        ],
        test_stats=FormatStats(
            format_name="Test",
            matches_played=99,
            runs_scored=8200,
            wickets_taken=0,
            batting_average=50.61,
            bowling_average=0.0,
            strike_rate=58.45,
            highest_score=254,
            best_bowling="0/0"
        ),
        odi_stats=FormatStats(
            format_name="ODI",
            matches_played=284,
            runs_scored=12000,
            wickets_taken=0,
            batting_average=58.50,
            bowling_average=0.0,
            strike_rate=93.67,
            highest_score=183,
            best_bowling="0/0"
        ),
        t20_stats=FormatStats(
            format_name="T20",
            matches_played=115,
            runs_scored=3500,
            wickets_taken=0,
            batting_average=31.82,
            bowling_average=0.0,
            strike_rate=139.68,
            highest_score=94,
            best_bowling="0/0"
        ),
        international_caps=498,
        century_count=48,
        half_century_count=67,
        man_of_the_match_awards=42,
        is_active=True
    )
    
    return player


# Display Functions
def display_player_summary(player: CricketPlayer) -> None:
    """Display a summary of player information"""
    print(f"\n{'='*60}")
    print(f"CRICKET PLAYER PROFILE")
    print(f"{'='*60}")
    print(f"Name: {player.first_name} {player.last_name}")
    print(f"Player ID: {player.player_id}")
    print(f"DOB: {player.date_of_birth}")
    print(f"Nationality: {player.nationality}")
    print(f"Primary Role: {player.primary_role}")
    print(f"Active: {'Yes' if player.is_active else 'No'}")
    print(f"International Caps: {player.international_caps}")
    print(f"Centuries: {player.century_count}")
    print(f"Half-Centuries: {player.half_century_count}")
    print(f"Player of the Match Awards: {player.man_of_the_match_awards}")
    print(f"{'='*60}\n")


def display_format_stats(stats: FormatStats) -> None:
    """Display statistics for a specific format"""
    print(f"\n{stats.format_name} STATISTICS")
    print(f"{'-'*40}")
    print(f"Matches: {stats.matches_played}")
    print(f"Runs: {stats.runs_scored}")
    print(f"Wickets: {stats.wickets_taken}")
    print(f"Batting Average: {stats.batting_average:.2f}")
    print(f"Bowling Average: {stats.bowling_average:.2f}")
    print(f"Strike Rate: {stats.strike_rate:.2f}")
    print(f"Highest Score: {stats.highest_score}")
    print(f"Best Bowling: {stats.best_bowling}")


if __name__ == "__main__":
    # Create and display sample player
    player = create_sample_player()
    display_player_summary(player)
    
    # Display format-wise statistics
    display_format_stats(player.test_stats)
    display_format_stats(player.odi_stats)
    display_format_stats(player.t20_stats)
    
    print("\n" + "="*60)
    print("TEAMS REPRESENTED")
    print("="*60)
    for team in player.teams_represented:
        print(f"\nTeam: {team.team_name}")
        print(f"Joining Date: {team.joining_date}")
        if team.departure_date:
            print(f"Departure Date: {team.departure_date}")
        else:
            print(f"Status: Currently playing")
        print(f"Role: {team.role}")
        print(f"Jersey Number: {team.jersey_number}")
        print(f"Matches for Team: {team.matches_for_team}")
