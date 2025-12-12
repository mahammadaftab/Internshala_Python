"""
Scoring Rules for Fantasy Cricket Game

This module contains the implementation of scoring rules for the fantasy cricket game.
"""

class ScoringRules:
    """
    A class to encapsulate all the scoring rules for the fantasy cricket game.
    """
    
    @staticmethod
    def calculate_batting_points(runs, balls_faced, fours, sixes):
        """
        Calculate batting points based on the given parameters.
        
        Args:
            runs (int): Runs scored by the player
            balls_faced (int): Balls faced by the player
            fours (int): Number of fours hit
            sixes (int): Number of sixes hit
            
        Returns:
            int: Total batting points
        """
        try:
            points = 0
            
            # Validate inputs
            if not isinstance(runs, int) or runs < 0:
                runs = 0
            if not isinstance(balls_faced, int) or balls_faced < 0:
                balls_faced = 0
            if not isinstance(fours, int) or fours < 0:
                fours = 0
            if not isinstance(sixes, int) or sixes < 0:
                sixes = 0
            
            # 1 point for 2 runs scored
            points += runs // 2
            
            # Additional 5 points for half century
            if runs >= 50:
                points += 5
                
            # Additional 10 points for century
            if runs >= 100:
                points += 10
                
            # Strike rate points
            if balls_faced > 0:
                strike_rate = (runs / balls_faced) * 100
                if 80 <= strike_rate <= 100:
                    points += 2  # 2 points for strike rate 80-100
                elif strike_rate > 100:
                    points += 4  # Additional 4 points for strike rate > 100
                    
            # Boundary points
            points += fours * 1  # 1 point for hitting a boundary (four)
            points += sixes * 2  # 2 points for over boundary (six)
            
            return points
        except Exception:
            # Return 0 points if there's an error in calculation
            return 0
    
    @staticmethod
    def calculate_bowling_points(wickets, balls_bowled, runs_given):
        """
        Calculate bowling points based on the given parameters.
        
        Args:
            wickets (int): Wickets taken by the player
            balls_bowled (int): Balls bowled by the player
            runs_given (int): Runs given by the player
            
        Returns:
            int: Total bowling points
        """
        try:
            points = 0
            
            # Validate inputs
            if not isinstance(wickets, int) or wickets < 0:
                wickets = 0
            if not isinstance(balls_bowled, int) or balls_bowled < 0:
                balls_bowled = 0
            if not isinstance(runs_given, int) or runs_given < 0:
                runs_given = 0
            
            # 10 points for each wicket
            points += wickets * 10
            
            # Additional points for wickets per innings
            if wickets >= 3:
                points += 5  # Additional 5 points for three wickets per innings
            if wickets >= 5:
                points += 10  # Additional 10 points for 5 wickets or more in innings
                
            # Economy rate points
            if balls_bowled > 0:
                overs = balls_bowled / 6
                if overs > 0:
                    economy_rate = runs_given / overs
                    if 3.5 <= economy_rate <= 4.5:
                        points += 4  # 4 points for economy rate between 3.5 and 4.5
                    elif 2 <= economy_rate < 3.5:
                        points += 7  # 7 points for economy rate between 2 and 3.5
                    elif economy_rate < 2:
                        points += 10  # 10 points for economy rate less than 2
                        
            return points
        except Exception:
            # Return 0 points if there's an error in calculation
            return 0
    
    @staticmethod
    def calculate_fielding_points(catches, stumpings, run_outs):
        """
        Calculate fielding points based on the given parameters.
        
        Args:
            catches (int): Catches taken by the player
            stumpings (int): Stumpings done by the player
            run_outs (int): Run outs done by the player
            
        Returns:
            int: Total fielding points
        """
        try:
            # Validate inputs
            if not isinstance(catches, int) or catches < 0:
                catches = 0
            if not isinstance(stumpings, int) or stumpings < 0:
                stumpings = 0
            if not isinstance(run_outs, int) or run_outs < 0:
                run_outs = 0
            
            # 10 points each for catch/stumping/run out
            points = (catches + stumpings + run_outs) * 10
            return points
        except Exception:
            # Return 0 points if there's an error in calculation
            return 0
    
    @staticmethod
    def calculate_player_score(match_data):
        """
        Calculate total points for a player based on match data.
        
        Args:
            match_data (tuple): Tuple containing player match data in the following order:
                              (Player, Scored, Faced, Fours, Sixes, Bowled, Maiden, Given, Wkts, Catches, Stumping, RO)
                              
        Returns:
            int: Total points for the player
        """
        try:
            # Validate input
            if not match_data or not isinstance(match_data, (tuple, list)) or len(match_data) < 12:
                return 0
            
            # Extract data from match_data tuple
            scored = match_data[1] if len(match_data) > 1 else 0      # Runs scored
            faced = match_data[2] if len(match_data) > 2 else 0       # Balls faced
            fours = match_data[3] if len(match_data) > 3 else 0       # Fours
            sixes = match_data[4] if len(match_data) > 4 else 0       # Sixes
            bowled = match_data[5] if len(match_data) > 5 else 0      # Balls bowled
            given = match_data[7] if len(match_data) > 7 else 0       # Runs given
            wkts = match_data[8] if len(match_data) > 8 else 0        # Wickets
            catches = match_data[9] if len(match_data) > 9 else 0     # Catches
            stumping = match_data[10] if len(match_data) > 10 else 0   # Stumping
            run_outs = match_data[11] if len(match_data) > 11 else 0   # Run Outs
            
            # Calculate points for each category
            batting_points = ScoringRules.calculate_batting_points(scored, faced, fours, sixes)
            bowling_points = ScoringRules.calculate_bowling_points(wkts, bowled, given)
            fielding_points = ScoringRules.calculate_fielding_points(catches, stumping, run_outs)
            
            # Return total points
            return batting_points + bowling_points + fielding_points
        except Exception:
            # Return 0 points if there's an error in calculation
            return 0