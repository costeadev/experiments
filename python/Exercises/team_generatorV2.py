import random, os, time

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

# Welcome message
print("WELCOME TO THE MOTHERFUCKING TEAM GENERATOR RNG")
print("-" * 20)
os.system("pause") # Wait for user to press ENTER



################
# PLAYER INPUT #
################

# List to store all player's names
all_players = [] 

# Loop to get input about players
while True:
    clear()

    player_number = int(get_valid_integer("How many players?: "))
    print("\n")

    # Input validation
    if player_number < 4:
        print("The number of players must be at least 4")
    elif player_number % 2 != 0:
        print("The number of players must be even")
    else:
        break # Valid input, stop loop


for i in range(0,player_number):
    player = input(f"Player {i+1} name: ")
    all_players.append(player)


##############
# TEAM INPUT #
##############


while True:

    clear()

    team_number = int(get_valid_integer("How many teams?: "))

    # Validate the number of teams input
    if (team_number * 2 > player_number):
        clear()
        print("There must be at least 2 players per team\n")
        time.sleep(3)
    elif (team_number <= 1):
        clear()
        print("The must be at least 2 teams\n")
        time.sleep(3)
    else:
        break

players_per_team = int(player_number / team_number)

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
        print(f"- {all_teams[i][j]}") # Print each player on the team


print("\n")
os.system("pause")

