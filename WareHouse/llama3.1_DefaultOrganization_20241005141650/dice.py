# dice.py
'''
Dice data.
'''
class Dice:
    def __init__(self):
        '''
        Initialize a die.
        This is a simple implementation of a die.
        Each time the die is rolled, it generates a random number between 1 and 6.
        '''
        self.value = None
    def roll(self):
        '''
        Roll the dice.
        '''
        self.value = random.randint(1, 6)