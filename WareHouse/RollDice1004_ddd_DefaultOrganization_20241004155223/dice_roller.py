# LANGUAGE: Python
# DOCSTRING: Class that rolls a dice and returns its outcome.
"""
Class that rolls a dice and returns its outcome.
This class is responsible for generating a random number (i.e., the dice outcome)
and returning it to the caller.
"""
import random
class DiceRoller:
    def roll_dice(self):
        return random.randint(1, 6)
    def get_outcome(self):
        return self.roll_dice()