#imports
import os
import random
import tabulate


def clear_console():
    # Clear console based on the operating system
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Unix/Linux/Mac

def teams():
    global teams_list
    teams_list = []

    global leaderboard
    leaderboard = {}

    print("Please input at least 4 teams, type 'done' to finish")
    
    while True:
        teamname = input(f"Enter Team {len(teams_list)+1}: ")
        if teamname.lower() == "done" and len(teams_list) >= 4:
            break
        elif teamname == "" :
            print("Please enter a valid team name, or type 'done' to finish entering teams")
        elif teamname in teams_list:
            print("Please enter unique team names, or type 'done' to finish entering teams")
        elif teamname == "done" and len(teams_list) < 4:
            print("Please enter at least 4 teams")
        else:
            teams_list.append(teamname)
            
            team_stats = {
                "played": 0,
                "won": 0,
                "lost": 0
            }

            leaderboard[teamname] = team_stats
    print(f"Starting teams: {', '.join(teams_list)}")

    global act_teams
    act_teams = teams_list.copy()

pairs = []
teams_with_byes = set()  # Track teams that have received a bye


def print_leaderboard():
    # Display leaderboard using tabulate, sorted by wins descending
    data = []
    for team in teams_list:
        stats = leaderboard[team]
        data.append([team, stats["played"], stats["won"], stats["lost"]])
    # Sort by wins (index 2) descending
    data.sort(key=lambda x: x[2], reverse=True)
    print(tabulate.tabulate(data, headers=["Team", "Played", "Won", "Lost"], tablefmt="pipe"))


def rounds():
    global round_num
    round_num = 1

    while True:
        clear_console()
        print_leaderboard()

        if len(act_teams) == 1: #Winner
            print("\n", *act_teams, "has won the tournament")
            break #Winner Winner

        print(f"\nRound {round_num}: ")

        # Work on a copy of act_teams for pairing
        local_teams = act_teams.copy()
        global pairs
        pairs = []

        # Assign bye if there's an odd number of teams
        bye_team = None
        if len(local_teams) % 2 == 1:
            # Eligible teams for bye: active teams without previous bye
            eligible_byes = [team for team in local_teams if team not in teams_with_byes]

            # If no eligible teams left, allow all active teams (reset byes)
            if not eligible_byes:
                eligible_byes = local_teams.copy()
                teams_with_byes.clear()  # Reset bye history

            bye_team = random.choice(eligible_byes)
            print(f"{bye_team} has been given a bye for this round and proceeds automatically.")
            teams_with_byes.add(bye_team)
            local_teams.remove(bye_team)

        # Shuffle teams to ensure random fair matchups
        random.shuffle(local_teams)

        # Generate pairings
        for i in range(0, len(local_teams), 2):
            team1 = local_teams[i]
            team2 = local_teams[i + 1]
            pairs.append((team1, team2))

        round_print()

        # Re-add the bye team to act_teams (if still active)
        if bye_team and bye_team not in act_teams:
            act_teams.append(bye_team)

        round_num += 1

def round_print():
    counter = 1
    for pair in pairs:
        print(f"Pair {counter} is {pair[0]} versus {pair[1]}")
        
        while True:
            try:
                team1_score = int(input(f"What did {pair[0]} score? "))
                team2_score = int(input(f"What did {pair[1]} score? "))
            except:
                print("Please input scores as integers.")
                continue

            if team1_score > team2_score:
                counter +=1
                print(f"{pair[0]} won the round")

                #Updating played
                leaderboard[pair[0]]["played"] += 1 ; leaderboard[pair[1]]["played"] += 1

                leaderboard[pair[0]]["won"] += 1 #Updating won
                leaderboard[pair[1]]["lost"] += 1 #Updating lost

                # Remove loser from active teams
                if pair[1] in act_teams:
                    act_teams.remove(pair[1])
                break
            elif team2_score > team1_score:
                counter +=1
                print(f"{pair[1]} won the round")

                #Updating played
                leaderboard[pair[0]]["played"] += 1 ; leaderboard[pair[1]]["played"] += 1

                leaderboard[pair[1]]["won"] += 1 #Updating won
                leaderboard[pair[0]]["lost"] += 1 #Updating lost

                # Remove loser from active teams
                if pair[0] in act_teams:
                    act_teams.remove(pair[0])
                break

            else:
                print("Draws are not allowed, please re-enter scores")


if __name__ == "__main__":
    print("Welcome to the knockout Tournament Tracker!")

    teams()

    rounds()
