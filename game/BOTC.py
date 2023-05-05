import json
import random
import pygame
import time

class Townsfolk():
    types = {}
    with open("data/Townsfolks.csv") as ofile:
        for line in ofile:
            sline = line.strip().split(",")
            if sline[0] == "Role":
                pass
            else:
                role = sline[0].lower()
                text = sline[1]
                types[role] = text
    def __init__(self, type) -> None:
        if type in self.types:
            self.type = type
            self.text = self.types[type]
        else:
            print("That character does not exist...")
            raise TypeError
    def __str__(self) -> str:
        return f"Role: {self.type[0].upper()+self.type[1:]}"
        
class Outsider():
    types = {}
    with open("data/Outsiders.csv") as ofile:
        for line in ofile:
            sline = line.strip().split(",")
            if sline[0] == "Role":
                pass
            else:
                role = sline[0].lower()
                text = sline[1]
                types[role] = text
    def __init__(self, type) -> None:
        if type in self.types:
            self.type = type
            self.text = self.types[type]
        else:
            print("That character does not exist...")
            raise TypeError
    def __str__(self) -> str:
        return f"Role: {self.type[0].upper()+self.type[1:]}"
        
class Minion():
    types = {}
    with open("data/Minions.csv") as ofile:
        for line in ofile:
            sline = line.strip().split(",")
            if sline[0] == "Role":
                pass
            else:
                role = sline[0].lower()
                text = sline[1]
                types[role] = text
    def __init__(self, type) -> None:
        if type in self.types:
            self.type = type
            self.text = self.types[type]
        else:
            print("That character does not exist...")
            raise TypeError
    def __str__(self) -> str:
        return f"Role: {self.type[0].upper()+self.type[1:]}"
        
class Demon():
    types = {}
    with open("data/Demons.csv") as ofile:
        for line in ofile:
            sline = line.strip().split(",")
            if sline[0] == "Role":
                pass
            else:
                role = sline[0].lower()
                text = sline[1]
                types[role] = text
    def __init__(self, type) -> None:
        if type in self.types:
            self.type = type
            self.text = self.types[type]
        else:
            print("That character does not exist...")
            raise TypeError
    def __str__(self) -> str:
        return f"Role: {self.type[0].upper()+self.type[1:]}"
        
class Traveler():
    types = {}
    with open("data/Travelers.csv") as ofile:
        for line in ofile:
            sline = line.strip().split(",")
            if sline[0] == "Role":
                pass
            else:
                role = sline[0].lower()
                text = sline[1]
                types[role] = text
    def __init__(self, type) -> None:
        if type in self.types:
            self.type = type
            self.text = self.types[type]
        else:
            print("That character does not exist...")
            raise TypeError
        
class Player():
    def __init__(self, name:str, alignment:str, role, drunk_role:str) -> None:
        self.name = name
        self.alignment = alignment
        self.role = role
        self.alive = True
        self.deadvote = True
        self.poisoned = False
        self.mad = False
        self.mad_role = None
        drunk = False if role.type != "drunk" else True
        self.displayed_role = drunk_role if drunk else role
    
    def swap_alignment(self):
        if self.alignment == "Good":
            self.alignment = "Evil"
        else:
            self.alignment = "Good"

    def change_role(self, new_role):
        self.role = new_role

    def kill(self):
        self.alive = False

    def resurrect(self):
        self.alive = True

    def is_alive(self) -> bool:
        return self.alive
    
    def dead_vote(self):
        self.deadvote = False

    def make_mad(self, mad_role = None):
        self.mad = True
        self.mad_role = mad_role

    def display_mad_role(self):
        print(self.mad_role)

    def is_mad(self):
        return self.mad

    def has_vote(self) -> bool:
        if self.is_alive():
            return True
        else:
            return self.deadvote
        
    def is_poisoned(self) -> bool:
        return self.poisoned
    
    def wake_up(self, game, first=False):
        print("Wake up " + self.__str__())
        players:list = game.name_list
        alive_players = []
        demon_list = []
        minion_list = []
        for name in players:
            if game.player_map[name].is_alive():
                alive_players.append(name)
            if game.player_map[name].role.type in Demon.types:
                demon_list.append(game.player_map[name])
            elif game.player_map[name].role.type in Minion.types:
                minion_list.append(game.player_map[name])
        if(first):
            if(self.role.type in Demon.types):
                print("These are your minions:")
                for minion in minion_list:
                    print(minion.name)
            elif(self.role.type in Minion.types):
                print("This is your demon:")
                print(demon_list[0].name)
        else:
            if "choose a player" in self.role.text and "*" not in self.role.text:
                choice = input(f"Choose a player: {set(players)} ")
                print(self.name + " chose " + choice)
            elif "choose 2 players" in self.role.text and "*" not in self.role.text:
                choice_1 = input(f"Choose a player: {set(players)} ")
                choice_2 = input(f"Choose a player: {set(players).difference(choice_1)} ")
                print(self.name + " chose " + choice_1 + " and " + choice_2)
            elif "choose an alive player" in self.role.text and "*" not in self.role.text:
                choice = input(f"Choose an alive player: {set(alive_players)} ")
                print(self.name + " chose " + choice)
            elif "choose 2 alive players" in self.role.text and "*" not in self.role.text:
                choice_1 = input(f"Choose a player: {set(alive_players).difference(self.name)} ")
                choice_2 = input(f"Choose a player: {set(alive_players).difference(self.name).difference(choice_1)} ")
                print(self.name + " chose " + choice_1 + " and " + choice_2)                

    def __str__(self) -> str:
        return f"Player: {self.name} | {self.role.__str__()} | Alignment: {self.alignment} | Status: {'Alive' if self.is_alive() else 'Dead'} | DeadVote: {'Saved' if self.has_vote() else 'Used'}"


class StoryTeller():
    def __init__(self, game) -> None:
        pass


class Game():
    team_map = {  # player_count: (town, outsider, minion, demon)
                5: (3, 0, 1, 1),
                6: (3, 1, 1, 1),
                7: (5, 0, 1, 1),
                8: (5, 1, 1 ,1),
                9: (5, 2, 1, 1),
                10: (7, 0, 2, 1),
                11: (7, 1, 2, 1),
                12: (7, 2, 2, 1),
                13: (9, 0, 3, 1),
                14: (9, 1, 3, 1),
                15: (9, 2, 3, 1)}
    def __init__(self, players:list, script:str) -> None:
        roles_list = []
        with open(script) as file:
            loaded = json.load(file)
            for i in loaded:
                if i == loaded[0]:
                    pass
                else:
                    roles_list.append(i["id"])
        self.first_night_order = []
        self.other_night_order = []
        with open("../nightsheet.json") as file:
            orders = json.load(file)
            for i in orders["firstnight"]:
                if i in roles_list or i == "MINION_INFO" or i == "DEMON_INFO" or i == "DAWN":
                    self.first_night_order.append(i) 
            for i in orders["othernight"] or i == "DUSK" or i == "DAWN":
                if i in roles_list:
                    self.other_night_order.append(i)
        self.script = roles_list
        self.name_list = []
        for player in players:
            self.name_list.append(player)
        self.player_list = []
        role_list = []
        self.player_count = len(players)
        self.count_tuple = self.team_map[self.player_count]
        self.town_count = self.count_tuple[0]
        self.outsider_count = self.count_tuple[1]
        self.minion_count = self.count_tuple[2]
        self.demon_count = self.count_tuple[3]
        role_list.append(input("Enter your demon (must be all lowercase e.g: fang_gu): "))
        if "fang_gu" in role_list:
            self.outsider_count+=1
            self.town_count-=1
        elif "vigormortis" in role_list and self.outsider_count>0:
            self.outsider_count-=1
            self.town_count+=1
        for i in range(self.minion_count):
            role_list.append(input("Enter a new Minion (no repeats and must be lowercase e.g: pit-hag or evil_twin): "))
        if "baron" in role_list and self.outsider_count>0:
            self.outsider_count+=2
            self.town_count-=2
        if "godfather" in role_list:
            choice = input("Choose to add or subtract an outsider (+ or -): ")
            if choice == "+":
                self.outsider_count+=1
                self.town_count-=1
            elif choice == "-" and self.outsider_count>0:
                self.outsider_count-=1
                self.town_count+=1
            else:
                print("I'll give you one more chance!")
                choice = input("you MUST enter either '+' or '-'")
                if choice == "+":
                    self.outsider_count+=1
                    self.town_count-=1
                elif choice == "-" and self.outsider_count>0:
                    self.outsider_count-=1
                    self.town_count+=1
                else:
                    print("You suck")
                    raise ValueError
        for i in range(self.town_count):
            role_list.append(input("Enter a new Townsfolk character (no repeats and must be lowercase e.g: snake_charmer): "))
        for i in range(self.outsider_count):
            role_list.append(input("Enter a new Outsider character (no repeats and must be lowercase e.g: sweetheart): "))
        if "drunk" in role_list:
            drunk_character = input("Enter townsfolk role to give the drunk (must be lowercase and not in play): ")
        else: 
            drunk_character = None
        self.active_roles = []
        self.role_map = {}
        self.player_map = {}
        for i in role_list:
            self.active_roles.append(i)
        while len(role_list) > 0:
            i = random.randint(0, len(role_list)-1)
            role = role_list[i]
            role_list.remove(role)
            j = random.randint(0, len(players)-1)
            self.role_map[role] = players[j]
            if role in Townsfolk.types:
                self.player_map[players[j]] = Player(players[j], "Good", Townsfolk(role), drunk_character)
                self.player_list.append(self.player_map[players[j]])    
                print("town added")
            elif role in Outsider.types:
                self.player_map[players[j]] = Player(players[j], "Good", Outsider(role), drunk_character)
                self.player_list.append(self.player_map[players[j]])    
                print("outsider added")
            elif role in Minion.types:
                self.player_map[players[j]] = Player(players[j], "Evil", Minion(role), drunk_character)
                self.player_list.append(self.player_map[players[j]])    
                print("minion added")
            elif role in Demon.types:
                self.player_map[players[j]] = Player(players[j], "Evil", Demon(role), drunk_character)
                self.player_list.append(self.player_map[players[j]])    
                print("demon added")
            players.remove(players[j])
    
    def night_1(self):
        self.night = 1
        print("---Night 1---")
        for role in self.first_night_order:
            if role in self.active_roles:
                player = self.role_map[role]
                self.player_map[player].wake_up(self)
            elif role == "MINION_INFO":
                for r in self.active_roles:
                    if r in Minion.types:
                        player = self.role_map[r]
                        self.player_map[player].wake_up(self, True)
            elif role == "DEMON_INFO":
                for r in self.active_roles:
                    if r in Demon.types:
                        player = self.role_map[r]
                        self.player_map[player].wake_up(self, True)
                

    def play_day(self):
        t = 60 * int(input("How long is the day? (enter int in minutes)"))
        time.sleep(t)
        self.nominations()


    def nominations(self):
        if "juggler" in self.script or "gossip" in self.script:
            print("Now accepting juggles / public statements:")
            time.sleep(80)
        print("Now accepting nominations:")
        # Code input for nominations and votes
        print("Now beginning the night: ")
        self.other_nights()

    def other_nights(self):
        self.night+=1
        print(f"---Night {self.night}---")
        for role in self.other_night_order:
            if role in self.active_roles:
                player = self.role_map[role]
                if self.player_map[player].is_alive():
                    self.player_map[player].wake_up(self)

def main():
    # When players join the game, they need to fill out an entry box with their name, which will be added
    # to a list of players which will be used to randomize roles
    player_list = []
    while True: # this is just a placeholder to allow me to play locally (eventually put on some website idk)
        player_name = input("Enter your name: ")
        if player_name == "":
            break
        else:
            player_list.append(player_name)
    game = Game(player_list, "../scripts/Sects and Violets.json")
    
    for player in game.player_list:
        print(player)

def test():
        players = ["Logan", "Jason", "Ada", "Ata", "Joe", "Matt", "Emma", "Jeremy", "Darwin", "Dani", "Zach"]
        game = Game(players, "../scripts/Sects and Violets.json")
        game.night_1()

if __name__ == "__main__":
    #main()
    test()
