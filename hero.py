from ability import Ability
from armor import Armor
from weapon import Weapon
import random

# hero.py
class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''

        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def add_ability(self, ability):
        '''add ability to abilities list'''

        self.abilities.append(ability)
    
    def add_armor(self, armor):
        '''add armor to armor list'''

        self.armors.append(armor)

    def add_weapon(self, weapon):
        '''add weapon to self.abilities'''

        self.abilities.append(weapon)

    def take_damage(self, damage):
        '''updates self.current_health to reflect the damage minus the defense'''

        taken_damage = damage - self.defend() 
        taken_damage = max(taken_damage, 0)
        self.current_health -= taken_damage

    def is_alive(self):
        return self.current_health > 0

    def attack(self):
        '''Calculate the total damage from all ability attacks.
        return: total_damage:Int
        '''
        
        # start our total out at 0
        total_damage = 0
         
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
            # return the total damage
        return total_damage

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''
        total_armor = 0
        # TODO: This method should run the block method on each armor in self.armors
        if self.is_alive():
            for armor in self.armors:
                total_armor += armor.block()
            return total_armor
    

    def fight(self, opponent):
            ''' Current Hero will take turns fighting the opponent hero passed in.
            '''
            if len(self.abilities) == 0:
                print("Draw")
            else:
                while self.is_alive() and opponent.is_alive():
                    winner = random.choice([self, opponent])
                    loser = self if winner == opponent else opponent

                    damage = random.randint(1,50)

                    loser.take_damage(damage)

                    print(f"{winner.name} attacks {loser.name} for {damage} damage!")

                if self.is_alive():
                    print(f"{self.name} wins the battle!")
                    return self
                else:
                    print(f"{opponent.name} wins the battle!")
                    return opponent
            # TODO: Fight each hero until a victor emerges.
            # Phases to implement:
            #1) randomly choose winner,
            # Hint: Look into random library, more specifically the choice method





        









if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
#     my_hero = Hero("Grace Hopper", 200)
#     villan = Hero("Jane")
#     print(my_hero.name)
#     print(my_hero.current_health)
#     ability = Ability("Debugging Ability", 20)
#     print(ability.name)
#     print(ability.attack())
# #   winner = my_hero.fight(villan)
#     armor = Armor("Debugging Shield", 10)
#     print(armor.name)
#     print(armor.block())
#     my_hero.add_ability(ability)
#     print(my_hero.abilities)
    # ability = Ability("Great Debugging", 50)
    # # ability2 = Ability("YOLO", 70)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # # hero.add_ability(ability2)
    # print(hero.abilities)
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # # hero.add_ability(ability)
    # # hero.add_ability(another_ability)
    # # print(hero.attack())
    # armor = Armor("Shield", 1)
    # mor_armor = Armor("Forcefield", 1)
    # hero.add_armor(armor)
    # hero.add_armor(mor_armor)
    # print(hero.defend())
    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
   
