# Domain model classes.
from random import randint
class Dice:
    def __init__(self):
        self.sides = 6
    def roll(self):
        return randint(1, self.sides)