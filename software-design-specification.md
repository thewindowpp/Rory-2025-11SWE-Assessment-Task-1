
# Software Requirements Specification (SRS)

**Project title:** Knockout Tournament Tracker with Scores and Leaderboard  
**Course:** Year 11 Software Engineering  
**Version:** 2.2  
**Prepared by:** [Teacher’s Name]  
**Date:** [Insert date]

---

## 1. Purpose

This Python project enables users to manage a knockout tournament dynamically. It supports any number of teams (minimum 4), including non-power-of-2 team counts with automatic bye assignment. Users input team names, record match results (with scores), and the program tracks tournament progression and updates a detailed leaderboard after each round, culminating in the declaration of a champion.

## 2. Functional requirements

The Knockout Tournament Tracker must:

- Allow the user to input any number of teams (minimum 4) for the tournament.
- Validate the team count and prompt the user again if fewer than 4 teams are entered.
- Accept team names for all teams.
- Automatically generate matches for each round, pairing teams.
- If the number of teams is not a power of 2, assign byes so that the tournament can progress correctly.
- For each match:
    - Prompt the user to enter the match result, including scores for both teams.
    - Automatically determine the winner based on scores.
- Update a leaderboard after each round, displaying:
    - Team name
    - Matches played
    - Wins
    - Losses
    - Total goals for and against
- Progress winners (and bye teams) to the next round automatically.
- Continue until 1 team remains and declare the champion.
- Provide clear prompts and robust error handling throughout.

## 3. Data flow diagram (DFD) adn Sturcture Chart

[DFD and Structure Chart](https://www.figma.com/board/WNywN4KmVRiXUZ07huRDob/2025-11SWE-AT1?node-id=0-1&t=uBabRc9YETND8BG5-1)

*Note: Students must edit the structure chart to show data passing between functions, using arrows to indicate flags, parameters, and control variables.*

## 4. Data dictionary

| Variable Name  | Data Type        | Description                                             | Example                                            |
|----------------|------------------|---------------------------------------------------------|----------------------------------------------------|
| teams          | List of strings  | List of current team names in the tournament            | ["Alpha", "Bravo", "Echo"]                          |
| matches        | List of tuples   | List of matches in the current round                    | [("Alpha", "Bravo"), ("Charlie", "Delta")]          |
| bye_teams      | List of strings  | Teams receiving byes in the current round               | ["Echo"]                                           |
| leaderboard    | Dictionary       | Tracks stats for each team                              | {"Alpha": {"played": 1, "won": 1, "lost": 0, "for": 3, "against": 1}} |
| winners        | List of strings  | List of match winners for the current round             | ["Alpha", "Echo"]                                   |
| num_teams      | Integer          | Total number of teams entered                           | 6                                                  |
| round_number   | Integer          | The current round number                                | 1                                                  |
| winner         | String           | The name of the tournament champion                     | "Alpha"                                            |

## 5. Pseudocode

### Main program:

```
BEGIN TournamentTracker
    Display welcome message

    num_teams = InputNumberOfTeams()
    teams = InputTeamNames(num_teams)

    leaderboard = InitialiseLeaderboard(teams)

    round_number = 1

    WHILE len(teams) > 1:
        Display "Round {round_number} starting"

        IF len(teams) is not power of 2:
            bye_teams = AssignByes(teams)
            Display bye_teams get a bye
        ELSE:
            bye_teams = []

        matches = GenerateMatches(teams EXCLUDING bye_teams)

        winners = []
        FOR each match in matches:
            Display match details
            Input scores for both teams
            Determine winner
            UpdateLeaderboard(winner, loser, scores)
            Add winner to winners

        teams = winners + bye_teams

        DisplayLeaderboard(leaderboard)

        round_number += 1

    DisplayChampion(teams[0])
END
```

### InitialiseLeaderboard function:

```
FUNCTION InitialiseLeaderboard(teams)
    leaderboard = empty dictionary
    FOR team in teams:
        leaderboard[team] = {"played": 0, "won": 0, "lost": 0, "for": 0, "against": 0}
    RETURN leaderboard
END
```

### RecordMatchResults function:

```
FOR each match (team1, team2):
    Prompt for score_team1 and score_team2
    IF score_team1 > score_team2:
        winner = team1
        loser = team2
    ELSE IF score_team2 > score_team1:
        winner = team2
        loser = team1
    ELSE:
        Display "No draws allowed, re-enter scores"
        Repeat input
    UpdateLeaderboard(winner, loser, scores)
    Add winner to winners list
```

### UpdateLeaderboard function:
```
INCREMENT "played" for both teams by 1
INCREMENT "won" for winner by 1
INCREMENT "lost" for loser by 1
ADD score to "for" and "against" for both teams appropriately
```
## 6. Validation rules

- Minimum 4 teams required.
- Team names must be unique and non-empty.
- Match scores must be non-negative integers.
- No draws allowed: prompt again if scores are equal.
- Winner must be determined based on entered scores.

## 7. Error handling

- Invalid team count (less than 4): prompt again.
- Duplicate or blank team name: prompt again.
- Invalid scores (negative or non-numeric): prompt again.
- Draw result: prompt again (no draws allowed).

## 8. Example run (6 teams)

- User enters 6 teams: Alpha, Bravo, Charlie, Delta, Echo, Foxtrot.

**Round 1:**

- Bye: Foxtrot
- Matches:
    - Alpha vs Bravo
    - Charlie vs Delta
    - Echo vs Foxtrot (if applicable)

**User inputs:**

- Alpha 3 – 1 Bravo
- Charlie 2 – 0 Delta
- Echo 1 – 0 Foxtrot

**Leaderboard after Round 1:**

| Team     | Played | Won | Lost | For | Against |
|----------|--------|-----|-------|------|----------|
| Alpha    | 1      | 1   | 0     | 3    | 1        |
| Bravo    | 1      | 0   | 1     | 1    | 3        |
| Charlie  | 1      | 1   | 0     | 2    | 0        |
| Delta    | 1      | 0   | 1     | 0    | 2        |
| Echo     | 1      | 1   | 0     | 1    | 0        |
| Foxtrot  | 1      | 0   | 1     | 0    | 1        |

## 9. Notes for implementation

- The leaderboard only includes teams that have played matches.
- Byes do not increment matches played or other stats.
- The leaderboard is updated and displayed after each round.
- Code should be fully modularised to reflect the structure chart.
- Use `random.sample()` or similar to assign byes randomly when needed.

---

*Refer to the [Figma diagrams for the Level 0 DFD and initial Structure Chart](https://www.figma.com/board/WNywN4KmVRiXUZ07huRDob/2025-11SWE-AT1?node-id=0-1&t=uBabRc9YETND8BG5-1)].*
