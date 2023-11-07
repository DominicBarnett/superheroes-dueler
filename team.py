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
