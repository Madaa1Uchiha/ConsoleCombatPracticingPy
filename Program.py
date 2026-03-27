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
        creature_list = CreatureList()
   
    #Just a welcome message and asking for the player's name and gender
        print ("Welcome to Console Combat Practicing Py!")
        print ("This like pokemon where you get to choose a creature to fight with and battle against an enemy, but with a twist of you being able to choose your name and creature!")
        players.name = input("Enter your name: ")
        players.gender = input("Enter your gender: ")
        print("Hello " + players.name + " the " + players.gender + "!")

    #Asking the player to choose a creature and showing them the list of creatures to choose from
       # print ("Here are the creatures you can choose from: ")

       # for creature in creature_list.creatures:
         #  print(creature.name + ": " + creature.description)
       

        creature_choice = creature_list.creatures
        for i, creature in enumerate(creature_choice):
            print(str(i + 1) + ". " + creature.name)

        creature_choice = input("Choose a creature by number or name: ")
        if creature_choice.isdigit():
            index = int(creature_choice) - 1
            if 0 <= index < len(creature_list.creatures):
                players.creature = creature_list.creatures[index]
            else:
                print("Invalid number.")
                players.creature = None
        else:
            players.creature = next((c for c in creature_list.creatures if c.name.lower() == creature_choice.lower()), None)
            if players.creature is None:
                print("Creature not found.")
            

        print("You chose " + players.creature.name + "!")
        print("Your creature's stats are: Health: " + str(players.creature.health) + ", Attack Power: " + str(players.creature.attackPower) + ", Speed: " + str(players.creature.speed) + ", Defense: " + str(players.creature.defense) + ", Type: " + players.creature.type)
            
        enemy.creature = creature_list.creatures[random.randint(0, len(creature_list.creatures) - 1)]

        answer = input("Would you like to start Auto Combat? Enter Y\n")
        Program.Battle(creature_list, players, enemy, dmg, answer)
        
        
    def Battle(creature_list, players, enemy, dmg, answer):
        battle = False
        print("You entered: " + answer)
        if answer.lower() == "y":
            battle = True
            if players.creature.speed >= enemy.creature.speed:
                print("You go first!")
                print(players.creature.name + " vs " + enemy.creature.name)
                while battle:
                    # When showing the options, number them
                    attack_list = players.creature.attacks
                    for i, attack in enumerate(attack_list):
                        print(str(i + 1) + ". " + attack.name)

                    attack_choice = input("Choose an attack: ")

                    # Check if they typed a number
                    if attack_choice.isdigit():
                        index = int(attack_choice) - 1
                        if 0 <= index < len(attack_list):
                            attack = attack_list[index]
                        else:
                            print("Invalid number.")
                            attack = None
                    else:
                        # Fall back to name matching
                        attack = next((a for a in attack_list if a.name.lower() == attack_choice.lower()), None)
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
                    # When showing the options, number them
                    attack_list = players.creature.attacks
                    for i, attack in enumerate(attack_list):
                        print(str(i + 1) + ". " + attack.name)

                    attack_choice = input("Choose an attack: ")

                    # Check if they typed a number
                    if attack_choice.isdigit():
                        index = int(attack_choice) - 1
                        if 0 <= index < len(attack_list):
                            attack = attack_list[index]
                        else:
                            print("Invalid number.")
                            attack = None
                    else:
                        # Fall back to name matching
                        attack = next((a for a in attack_list if a.name.lower() == attack_choice.lower()), None)
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