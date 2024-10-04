# dice_roller.py
'''
Dice Roller Class - Responsible for rolling the dice.
'''
import random
class DiceRoller:
    def __init__(self):
        '''
        Initializes a new instance of the DiceRoller class.
        '''
    def roll_dice(self):
        '''
        Rolls a virtual dice and returns the result.
        Returns:
            int: The rolled value.
        '''
        return random.randint(1, 6)
    def get_rolled_dice_value(self):
        '''
        Gets the last rolled value from the DiceRoller instance.
        Returns:
            int: The last rolled value.
        '''
        return self.roll_dice()