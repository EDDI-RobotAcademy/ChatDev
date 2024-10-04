# python
'''
Domain Model for Roll Dice App
'''
from abc import ABC, abstractmethod
class Dice(ABC):
    @abstractmethod
    def roll(self):
        pass
    def __str__(self):
        return f"Dice with {self.sides} sides"
class SixSidedDie(Dice):
    def __init__(self):
        self.sides = 6
    def roll(self):
        # Implement the roll logic here
        # For simplicity, we'll use a random number between 1 and 6
        import random
        return random.randint(1, 6)
class RollDiceDomain:
    def __init__(self, die):
        self.die = die
    def roll_dice(self, num_rolls=1):
        results = []
        for _ in range(num_rolls):
            results.append(str(self.die.roll()))
        return ", ".join(results)