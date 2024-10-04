# dice.py
'''
Dice Domain Model (No Changes Required)
'''
import random
class Dice:
    def __init__(self):
        self.sides = 6
    def roll(self):
        # Simulate a die roll using random.choice
        return [random.choice([1,2,3,4,5,6])] * self.sides
class Die(Dice):
    def __init__(self):
        super().__init__()
    def get_result(self):
        return self.roll()