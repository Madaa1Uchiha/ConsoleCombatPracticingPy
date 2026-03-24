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
        print("Health is " + str(hero.health))
        print("Damage is " + str(hero.attackPower))

        answer = input("Would you like to start Auto Combat? Enter Y\n")
        print("You entered: " + answer)
        if answer.lower() == "y":
            roll = random.randint(1, 2) 
            roll = 1
            if roll > 1:
                battle = True
                while battle == True:
                    print("You attack " + enemy.name)
                    dmg.takeDmg(enemy)
                    print(enemy.name + " Health is " + str(enemy.health))
                    if enemy.health <= 0:
                        print("You win!")
                        break
                    print(enemy.name +" attacks you ")
                    dmg.takeDmg(hero)
                    print(hero.name + " Health is " + str(hero.health))
                    if hero.health <= 0:
                        print("You lose!")
                        break
            if roll <= 1:
                battle = True
                while battle == True:
                    print(enemy.name +" attacks you ")
                    dmg.takeDmg(hero)
                    print(hero.name + " Health is " + str(hero.health))
                    if hero.health <= 0:
                        print("You lose!")
                        break
                    print("You attack " + enemy.name)
                    dmg.takeDmg(enemy)
                    print(enemy.name + " Health is " + str(enemy.health))
                    if enemy.health <= 0:
                        print("You win!")
                        break    



if __name__ == "__main__":
    Program.main()