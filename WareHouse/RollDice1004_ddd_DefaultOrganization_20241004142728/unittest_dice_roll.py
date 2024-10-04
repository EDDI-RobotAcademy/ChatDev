# unittest_dice_roll.py
import unittest
from dice import Dice
class TestDiceDomainLogic(unittest.TestCase):
    def test_default_sides(self):
        # Arrange: Create a Dice instance with default sides
        dice = Dice()
        # Act: Get the number of sides on the Dice instance
        result = dice.sides
        # Assert: Verify that the actual result matches the expected outcome
        self.assertEqual(result, 6)
    def test_custom_sides(self):
        # Arrange: Create a Dice instance with custom sides
        dice = Dice(sides=10)
        # Act: Get the number of sides on the Dice instance
        result = dice.sides
        # Assert: Verify that the actual result matches the expected outcome
        self.assertEqual(result, 10)
    def test_roll_result_within_range(self):
        # Arrange: Create a Dice instance with default sides
        dice = Dice()
        # Act: Roll the Dice and get the result
        result = dice.roll()
        # Assert: Verify that the actual result is within the expected range
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)
    def test_roll_result_type(self):
        # Arrange: Create a Dice instance with default sides
        dice = Dice()
        # Act: Roll the Dice and get the result
        result = dice.roll()
        # Assert: Verify that the actual result is of the expected type
        self.assertIsInstance(result, int)