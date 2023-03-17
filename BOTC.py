class Townsfolk():
    types = {"Washerwoman" : "You start knowing that 1 of 2 players is a particular Townsfolk.",
             "Librarian": "You start knowing that 1 of 2 players is a particular Outsider. (Or that zero are in play.)",
             "Investigator": "You start knowing that 1 of 2 players is a particular Minion.",
             "Chef": "You start knowing how many pairs of evil players there are.",
             "Empath": "Each night, you learn how many of your 2 alive neighbours are evil.",
             "Fortune Teller": "Each night, choose 2 players: you learn if either is a Demon. There is a good player that registers as a Demon to you."}
    def __init__(self, type) -> None:
        pass

class Outsider():
    types = []
    def __init__(self, type) -> None:
        pass

class Minion():
    types = []
    def __init__(self, type) -> None:
        pass

class Demon():
    types = []
    def __init__(self, type) -> None:
        pass

class Traveler():
    types = []
    def __init__(self, type) -> None:
        pass

class Player():
    def __init__(self, alignment, role:object) -> None:
        self.alignment = alignment
        self.role = role
        pass

class Game():
    def __init__(self, playercount:int, players:list) -> None:
        pass