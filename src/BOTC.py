class Townsfolk():
    types = {}
    with open("data/Townsfolks.csv") as file:
        for line in file:
            sline = line.strip().split(",")
            if sline[0] == "Role":
                pass
            else:
                role = sline[0]
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
        return f"Role: {self.type}"
        
class Outsider():
    types = {}
    with open("data/Outsiders.csv") as file:
        for line in file:
            sline = line.strip().split(",")
            if sline[0] == "Role":
                pass
            else:
                role = sline[0]
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
        return f"Role: {self.type}"
        
class Minion():
    types = {}
    with open("data/Minions.csv") as file:
        for line in file:
            sline = line.strip().split(",")
            if sline[0] == "Role":
                pass
            else:
                role = sline[0]
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
        return f"Role: {self.type}"
        
class Demon():
    types = {}
    with open("data/Demons.csv") as file:
        for line in file:
            sline = line.strip().split(",")
            if sline[0] == "Role":
                pass
            else:
                role = sline[0]
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
        return f"Role: {self.type}"
        
class Traveler():
    types = {}
    with open("data/Travelers.csv") as file:
        for line in file:
            sline = line.strip().split(",")
            if sline[0] == "Role":
                pass
            else:
                role = sline[0]
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
    def __init__(self, name:str, alignment:str, role:object) -> None:
        self.name = name
        self.alignment = alignment
        self.role = role
        self.alive = True
        self.deadvote = True
    
    def swap_alignment(self):
        if self.alignment == "Good":
            self.alignment = "Evil"
        else:
            self.alignment = "Good"

    def kill(self):
        self.alive = False

    def resurrect(self):
        self.alive = True

    def is_alive(self) -> bool:
        return self.alive
    
    def dead_vote(self):
        self.deadvote = False

    def has_vote(self) -> bool:
        if self.is_alive():
            return True
        else:
            return self.deadvote

    def __str__(self) -> str:
        return f"Player: {self.name} | {self.role.__str__()} | Alignment: {self.alignment} | Status: {'Alive' if self.is_alive() else 'Dead'} | DeadVote: {'Saved' if self.has_vote() else 'Used'}"

class Game():
    def __init__(self, playercount:int, players:list) -> None:
        pass

tf = Townsfolk("Washerwoman")
print(tf.type, tf.text)
p1 = Player("Logan", "Good", tf)
p1.kill()
p1.dead_vote()
print(p1)