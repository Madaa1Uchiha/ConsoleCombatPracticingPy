from CreatureInfo import CreatureInfo
from Attacks import Attacks

class Dmg_Heal():
    def isAlive(self, creature):
        if creature.health <= 0:
            creature.health = 0
    
    def TypeAdvantage(self, attack, target):
        if attack.type == "Fire" and target.type == "Grass":
            return 1.5
        elif attack.type == "Water" and target.type == "Fire":
            return 1.5
        elif attack.type == "Grass" and target.type == "Water":
            return 1.5
        elif attack.type == "Fire" and target.type == "Water":
            return 0.5
        elif attack.type == "Water" and target.type == "Grass":
            return 0.5
        elif attack.type == "Grass" and target.type == "Fire":
            return 0.5
        else:
            return 1
    def takeDmg(self, creature, attack, target):
        damage = (creature.attackPower * attack.power * self.TypeAdvantage(attack, target)) - target.defense
        if damage < 0:
            damage = 0
        target.health -= damage
        self.isAlive(target)
        return damage
