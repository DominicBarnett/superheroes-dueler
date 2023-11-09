import random
from hero import Hero

class Team:
    def __init__(self, name):
        '''initialize your team with its team name and an empty list of heroes'''
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        '''Remove a hero from heroes list
        if hero isn't found return 0'''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
            
        if not foundHero:
            return 0
        
    def view_all_heroes(self):
        '''prints out all heroes to the console.'''
        for hero in self.heroes:
            print(f'{hero.name}')
    
    def add_hero(self, hero):
        '''Add Hero object to self.heroes'''
        self.heroes.append(hero)
    
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f'{hero.name} Kill/Deaths:{kd}')
            
    def revive_heroes(self):
        '''reset all heroes health to starting_health'''
        for hero in self.heroes:
            
            hero.current_health = hero.starting_health
        print(f'{hero.name} has been revived with {hero.starting_health} health')

    def attack(self, other_team):
        '''Battle each team against each other'''

        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)
        
        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            fighting_hero = random.choice(living_heroes)
            fighting_opponent = random.choice(living_opponents)

            winner = fighting_hero.fight(fighting_opponent)

            if winner == fighting_hero:
                living_opponents.remove(fighting_opponent)
            else:
                living_heroes.remove(fighting_hero)