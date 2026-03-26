from Character import Character

class Enemy(Character):
    def __init__(self, name="Enemy", creature=None):
        self.name = name
        super().__init__(name, "Male", creature)

