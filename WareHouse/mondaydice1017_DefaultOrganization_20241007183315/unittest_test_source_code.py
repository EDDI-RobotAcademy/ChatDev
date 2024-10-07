#!/usr/bin/env python3
"""
Unit Test File for source_code.py
This file contains unit test cases for source_code.py.
"""
import unittest
from source_code import DiceRoll, GameLogic
class TestDiceRoll(unittest.TestCase):
    def setUp(self):
        self.dice_roll = DiceRoll()
    def test_roll_dice_result(self):
        result = self.dice_roll.roll()
        self.assertIsInstance(result, int)
    def test_invalid_result(self):
        with self.assertRaises(ValueError):
            self.dice_roll.result = 'hello'
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