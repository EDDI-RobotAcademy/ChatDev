# unittest_roll_dice_app.py
"""
Unit tests for RollDiceApp.
"""
import unittest
from roll_dice_app import RollDiceApp
class TestRollDiceApp(unittest.TestCase):
    def test_run_app(self):
        app = RollDiceApp()
        outcome = app.run_app(5)  # valid input
        self.assertGreaterEqual(outcome, 1)
        self.assertLessEqual(outcome, 6)
    def test_run_app_large_input(self):
        app = RollDiceApp()
        with self.assertRaises(Exception):  # expect Exception to be raised for large input (1000)
            app.run_app(1000)
    def test_run_app_invalid_input_type(self):
        app = RollDiceApp()
        with self.assertRaises(TypeError):  # expect TypeError to be raised for invalid input type
            app.run_app("hello")  # passing a string as an argument
if __name__ == '__main__':
    unittest.main()