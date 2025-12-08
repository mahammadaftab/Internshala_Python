"""
Main script for Assignment 2: Determine Man of the Match (top performer)

This script imports scoring functions from `match_points` and computes total
points for five players provided in the problem statement. It prints individual
scores and the player with the highest points.
"""
from match_points import batting_points, bowling_points, fielding_points

# Players data provided in the assignment
p1 = {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0, 'balls': 119, 'field': 0}
p2 = {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4': 11, '6': 2, 'balls': 112, 'field': 0}
p3 = {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1}
p4 = {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0}
p5 = {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34, 'field': 0}

players = [p1, p2, p3, p4, p5]

# Compute scores and track top performer
scores = []

for p in players:
    if p.get('role') == 'bat':
        bscore = batting_points(p)
        fscore = fielding_points(p)
        total = bscore + fscore
        print({'name': p['name'], 'batscore': total})
        scores.append({'name': p['name'], 'score': total})
    else:
        bwscore = bowling_points(p)
        fscore = fielding_points(p)
        total = bwscore + fscore
        print({'name': p['name'], 'bowlscore': total})
        scores.append({'name': p['name'], 'score': total})

# Determine top performer
winner = max(scores, key=lambda x: x['score'])
print('\nMan of the Match: ', winner)
