from Player import Player
from Enemy import Enemy
from Dmg_Heal import Dmg_Heal
import random

class Program():

    def main():
        hero = Player()
        enemy = Enemy()
        dmg = Dmg_Heal()
        battle = False

        print("Player stats/info\n")
        print("Name is " + hero.name)        
        print("Health is " + hero.health) 
        print("Damage is " + hero.attackPower)

        print("Would you Like to Start Auto Combat Game, Enter Y")
        input("")

        if input().lower() == "y":
            roll = random.randint(1, 2) 
            if roll > 1:
                battle = True
                while battle == True:
                    print("You attack " + enemy.name)
                    dmg.takeDmg(enemy)
                    print(enemy.name + " Health is " + enemy.health)
                    if enemy.health <= 0:
                        break
                    print(enemy.name +" attacks you ")
                    dmg.takeDmg(hero)
                    print(hero.name + " Health is " + hero.health)
                    if hero.health <= 0:
                        break
            if roll <= 1:
                battle = True
                while battle == True:
                    print(enemy.name +" attacks you ")
                    dmg.takeDmg(hero)
                    print(hero.name + " Health is " + hero.health)
                    if hero.health <= 0:
                        break
                    print("You attack " + enemy.name)
                    dmg.takeDmg(enemy)
                    print(enemy.name + " Health is " + enemy.health)
                    if enemy.health <= 0:
                        break    



    if __name__ == "__main__":
        main()