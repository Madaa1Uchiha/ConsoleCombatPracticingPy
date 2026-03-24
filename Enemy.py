from Character import Character

class Enemy(Character):
    def __init__(self, maxHealth=80, attackPower=10, name="Bart"):
        self.name = name
        super().__init__(maxHealth, attackPower)

