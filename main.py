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
    global teamslist
    teamslist = []

    global leaderboard
    leaderboard = {}

    print("Please input at least 4 teams, type 'done' to finish")
    
    while True:
        teamname = input(f"Enter Team {len(teamslist)+1}: ")
        if teamname.lower() == "done" and len(teamslist) >= 4:
            break
        elif teamname == "" :
            print("Please enter a valid team name, or type 'done' to finish entering teams")
        elif teamname in teamslist:
            print("Please enter unique team names, or type 'done' to finish entering teams")
        elif teamname == "done" and len(teamslist) < 4:
            print("Please enter atleast 4 teams")
        else:
            teamslist.append(teamname)
            
            team_stats = {
                "played": 0,
                "won": 0,
                "lost": 0,
                "for": 0,
                "against": 0
            }

            leaderboard[teamname] = team_stats
    print(f"Starting teams: {', '.join(teamslist)}")

    global act_teams
    act_teama = teamslist.copy()


def rounds():
    global round_num
    round_num = 1

    while True:
        if len(act_teams) == 1: #Winner
            print(*act_teams)

        if len(act_teams) % 2 == 0:
            pass #Complete!!!!!!! No bye
        elif len(act_teams) % 2 == 1:
            
            
            pass #COMPLETE!!!!! ASSIGN BYE
        else:
            print("Error occured, please contact creator")

print("Welcome to the knockout Tournament Tracker!")

teams()

print(leaderboard)
