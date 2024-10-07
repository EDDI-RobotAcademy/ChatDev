"""
Unit test for dice_roll module.
"""
import unittest
from app import DiceRoll  # noqa: F401
class TestDiceRoll(unittest.TestCase):
    def setUp(self):
        self.dice = DiceRoll()
    def test_roll(self):
        # Verify that the roll method returns a random number
        self.assertIsNotNone(self.dice.roll())
    def test_invalid_input(self):
        # Test with invalid input (e.g., string instead of integer)
        with self.assertRaises(ValueError):
            self.dice.roll("invalid")