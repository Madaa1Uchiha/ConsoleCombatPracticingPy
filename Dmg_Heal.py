from Player import Player


class Dmg_Heal():
   
    def isAlive(self, player):
        if player.health <= 0:
            player.health = 0

    def takeDmg(self, player, damage=10):
        player.health -= damage
        self.isAlive(player)

