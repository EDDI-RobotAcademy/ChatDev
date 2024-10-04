# FILENAME: dice_model.py
# LANGUAGE: Python 3.x
'''
DOCSTRING:
This module defines the business logic for rolling a dice.
It encapsulates the domain knowledge and provides a simple API for interacting with it.
'''
import dash
from dash.dependencies import Input, Output
import random
class DiceModel:
    def __init__(self):
        pass
    @staticmethod
    def roll_dice(sides):
        # Simulate rolling the dice by generating a random number between 1 and sides (inclusive)
        if not isinstance(sides, int) or sides <= 0:
            raise ValueError("Invalid input: 'sides' must be a positive integer")
        return random.randint(1, sides)
    def update_graph(self, result):
        # Simulate updating the graph with the rolled dice result
        fig = {"result": result}
        return fig
# unittest (to enable Python's unittest framework)
import unittest
class TestDiceModel(unittest.TestCase):
    def test_roll_dice_valid_input(self):
        model = DiceModel()
        result = model.roll_dice(6)
        self.assertIsInstance(result, int)
    def test_roll_dice_invalid_input_type(self):
        model = DiceModel()
        with self.assertRaises(ValueError):
            model.roll_dice("not an integer")
    def test_roll_dice_invalid_input_value(self):
        model = DiceModel()
        with self.assertRaises(ValueError):
            model.roll_dice(-5)
if __name__ == '__main__':
    unittest.main()