# unittest
import unittest
from dice_roller import DiceRoller
class TestDiceRoller(unittest.TestCase):
    def setUp(self):
        self.roller = DiceRoller()
    def test_roll_dice_valid_input(self):
        outcome = self.roller.roll_dice()
        self.assertGreaterEqual(outcome, 1)
        self.assertLessEqual(outcome, 6)
    def test_roll_dice_invalid_input_type(self):
        with self.assertRaises(TypeError):
            self.roller.roll_dice("hello")
class TestDiceRollerExceptions(unittest.TestCase):
    def test_error_generation(self):
        roller = DiceRoller()
        try:
            roller.roll_dice()  # Simulate an error while generating a random number
        except Exception as e:
            self.assertEqual(str(e), "Error generating random number")