import os
import pandas as pd



csv_file = "Test.csv"
path = "./Test.csv"

# Convert XLSX into CSV

if os.path.exists(path) == False:

    xlsx_file = "Test.xlsx"

    read = pd.read_excel(xlsx_file)

    read.to_csv(csv_file, index=False)


# Convert CSV into array

df = pd.read_csv(csv_file)

all_players = df.values.tolist()



# Calculate posible players per team
player_number = len(all_players)

max_posible_players_per_team = int(player_number/2)

posible_players_per_team = []
for i in range(max_posible_players_per_team,1,-1):
    if player_number % i == 0:
        posible_players_per_team.append(int(player_number/i))



# Calculate posible teams

posible_teams = []
for i in range(2,max_posible_players_per_team+1):
    if player_number % i == 0:
        posible_teams.append(int(player_number/i))

#

player_number = len(all_players)

# Printout

print(f"Possible players per team: {posible_players_per_team}")
print(f"Possible teams: {posible_teams}")
print(all_players) 
print(player_number)


os.system("pause")