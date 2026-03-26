from Character import Character 

class Player(Character):
    def __init__(self, name="Player", gender="Male", creature=None):
        self.name = name
        self.gender = gender
        self.creature = creature
        super().__init__(name, gender, creature)