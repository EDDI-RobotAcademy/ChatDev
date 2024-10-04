# app_roll_dice.py
"""
Module containing the business logic for rolling a dice.
"""
from domain_dice import Dice
class RollDiceApp:
    def __init__(self):
        self.dice = Dice()
    def roll_dice(self):
        result = self.dice.roll()
        return f"You rolled a {result}"