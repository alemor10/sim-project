import random 


class Team: 

    def __init__(self,name):
        self.name = name 
        self.teamlineup = {"F":None, "F": None, "G":None , "G":None ,"C":None ,"C":None ,"G-F":None, "G-F":None, "F-C":None, "F-C":None, "C-F":None, "C-F":None , "F-C":None, "F-C":None ,"F-G":None , "F-G": None  }
        self.points = 0
        self.running_points = 0
        self.fouls = 0
        self.points_in_a_quarter = {}


class GameStats: 
    def __init__(self):
        self.points = 0 
        self.three_point_attmpt = 0 
        self.three_points = 0
        self.two_point_attmpt = 0
        self.two_points = 0 
        self.turnovers = 0 
        self.fouls = 0
        self.free_throw_attmpt = 0 
        self.free_throws =0
        self.offensive_reb = 0 
        self.defensive_reb = 0 
        self.blocks  = 0 
        self.steals = 0 

        def total_reb(self):
            self.total_reb = self.offensive_reb + self.defensive_reb



class Player:

    def __init__(self):
        self.name = None
        self.position = None
        self.usage = 0.0
        self.less_than_5ft_shot_pct  = 0.0
        self.less_than_5ft_to_9ft_shot_pct  = 0.0
        self.less_than_10ft_to_14ft_shot_pct  = 0.0
        self.less_than_15ft_to_19ft_shot_pct  = 0.0
        self.less_than_20ft_to_24ft_shot_pct  = 0.0
        self.less_than_25ft_to_29ft_shot_pct  = 0.0
        self.less_than_30ft__to_34ft_shot_pct = 0.0
        self.less_than_35ft_to_39ft_shot_pct  = 0.0
        self.less_than_40ftPlus_shot_pct  = 0.0
        self.two_point_pct = 0.0
        self.three_chance = 0.0
        self.freethrow_pct = 0.0
        self.stats = GameStats()