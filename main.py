team_roster= {}
# keys will be position
# values will be player name
class Player:
    def __init__(self, name=None,pos=None):
        self.name = name
        self.pos = pos
        
    # getter method
    def get_name(self):
        return self.name
    
    # setter method
    def set_name(self, x):
        self.name = x
        
    def get_pos(self):
        return self.pos
    
    def set_pos(self, y):
        self.pos = y
        
class Team:
    def __init__(self, team_name=None, league=None, url=None):
        self.team_name = team_name
        self.league = league
        self.url = url
    
    def get_team_name(self):
        return self.team_name
    
    def set_team_name(self, team_name):
        self.team_name = team_name
        
        
player = Player()
team = Team()

player.set_name('Christian McCaffrey')
player.set_pos('Running Back')
team.set_team_name('San Francisco 49ers')


print(player.get_name())
print(player.get_pos())
print(team.get_team_name())
# def add_player

# def del_player

# def edit_team

# def delete_team

