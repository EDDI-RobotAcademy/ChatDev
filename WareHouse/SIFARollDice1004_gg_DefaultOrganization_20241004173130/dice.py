# dice.py (Python)
'''
Represents a single die entity.
'''
import random
class Dice:
    def __init__(self):
        self.value = None
    def roll(self):
        # Simulate rolling the dice (in real application, use a random number generator)
        self.value = 1 + random.randint(0, 5)  
        return self.value