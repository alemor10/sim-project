import random 
import csv 


from models import *

pos_to_player = {1: "player1", 2: "player2", 3: "player3", 4: "player4", 5: "player5"}
pos_to_num = {"player1": 1, "player2": 2, "player3": 3, "player4": 4, "player5": 5}


def shooting(player, team): 
    shot_type_value = 0
    shot_chance_value = 0 
    
    result = None 

    if player.three_chance > shot_type_value:
        if player.three_point_pct > shot_chance_value:
            team.points += 3
            player.stats.points +=3
            player.stats.three_points +=1
            player.stats.three_point_attmpt +=1
            ## we could out put play by play here
            results = "make"
        else:
            player.stats.three_point_attmpt +=1
            results = "miss"


    else: 
        if player.two_point_pct > shot_chance_value:
            team.points +=2
            player.stats.points +=2
            player.stats.two_points +=1
            player.stats.two_point_attmpt +=1
            result = "make"

        else:
            player.stats.two_point_attmpt += 1 
            result = "miss"   

    return result

def freethrow_rebounding_sequence(player, team):
    rebound_val = round(random.random()*100)
    rebound_range = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
    player_num = pos_to_num[player.position]
    offensive_rebound_range = rebound_range.remove(player_num)
    if rebound_val < 14:
        rebounder = random.choice(offensive_rebound_range)
        rebounding_pos = pos_to_player[rebounder]
        team.teamlineup[rebounding_pos].stats.oreb += 1
        controlling_team = team
    else:
        rebounder = random.choice(rebound_range)
        rebounding_pos = pos_to_player[rebounder]
        team.opponent.teamlineup[rebounding_pos].stats.dreb += 1
        controlling_team = team.opponent
    return controlling_team

def free_throw_sequence(player, team, event_type = None):
    shots = 0
    if event_type == "2pt":
        total_shots = 2
    elif event_type == "3pt":
        total_shots = 3
    elif event_type == "and_one":
        total_shots = 1
    else:
        total_shots = 2
    while total_shots > shots:
        shot_chance_val = round(random.random()*100)
        if shot_chance_val > player.freethrow_pct:
            team.points += 1
            player.stats.free_throw_attmpt += 1
            player.stats.free_throws += 1
            shots += 1
            if shots == total_shots:
                controlling_team = team.opponent
            else:
                pass
        else:
            player.stats.free_throw_attmpt += 1
            shots += 1
            if shots == total_shots:
                controlling_team = freethrow_rebounding_sequence(player, team)
            else:
                pass
    return controlling_team


def rebounding_sequence(team):
    rebound_val = round(random.random()*100)
    #this is a little schematic to weight rebounding to right pos
    rebound_range = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
    rebounder = random.choice(rebound_range)
    rebounding_pos = pos_to_player[rebounder]
    if rebound_val < 26:
        team.teamlineup[rebounding_pos].stats.oreb += 1
        res = "oreb"
    else:
        team.opponent.teamlineup[rebounding_pos].stats.dreb += 1
        res = "dreb"
    return res




    #########################sim starting point 


    ### make teams 

    ### hard coded players 

### hard coded team1
## 2019 toronto raptors 
team1PF= "1627783"
team1SF = "202695"
team1C = "201188"
team1PG = "200768"
team1SG = "201980"

### hard coded team2
team2PF= "200755" ## G
team2SF = "202699" ## F
team2C = "203954" ## 
team2PG = "1627732"
team2SG = "202710"



home = Team("Team 1")
away = Team("Team 2")
home.opponent = away
away.opponent = home
teams = [home, away]

#make players
def make_Team1players_from_data(team,playerID, path):    
    data = open(path, "r")
    reader = csv.reader(data)
    for r in reader:
        if  r[0]==playerID in r:
            p = Player()
            p.name, p.position = r[1], r[2]
            p.usage = float(r[3])
            print (p.position)
            team.teamlineup[p.position] = p
            print (team.teamlineup)




def make_Team2players_from_data(team, playerID, path):    
    data = open(path, "r")
    reader = csv.reader(data)
    for r in reader:
        if  r[0]==playerID in r:
            p = Player()
            p.name,  p.position = r[1], r[2]
            p.usage = float(r[3])
            team.teamlineup[p.position] = p

make_Team1players_from_data(home ,team1PF, "player_data.csv")
make_Team1players_from_data(home, team1SF, "player_data.csv")
make_Team1players_from_data(home,team1C, "player_data.csv")
make_Team1players_from_data(home,team1PG, "player_data.csv")
make_Team1players_from_data(home, team1SG, "player_data.csv")


make_Team2players_from_data(away,team2PF, "player_data.csv")
make_Team2players_from_data(away, team2SF, "player_data.csv")
make_Team2players_from_data(away, team2C, "player_data.csv")
make_Team2players_from_data(away, team2PG, "player_data.csv")
make_Team2players_from_data(away, team2SG, "player_data.csv")

#print home.lineup
#print away.lineup

possessing_team = None
quarter = 1

#jump ball
jump_val = random.random()
if jump_val > 0.50:
    possessing_team = away
else:
    possessing_team = home



for t in teams:
    print (t.name, t.points, t.points_in_a_quarter)

for t in teams:
    for k in t.teamlineup.keys():
        p = t.teamlineup[k]
        print (p.name , p.stats.__dict__)