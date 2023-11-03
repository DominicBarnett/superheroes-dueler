import random
class Armor:
    def __init__(self, name, max_block):
        ''''Initialize the values passed into this method
        as instance variables'''

        self.name = name
        self.max_block = max_block

    def block(self):
        '''return a value between 0 and the value set by max'''
        block_value = random.randint(0,self.max_block)
        return block_value



if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())