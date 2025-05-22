#imports
import os
import random




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
            print("Please enter atleast 4 teams")
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
seen_teams = []


def teamrandom(): #Keeps matches easy easy
    return random.randint(0, len(act_teams) - 1)





def rounds():
    global round_num
    round_num = 1

    while True:

        if len(act_teams) == 1: #Winner
            print(*act_teams, " has won!")
            #TABLE TABLE TABLE TABLE TABLE TABLE TABLE TABLE 

            break #Winner Winner

        if len(act_teams) % 2 == 0:
            while len(pairs) < len(act_teams) / 2: #Generating pairings
                team1 = teamrandom()
                while team1 in seen_teams:
                    team1 = teamrandom()
                team2 = teamrandom()
                while team2 in seen_teams or team2 == team1:
                    team2 = teamrandom()
                seen_teams.append(team1) #Add teams to seen_teams so no repeats
                seen_teams.append(team2)
                pair = (act_teams[team1], act_teams[team2])
                pairs.append(pair)
            round_print()
            break
  
        elif len(act_teams) % 2 == 1:
            bye = random.sample(teams_list, 1)
            print(f"{bye} has been chosen as a bye for this round")
            
            pass #COMPLETE!!!!! ASSIGN BYE
        else:
            print("Error occured, please contact creator")

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
                print("Please input scores as intergers.")
                team1_score = int(input(f"What did {pair[0]} score? "))
                team2_score = int(input(f"What did {pair[1]} score? "))

            if team1_score > team2_score:
                counter +=1
                print(f"{pair[0]} won the round")

                #Updating played
                leaderboard[pair[0]]["played"] += 1 ; leaderboard[pair[1]]["played"] += 1

                leaderboard[pair[0]]["won"] += 1 #Updating won
                leaderboard[pair[1]]["lost"] += 1 #Updating lost

                act_teams.remove(pair[1]) #Remove losing team from active teams
                break
            elif team2_score > team1_score:
                counter +=1
                print(f"{pair[1]} won the round")

                #Updating played
                leaderboard[pair[0]]["played"] += 1 ; leaderboard[pair[1]]["played"] += 1

                leaderboard[pair[1]]["won"] += 1 #Updating won
                leaderboard[pair[0]]["lost"] += 1 #Updating lost
                act_teams.remove(pair[0]) #Remove losing team from active teams

                break

            else:
                print("Draws are not allowed, please re-enter scores")


print("Welcome to the knockout Tournament Tracker!")

teams()

rounds()
