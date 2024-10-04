# domain_dice.py
"""
Module containing the Dice entity and its related logic.
"""
import random
class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)