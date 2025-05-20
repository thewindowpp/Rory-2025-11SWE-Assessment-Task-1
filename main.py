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
    print(f"Starting teams: {', '.join(teamslist)}")
    
def init_leaderboard():
    global leaderboard
    leaderboard = []

    global act_teams
    act_teams = teamslist.copy()

    for teamname in teamslist:
        team_stats = {
            "name": teamname,
            "wins": 0,
            "losses": 0,
            "points": 0,
            "Byes": 0
        }
        leaderboard.append(team_stats)


def rounds():
    global round_num
    round_num = 1

    while True:
        if len(act_teams) == 1:
            pass #Complete!!!!!!! Winner stuff

        if len(act_teams) % 2 == 0:
            pass #Complete!!!!!!! No bye
        elif len(act_teams) % 2 == 1:
            
            
            pass #COMPLETE!!!!! ASSIGN BYE
        else:
            print("Error occured, please contact creator")

print("Welcome to the knockout Tournament Tracker!")

teams()

init_leaderboard()
    

