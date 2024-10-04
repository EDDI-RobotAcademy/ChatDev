# unittest
import unittest
from roll_dice_app import RollDiceApp
class TestRollDiceApp(unittest.TestCase):
    def setUp(self):
        self.app = RollDiceApp()
    def test_run_app_valid_input(self):
        with self.assertRaises(Exception):
            self.app.run(1)  # test running the app with valid input (e.g., 1)
    def test_run_app_invalid_input_type(self):
        with self.assertRaises(TypeError):
            self.app.run("hello")  # test running the app with invalid input type (string)
    def test_run_app_invalid_input_value(self):
        with self.assertRaises(Exception):
            self.app.run(10000)  # test running the app with large integer value
class TestRollDiceAppExceptions(unittest.TestCase):
    def test_unexpected_error(self):
        app = RollDiceApp()
        try:
            app.run(1000)  # Simulate an unexpected error while running the app
        except Exception as e:
            self.assertEqual(str(e), "Unexpected error occurred")