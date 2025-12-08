"""
Module: match_points
Contains functions to compute batting, bowling and fielding points for a 50-over match.

Functions:
- batting_points(player_dict) -> int
- bowling_points(player_dict) -> int
- fielding_points(player_dict) -> int

Each function expects the player's performance dictionary described in the assignment.
"""
from typing import Dict


def batting_points(player: Dict) -> int:
    """Compute batting-related points according to rules.

    Rules applied:
    - 1 point for 2 runs scored (runs // 2)
    - +5 points for a half-century (runs >= 50)
    - +10 points for a century (runs >= 100)
    - +2 points for strike rate between 80 and 100 (inclusive)
    - +4 points for strike rate > 100
    - +1 point per four (key '4')
    - +2 points per six (key '6')
    """
    runs = player.get("runs", 0)
    balls = player.get("balls", 1) or 1
    fours = player.get("4", 0)
    sixes = player.get("6", 0)

    points = int(runs // 2)

    if runs >= 50:
        points += 5
    if runs >= 100:
        points += 10

    # Strike rate as runs per 100 balls
    sr = (runs / balls) * 100
    if sr > 100:
        points += 4
    elif 80 <= sr <= 100:
        points += 2

    # Boundaries
    points += int(fours) * 1
    points += int(sixes) * 2

    return points


def bowling_points(player: Dict) -> int:
    """Compute bowling-related points according to rules.

    Rules applied:
    - 10 points per wicket
    - +5 points for 3 wickets in innings (wkts >= 3)
    - +10 points for 5 or more wickets in innings (wkts >= 5)
    - Economy (runs per over):
        * +10 points if econ < 2
        * +7 points if 2 <= econ < 3.5
        * +4 points if 3.5 <= econ <= 4.5
    """
    wkts = player.get("wkts", 0)
    overs = player.get("overs", 0) or 0
    runs_conceded = player.get("runs", 0)

    points = int(wkts) * 10

    if wkts >= 3:
        points += 5
    if wkts >= 5:
        points += 10

    # Economy rate (runs per over)
    econ = float('inf')
    if overs > 0:
        econ = runs_conceded / overs

    if econ < 2:
        points += 10
    elif 2 <= econ < 3.5:
        points += 7
    elif 3.5 <= econ <= 4.5:
        points += 4

    return points


def fielding_points(player: Dict) -> int:
    """Compute fielding points: 10 points each for catch/stumping/run out.

    The player dict provides a key 'field' with the count of such events.
    """
    field_events = player.get("field", 0)
    return int(field_events) * 10
