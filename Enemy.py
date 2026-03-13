from Character import Character

class Enemy(Character):

    def __init__(self, maxHealth, attackPower, name = "Bart"):
        self.name = name
        super().__init__(self, maxHealth, attackPower)

