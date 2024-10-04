# unittest
'''
Unit test for Roll Dice App
'''
import unittest
from dice import RollResult, roll_die
from game_manager import GameManager
class TestApp(unittest.TestCase):
    def test_gui_initialization(self):
        gui = GUI()
        gui.run()
        self.assertEqual(gui.root.title(), "Roll Dice App")
    def test_roll_die_functionality(self):
        num_sides = 6
        result = RollResult(5, [4])
        roll_die(num_sides)
        self.assertEqual(result.value, 5)
    def test_game_history_functionality(self):
        game_manager = GameManager()
        roll_result = RollResult(3, [2])
        game_manager.add_roll_to_history(roll_result)
        self.assertIsNotNone(game_manager.game.roll_history.add_roll)
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            roll_die(-5)
    def test_edge_cases_game_history(self):
        game_manager = GameManager()
        for _ in range(5):
            game_manager.add_roll_to_history(RollResult(3, [2]))
        self.assertEqual(len(game_manager.game.roll_history.roll_history), 5)