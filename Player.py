from Character import Character 

class Player(Character):
    def __init__(self, maxHealth=100, attackPower=14, name="Hero"):
        self.name = name
        super().__init__(maxHealth, attackPower)