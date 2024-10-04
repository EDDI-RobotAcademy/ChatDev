# game_manager.py
'''Manages the game state and history.'''
from game import Game
class GameManager:
    def __init__(self):
        self.game = Game()
    def add_roll_to_history(self, roll_result):
        self.game.update_roll_history(roll_result)