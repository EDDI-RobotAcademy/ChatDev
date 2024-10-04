# unittest_app_roll_dice.py
import unittest
from app_roll_dice import RollDiceApp
class TestRollDiceAppBusinessLogic(unittest.TestCase):
    def test_default_dice(self):
        # Arrange: Create a RollDiceApp instance with default dice
        app = RollDiceApp()
        # Act: Get the result of rolling the Dice using the RollDiceApp instance
        result = app.roll_dice()
        # Assert: Verify that the actual result matches the expected outcome
        self.assertIsInstance(result, str)
    def test_custom_dice_sides(self):
        # Arrange: Create a RollDiceApp instance with custom dice sides
        app = RollDiceApp()
        app.dice.sides = 10
        # Act: Get the result of rolling the Dice using the RollDiceApp instance
        result = app.roll_dice()
        # Assert: Verify that the actual result matches the expected outcome
        self.assertIn('10', result)
    def test_roll_dice_result_type(self):
        # Arrange: Create a RollDiceApp instance with default dice
        app = RollDiceApp()
        # Act: Get the result of rolling the Dice using the RollDiceApp instance
        result = app.roll_dice()
        # Assert: Verify that the actual result is of the expected type
        self.assertIsInstance(result, str)