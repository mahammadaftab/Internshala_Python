# Fantasy Cricket Game Database Design

## Tables

### 1. match
Stores player performance data for matches.

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| Player      | TEXT      | Player name |
| Scored      | INTEGER   | Runs scored |
| Faced       | INTEGER   | Balls faced |
| Fours       | INTEGER   | Number of fours hit |
| Sixes       | INTEGER   | Number of sixes hit |
| Bowled      | INTEGER   | Balls bowled |
| Maiden      | INTEGER   | Maiden overs bowled |
| Given       | INTEGER   | Runs given |
| Wkts        | INTEGER   | Wickets taken |
| Catches     | INTEGER   | Catches taken |
| Stumping    | INTEGER   | Stumpings done |
| RO          | INTEGER   | Run outs done |

### 2. stats
Stores player statistics.

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| player      | TEXT      | Player name |
| matches     | INTEGER   | Matches played |
| runs        | INTEGER   | Total runs scored |
| 100s        | INTEGER   | Hundreds scored |
| 50s         | INTEGER   | Fifties scored |
| value       | INTEGER   | Player value |
| ctg         | TEXT      | Player category (BAT, BOW, AR, WK) |

### 3. teams
Stores fantasy cricket teams.

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| name        | TEXT      | Team name |
| players     | TEXT      | Comma-separated list of players |
| value       | INTEGER   | Total team value |