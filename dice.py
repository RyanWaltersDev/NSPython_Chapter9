from random import randint
'''Modeling a simple dice roller'''

class Dice:

    def __init__(self, sides=6):
        '''Initalize dice attributes'''
        self.sides = sides

    def roll_dice(self, sides=6):
        '''Select random integer between 1 and the sepcified number of sides'''
        print(randint(1, sides))

six_sided = Dice()
six_sided.roll_dice()

ten_sided = Dice()
ten_sided.roll_dice(sides=10)

twenty_sided = Dice()
twenty_sided.roll_dice(sides=20)
