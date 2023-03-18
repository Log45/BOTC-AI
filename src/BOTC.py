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
    def __init__(self, alignment, role:object) -> None:
        self.alignment = alignment
        self.role = role
        pass

class Game():
    def __init__(self, playercount:int, players:list) -> None:
        pass

tf = Townsfolk("Washerwoman")
print(tf.type, tf.text)