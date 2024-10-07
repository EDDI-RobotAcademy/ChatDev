# LANGUAGE: Python
# DOCSTRING: Domain model: `DiceRoll`
'''
dice_roll.py
Domain model for a single dice roll outcome.
'''
import random
class DiceRoll:
    def __init__(self):
        self._result = None
    @property
    def result(self):
        return self._result
    @result.setter
    def result(self, value):
        if not isinstance(value, int) or not 1 <= value <= 6:
            raise ValueError("Dice roll outcome must be an integer between 1 and 6")
        self._result = value