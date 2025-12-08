# Assignment 2 — Match Points Output

This file records the output produced by `assignment2_main.py` (scoring for Man of the Match).

## Command run

```powershell
cd "Assignments\assignment 2"
python assignment2_main.py
```

## Raw Printed Output

```
{'name': 'Virat Kohli', 'batscore': 83}
{'name': 'du Plessis', 'batscore': 94}
{'name': 'Bhuvneshwar Kumar', 'bowlscore': 20}
{'name': 'Yuzvendra Chahal', 'bowlscore': 24}
{'name': 'Kuldeep Yadav', 'bowlscore': 42}

Man of the Match:  {'name': 'du Plessis', 'score': 94}
```

## Tabular Summary (computed scores)

| Name                  | Role  | Bat/Bowl Score | Fielding Points | Total Points |
|-----------------------|-------|----------------|-----------------|--------------|
| Virat Kohli           | bat   | 83             | 0               | 83           |
| du Plessis            | bat   | 94             | 0               | 94           |
| Bhuvneshwar Kumar     | bowl  | 20             | 10              | 20           |
| Yuzvendra Chahal      | bowl  | 24             | 0               | 24           |
| Kuldeep Yadav         | bowl  | 42             | 0               | 42           |

> Man of the Match: **du Plessis** (94 points)


## Notes
- The table shows the printed `batscore` for batting players and `bowlscore` for bowlers — these values already include fielding points where applicable (the script adds fielding points to the player's total).  
- If you want a breakdown column-by-column (batting points, bowling points, and fielding points separately) I can update the script to print and store each component individually and regenerate this file.
