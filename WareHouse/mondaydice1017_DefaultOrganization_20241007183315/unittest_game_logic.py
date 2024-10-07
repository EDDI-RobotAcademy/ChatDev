"""
Unit test for game_logic module.
"""
import unittest
from app import GameLogic  # noqa: F401
class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()
    def test_roll_dice(self):
        # Verify that the roll_dice method returns a list of rolled dice
        rolled_dice = self.game.roll_dice(5)
        self.assertIsInstance(rolled_dice, list)
    def test_all_rolled_scores(self):
        # Test that all_rolled_scores property returns a dictionary with expected values
        rolled_scores = self.game.all_rolled_scores
        self.assertIsInstance(rolled_scores, dict)