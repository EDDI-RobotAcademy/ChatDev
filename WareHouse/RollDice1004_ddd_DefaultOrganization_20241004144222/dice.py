# dice.py
'''Defines the RollResult and roll_die functions for rolling a die.'''
import random
class RollResult:
    def __init__(self, value, rolls):
        self.value = value
        self.rolls = rolls
def roll_die(num_sides):  # Modified function to match import statement in main.py
    return RollResult(random.randint(1, num_sides), [random.randint(1, num_sides)])