import random
import os
import time
import pandas as pd

def player_choose():
    # Randomly chooses a player from 'all_players[]', removes player from 'all_players[]'
    # Returns the chosen player's name
    player_chosen = random.choice(all_players)
    all_players.remove(player_chosen)
    return player_chosen

def get_valid_integer(prompt):
    # Makes sure input is a valid integer
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def clear():
    # Clear terminal screen
    # Windows: 'cls', Linux/macOS: 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')



#############
# MAIN CODE #
#############

# Convert XLSX into CSV

csv_file = "file.csv"
path = "./file.csv"

for file in os.listdir():
    if file.endswith('.xlsx') or file.endswith('.xls'):
        xlsx_file = os.path.abspath(file)

read = pd.read_excel(xlsx_file)

read.to_csv(csv_file, index=False)


# Convert CSV into array

df = pd.read_csv(csv_file)

all_players = df.values.tolist()

# Player variables

player_number = len(all_players)

max_posible_players_per_team = int(player_number/2)


# Calculate posible players per team

posible_players_per_team = []
for i in range(max_posible_players_per_team,1,-1):
    if player_number % i == 0:
        posible_players_per_team.append(int(player_number/i))


# Calculate posible teams

posible_teams = []
for i in range(2,max_posible_players_per_team+1):
    if player_number % i == 0:
        posible_teams.append(int(player_number/i))


# Printout


# Welcome message
print("-" * 50)
print("WELCOME TO THE MOTHERFUCKING TEAM GENERATOR RNG")
print("-" * 50)
print("\n")
os.system("pause") # Wait for user to press ENTER


while True:

    clear()

    print(f"There are {player_number} players\n")

    print("-" * 20)
    print("1. Input total teams")
    print("2. Input players per team")
    print("-" * 20)

    choice = int(get_valid_integer(""))

    # Input total teams
    if choice == 1: 
        while True:
            clear()
            print(f"These are the amount of teams you can do: {posible_teams}")
            team_number = int(get_valid_integer(""))
            if team_number in posible_teams:
                players_per_team = int(player_number/team_number)
                break
            else:
                print("Invalid number")
                time.sleep(2)
                continue
        break

    # Input players per teams
    elif choice == 2:   
        while True:
            clear()
            print(f"These are the amount of players you can add to a team: {posible_players_per_team}")
            players_per_team = int(get_valid_integer(""))
            if players_per_team in posible_players_per_team:
                team_number = int(player_number/players_per_team)
                break
            else:
                print("Invalid number")
                time.sleep(2)
                continue
        break

    # Invalid number
    else:
        print("Please choose between options 1 or 2")
        continue


# List to store all teams
all_teams = [] 


# Loop to assign players to teams
for i in range(0,team_number):
    team = [] # Create list for team
    for j in range(0,players_per_team):
        chosen_player = player_choose() 
        team.append(chosen_player) # Add chosen_player to the team

    all_teams.append(team) # Add the team to the 'all_teams' list


##########
# OUTPUT #
##########

clear()

# Output each team and its players
for i in range(0,team_number):
    print(f"\nTeam {i+1}")
    print("-" * 10)
    for j in range(0,players_per_team):
        print(f"- {all_teams[i][j][0]}") # Print each player on the team

print("\n")
os.system("pause")

