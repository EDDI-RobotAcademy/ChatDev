# python
'''
DOCSTRING:
This module defines the Dice class, which represents a single dice.
'''
import random
class Dice:
    def __init__(self, sides=6):
        if sides < 1:
            raise ValueError("Number of sides must be at least 1")
        self.sides = max(sides, 2)
        self.roll_value = 0
    def _generate_roll(self):
        return random.randint(1, self.sides)
    def roll(self):
        self.roll_value = self._generate_roll()