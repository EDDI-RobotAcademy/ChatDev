# LANGUAGE: Python
# DOCSTRING: Business logic: `GameLogic`
'''
game_logic.py
Business logic for the dice rolling game.
'''
from dice_roll import DiceRoll
import random
class GameLogic:
    def __init__(self):
        self.dice = DiceRoll()
        self.rolled_scores = []
    def roll_dice(self):
        self.dice.result = random.randint(1, 6)
        self.rolled_scores.append(self.dice.result)
    @property
    def current_score(self):
        return self.dice.result
    @property
    def all_rolled_scores(self):
        return self.rolled_scores