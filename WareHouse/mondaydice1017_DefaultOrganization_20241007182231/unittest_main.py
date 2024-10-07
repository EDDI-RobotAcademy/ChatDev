# LANGUAGE: Python
'''
DOCSTRING: Unit tests for edge cases of the Dice class's methods.
'''
import unittest
from dice import Dice  # Importing the Dice class from 'dice.py'
class TestDiceEdgeCases(unittest.TestCase):
    def test_get_result(self):
        # Arrange: Create a new instance of the Dice class.
        dice = Dice()
        # Act: Call the get_result() method and store the result.
        result = dice.get_result()
        # Assert: Verify that the result is correct.
        self.assertEqual(result, 1)
    def test_check_winner(self):
        # Arrange: Create a new instance of the Dice class.
        dice = Dice()
        # Act: Call the check_winner() method and store the result.
        result = dice.check_winner()
        # Assert: Verify that the result is correct.
        self.assertEqual(result, False)
if __name__ == "__main__":
    unittest.main()