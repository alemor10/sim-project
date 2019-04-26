import random 
import csv 
import getshots
from  models import *



def shooting(player, team): 

    shot_location = random.choice(player.shot_distances)
    ##print ("shot location", shot_location)
    
    result = None 

    if shot_location <= 5:
        shot_made = True if random.randrange(100) <= player.less_than_5ft_shot_pct *100 else False
        ##print('pct', player.less_than_5ft_shot_pct)
        if shot_made:
            team.points +=2
            player.stats.points +=2
            player.stats.two_points +=1
            player.stats.two_point_attmpt +=1
            result = "make"
        else:
            player.stats.two_point_attmpt += 1 
            result = "miss"   
        ###print(result)

    elif shot_location <= 9 and shot_location > 5: 
        shot_made = True if random.randrange(100) <= player.less_than_5ft_to_9ft_shot_pct *100 else False
        if shot_made:
            team.points +=2
            player.stats.points +=2
            player.stats.two_points +=1
            player.stats.two_point_attmpt +=1
            result = "make"

        else:
            player.stats.two_point_attmpt += 1 
            result = "miss"  
    elif shot_location <= 14 and shot_location > 9: 
        shot_made = True if random.randrange(100) <= player.less_than_10ft_to_14ft_shot_pct *100 else False
        if shot_made:
            team.points +=2
            player.stats.points +=2
            player.stats.two_points +=1
            player.stats.two_point_attmpt +=1
            result = "make"

        else:
            player.stats.two_point_attmpt += 1 
            result = "miss" 
    elif shot_location <= 19 and shot_location > 14: 
        shot_made = True if random.randrange(100) <= player.less_than_15ft_to_19ft_shot_pct *100 else False
        if shot_made:
            team.points +=2
            player.stats.points +=2
            player.stats.two_points +=1
            player.stats.two_point_attmpt +=1
            result = "make"

        else:
            player.stats.two_point_attmpt += 1 
            result = "miss" 
    elif shot_location <= 24 and shot_location > 19: 
        shot_made = True if random.randrange(100) <= player.less_than_20ft_to_24ft_shot_pct *100 else False
        if shot_made and shot_location > 23:
            team.points +=3
            player.stats.points +=3
            player.stats.three_points +=1
            player.stats.three_point_attmpt +=1
            result = "make"
        if(shot_made and shot_location < 23):
            team.points +=2
            player.stats.points +=2
            player.stats.two_points +=1
            player.stats.two_point_attmpt +=1
            result = "make"
        if not shot_made and shot_location < 23:
            player.stats.two_point_attmpt += 1 
            result = "miss" 
        if not shot_made and shot_location >= 23:
            player.stats.three_point_attmpt += 1 
            result = "miss" 
    elif shot_location <= 29 and shot_location > 24: 
        shot_made = True if random.randrange(100) <= player.less_than_25ft_to_29ft_shot_pct *100 else False
        if shot_made:
            team.points +=3
            player.stats.points +=3
            player.stats.three_points +=1
            player.stats.three_point_attmpt +=1
            result = "make"

        else:
            player.stats.three_point_attmpt += 1 
            result = "miss"    

    elif shot_location <= 34 and shot_location > 29: 
        shot_made = True if random.randrange(100) <= player.less_than_30ft__to_34ft_shot_pct *100 else False
        if shot_made:
            team.points +=3
            player.stats.points +=3
            player.stats.three_points +=1
            player.stats.three_point_attmpt +=1
            result = "make"

        else:
            player.stats.three_point_attmpt += 1 
            result = "miss"    

    elif shot_location <= 39 and shot_location > 34: 
        shot_made = True if random.randrange(100) <= player.less_than_35ft_to_39ft_shot_pct *100 else False
        if shot_made:
            team.points +=3
            player.stats.points +=3
            player.stats.three_points +=1
            player.stats.three_point_attmpt +=1
            result = "make"

        else:
            player.stats.three_point_attmpt += 1 
            result = "miss"
    elif shot_location >= 40: 
        shot_made = True if random.randrange(100) <= player.less_than_40ftPlus_shot_pct *100 else False
        if shot_made:
            team.points +=3
            player.stats.points +=3
            player.stats.three_points +=1
            player.stats.three_point_attmpt +=1
            result = "make"

        else:
            player.stats.three_point_attmpt += 1 
            result = "miss"        
    return result

def freethrow_rebounding_sequence(player,possessing_team,non_possessing_team ):


    playerName1 = possessing_team.getRandomPlayer()
    playerName2 = non_possessing_team.getRandomPlayer()
    player1REB = possessing_team.teamlineup[playerName1].offensiveREBpct 
    player2Reb = non_possessing_team.teamlineup[playerName2].defensiveREBpct 
    if (player1REB > player2Reb): 
        possessing_team.teamlineup[playerName1].stats.offensive_reb +=1
        controlling_team = possessing_team
    else: 
        non_possessing_team.teamlineup[playerName2].stats.defensive_reb +=1
        controlling_team = non_possessing_team
    
    return controlling_team
   

def free_throw_sequence(player, possessing_team, non_possessing_team,event_type = None):
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
            possessing_team.points += 1
            player.stats.free_throw_attmpt += 1
            player.stats.free_throws += 1
            shots += 1
            if shots == total_shots:
                controlling_team = non_possessing_team
            else:
                pass
        else:
            player.stats.free_throw_attmpt += 1
            shots += 1
            if shots == total_shots:
                controlling_team = freethrow_rebounding_sequence(player, possessing_team, non_possessing_team)
            else:
                pass
    return controlling_team


def rebounding_sequence(possessing_team,non_possessing_team):
    
    playerName1 = possessing_team.getRandomPlayer()
    playerName2 = non_possessing_team.getRandomPlayer()
    player1REB = possessing_team.teamlineup[playerName1].offensiveREBpct + possessing_team.teamlineup[playerName1].REB
    player2Reb = non_possessing_team.teamlineup[playerName2].defensiveREBpct + non_possessing_team.teamlineup[playerName2].REB
    ##print ("offensive reb rate ",player1REB, "defensive reb rate ", player2Reb)


    if (player1REB > player2Reb): 
        possessing_team.teamlineup[playerName1].stats.offensive_reb +=1
        res = "oreb"
    else: 
        non_possessing_team.teamlineup[playerName2].stats.defensive_reb +=1
        res = "dreb"
  
    return res
 


def run_possession(possessing_team,non_possessing_team, clock):
    passes = 1
    ##print(possessing_team.name)
    player_name = possessing_team.getPlayerWithHighestUsgPercentage()
    possessing_player = possessing_team.teamlineup[player_name]
    
    res = None
    while passes < 5:
        use_val = random.uniform(0,1)
        if use_val < possessing_player.usage:
            res = shooting(possessing_player, possessing_team)
            break
        else:
            new_player_pos =possessing_team.getRandomPlayer()
            possessing_player = possessing_team.teamlineup[new_player_pos]
            passes += 1
    #hero ball time
    if passes == 5:
        use_val = random.uniform(0,1)
        if use_val < (possessing_player.usage):
            res = shooting(possessing_player, possessing_team)
        elif use_val < .50:
            #These are tough 50/50 calls in the lane from hero-baller charging down it
            foul_val = random.uniform(0,1)
            if foul_val < .40:
                possessing_player.stats.turnovers += 1
                possessing_player.stats.fouls += 1
                temp = possessing_team
                possessing_team = non_possessing_team
                non_possessing_team = temp
                possessing_team.fouls += 1
            else:
                possessing_team.opponent.fouls += 1
                if possessing_team.opponent.fouls > 4:
                    print("hello")
                    possessing_team = free_throw_sequence(possessing_player, possessing_team, non_possessing_team)
                else:
                    pass
        else:
            #turnover
            possessing_player.stats.turnovers += 1
            temp = possessing_team
            possessing_team = non_possessing_team
            non_possessing_team = temp
   #resolve the make or miss if there was a shot
    if res != None:
        if res == "make":
                temp = possessing_team
                possessing_team = non_possessing_team
                non_possessing_team = temp
        elif res == "miss":
            reb_res = rebounding_sequence(possessing_team, non_possessing_team)
            if reb_res == "oreb":
                pass
            elif reb_res == "dreb":
                temp = possessing_team
                possessing_team = non_possessing_team
                non_possessing_team = temp
            else:
                print ("Received unknown rebound resolution")
        else:
            print ("Received unknown resolution")
    #resolve the clock
    clock -= passes * 5
    return possessing_team,non_possessing_team, clock






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
            p.REB = float(r[5])
            p.defensiveREBpct = float(r[7])
            p.offensiveREBpct = float (r[6])
            p.less_than_5ft_shot_pct = float(r[8])
            p.less_than_5ft_to_9ft_shot_pct = float(r[9])
            p.less_than_10ft_to_14ft_shot_pct = float(r[10])
            p.less_than_15ft_to_19ft_shot_pct = float(r[11])
            p.less_than_20ft_to_24ft_shot_pct  = float(r[12])
            p.less_than_25ft_to_29ft_shot_pct  = float(r[13])
            p.less_than_30ft__to_34ft_shot_pct = float(r[14])
            p.less_than_35ft_to_39ft_shot_pct  = float(r[15])
            p.less_than_40ftPlus_shot_pct  = float(r[16])
            p.shot_distances = getshots.shot_loc(r[0])
            team.teamlineup[p.name] = p




def make_Team2players_from_data(team, playerID, path):    
    data = open(path, "r")
    reader = csv.reader(data)
    for r in reader:
        if  r[0]==playerID in r:
            p = Player()
            p.name,  p.position = r[1], r[2]
            p.usage = float(r[3])
            p.REB = float(r[5])
            p.defensiveREBpct = float(r[7])
            p.offensiveREBpct = float (r[6])
            p.less_than_5ft_shot_pct = float(r[8])
            p.less_than_5ft_to_9ft_shot_pct = float(r[9])
            p.less_than_10ft_to_14ft_shot_pct = float(r[10])
            p.less_than_15ft_to_19ft_shot_pct = float(r[11])
            p.less_than_20ft_to_24ft_shot_pct  = float(r[12])
            p.less_than_25ft_to_29ft_shot_pct  = float(r[13])
            p.less_than_30ft__to_34ft_shot_pct = float(r[14])
            p.less_than_35ft_to_39ft_shot_pct  = float(r[15])
            p.less_than_40ftPlus_shot_pct  = float(r[16])
            p.shot_distances = getshots.shot_loc(r[0])
            team.teamlineup[p.name] = p



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



possessing_team = None
non_possessing_team = None 
quarter = 1

#jump ball
jump_val = random.random()
if jump_val > 0.50:
    possessing_team = away
    non_possessing_team = home
else:
    possessing_team = home
    non_possessing_team= away

while quarter < 5:
    clock_seconds = 720
    while clock_seconds > 0:
        (possessing_team,non_possessing_team, clock_seconds) = run_possession(possessing_team,non_possessing_team, clock_seconds)
    home.fouls = 0
    away.fouls = 0
    home.quarter_points = home.points - home.running_points
    away.quarter_points = away.points - away.running_points
    home.running_points = home.points
    away.running_points = away.points
    home.points_in_a_quarter[quarter] = home.quarter_points
    away.points_in_a_quarter[quarter] = away.quarter_points
    quarter += 1



for t in teams:
    print (t.name, t.points, t.points_in_a_quarter)

for t in teams:
    for k in t.teamlineup.keys():
        p = t.teamlineup[k]
        print (p.name , p.stats.__dict__)
