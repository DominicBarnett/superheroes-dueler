import random
class Weapon:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' This method returns a random value between one half to full attack power of the weapon'''
        half_damage = self.max_damage // 2
        random_damage = random.randint(half_damage, self.max_damage)
        return random_damage
