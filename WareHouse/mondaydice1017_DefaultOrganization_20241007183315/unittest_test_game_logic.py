#!/usr/bin/env python3
"""
Unit Test File for game_logic.py
This file contains unit test cases for the GameLogic class.
"""
import unittest
from game_logic import GameLogic
class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game_logic = GameLogic()
    def test_roll_dice(self):
        self.game_logic.roll_dice()
        self.assertEqual(self.game_logic.current_score, 5)
        self.assertEqual(len(self.game_logic.rolled_scores), 1)
    def test_current_score_property(self):
        self.game_logic.roll_dice()
        self.assertEqual(self.game_logic.current_score, 5)