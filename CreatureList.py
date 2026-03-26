from CreatureInfo import CreatureInfo
from Attacks import Attacks



class CreatureList: 
    def __init__(self):
        self.creatures = []
        self.creatures.append(CreatureInfo("A small, black horse with a white spot on its forehead, almost as if risen from the ashes giving it its fire type and name Ash steed.", "Ash Steed", 100, 2, 25, 10, "Fire"))
        self.creatures.append(CreatureInfo("A statured Bird a king of the water spearing fishes with its long beak, because of its time around water it has taken the typing of water over generations.", "Water Javelin", 50 , 3.2, 30, 15, "Water"))
        self.creatures.append(CreatureInfo("This creature that seems to be made of wood like a doll is actually a puppet to a creature of living vines giving it a grass type and the name of Wormvine.", "Wormvine", 80, 1.8, 15, 28, "Grass"))
        ashsteed_attack1 = Attacks("Flame Charge", "Fire", 5)
        ashsteed_attack2 = Attacks("Ember", "Fire", 5.8)
        self.creatures[0].attacks.extend([ashsteed_attack1, ashsteed_attack2])
        waterjavelin_attack1 = Attacks("Water Gun", "Water", 6)
        waterjavelin_attack2 = Attacks("Aqua Tail", "Water", 4.3)
        self.creatures[1].attacks.extend([waterjavelin_attack1, waterjavelin_attack2])
        wormvine_attack1 = Attacks("Vine Whip", "Grass", 3)
        wormvine_attack2 = Attacks("Razor Leaf", "Grass", 4.2)   
        self.creatures[2].attacks.extend([wormvine_attack1, wormvine_attack2])

