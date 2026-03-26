from Player import Player
from Enemy import Enemy
from Dmg_Heal import Dmg_Heal
from CreatureList import CreatureList
import random


class Program():

    def main():
        players = Player()
        enemy = Enemy()
        dmg = Dmg_Heal()
        battle = False
        creature_list = CreatureList()

    #Just a welcome message and asking for the player's name and gender
        print ("Welcome to Console Combat Practicing Py!")
        print ("This like pokemon where you get to choose a creature to fight with and battle against an enemy, but with a twist of you being able to choose your name and creature!")
        players.name = input("Enter your name: ")
        players.gender = input("Enter your gender: ")
        print("Hello " + players.name + " the " + players.gender + "!")

    #Asking the player to choose a creature and showing them the list of creatures to choose from
        print ("Here are the creatures you can choose from: ")

        for creature in creature_list.creatures:
            print(creature.name + ": " + creature.description)
       
        choice = input("Which would you like to choose? Enter the name of the creature: ")
        players.creature = next((c for c in creature_list.creatures if c.name.lower() == choice.lower()), None)
        if players.creature is None:
            print("Creature not found.")

        print("You chose " + players.creature.name + "!")
        print("Your creature's stats are: Health: " + str(players.creature.health) + ", Attack Power: " + str(players.creature.attackPower) + ", Speed: " + str(players.creature.speed) + ", Defense: " + str(players.creature.defense) + ", Type: " + players.creature.type)
            
        enemy.creature = creature_list.creatures[random.randint(0, len(creature_list.creatures) - 1)]

        answer = input("Would you like to start Auto Combat? Enter Y\n")
        print("You entered: " + answer)
        if answer.lower() == "y":
            battle = True
            if players.creature.speed >= enemy.creature.speed:
                print("You go first!")
                while battle:
                    attack_choice = input("Choose an attack: " + ", ".join([attack.name for attack in players.creature.attacks]) + "\n")
                    attack = next((a for a in players.creature.attacks if a.name.lower() == attack_choice.lower()), None)
                    if attack is None:
                        print("Attack not found.")
                        continue
                    damage_dealt = dmg.takeDmg(players.creature, attack, enemy.creature)
                    print("You used " + attack.name + " and dealt " + str(round(damage_dealt, 1)) + " damage!")
                    print("Enemy health: " + str(round(enemy.creature.health, 1)))  # helpful to add this
                    if enemy.creature.health <= 0:
                        print("You win!")
                        battle = False
                        break
                    enemy_attack = random.choice(enemy.creature.attacks)
                    enemy_damage = dmg.takeDmg(enemy.creature, enemy_attack, players.creature)
                    print("The enemy used " + enemy_attack.name + " and dealt " + str(round(enemy_damage, 1)) + " damage!")
                    print("Your health: " + str(round(players.creature.health, 1)))  # and this
                    if players.creature.health <= 0:
                        print("You lose!")
                        battle = False
                        break
            else:
                print("The enemy goes first!")
                while battle:
                    enemy_attack = random.choice(enemy.creature.attacks)
                    enemy_damage = dmg.takeDmg(enemy.creature, enemy_attack, players.creature)
                    print("The enemy used " + enemy_attack.name + " and dealt " + str(round(enemy_damage, 1)) + " damage!")
                    print("Your health: " + str(round(players.creature.health, 1)))  # and this
                    if players.creature.health <= 0:
                        print("You lose!")
                        battle = False
                        break
                    attack_choice = input("Choose an attack: " + ", ".join([attack.name for attack in players.creature.attacks]) + "\n")
                    attack = next((a for a in players.creature.attacks if a.name.lower() == attack_choice.lower()), None)
                    if attack is None:
                        print("Attack not found.")
                        continue
                    damage_dealt = dmg.takeDmg(players.creature, attack, enemy.creature)
                    print("You used " + attack.name + " and dealt " + str(round(damage_dealt, 1)) + " damage!")
                    print("Enemy health: " + str(round(enemy.creature.health, 1)))  # helpful to add this
                    if enemy.creature.health <= 0:
                        print("You win!")
                        battle = False
                        break

if __name__ == "__main__":
    Program.main()