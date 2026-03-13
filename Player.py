from Character import Character 

class Player(Character):


    def __init__(self, maxHealth, attackPower, name="Hero"):
        self.name = name
        super().__init__(self, maxHealth, attackPower)
