from BOTC import *

def demon_logic(game: Game, player: Player):
    if player.role.type == "vortox":
        pass
    pass

def town_logic(game: Game, player: Player):
    pass

def outsider_logic(game: Game, player: Player):
    pass

def minion_logic(game: Game, player: Player):
    pass

def traveler_logic(game: Game, player: Player):
    pass

def run_logic(game: Game, player: Player):
    if(player.role == Townsfolk):
        town_logic()
    elif(player.role == Outsider):
        outsider_logic()
    elif(player.role == Minion):
        minion_logic()
    elif(player.role == Demon):
        demon_logic()
    elif(player.role == Traveler):
        traveler_logic()
    pass