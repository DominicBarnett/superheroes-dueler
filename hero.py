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

    def take_damage(self, damage):
        self.current_health -= damage

    def is_alive(self):
        return self.current_health > 0


    def fight(self, opponent):
            ''' Current Hero will take turns fighting the opponent hero passed in.
            '''
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
  my_hero = Hero("Grace Hopper", 200)
  villan = Hero("Jane")
  print(my_hero.name)
  print(my_hero.current_health)

  winner = my_hero.fight(villan)