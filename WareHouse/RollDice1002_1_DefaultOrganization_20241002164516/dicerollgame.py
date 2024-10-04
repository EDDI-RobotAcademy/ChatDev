import tkinter as tk
from dice import Dice
from dice_roll_history_database import DiceRollHistoryDatabase
from game_engine import GameEngine
from settings import Settings
class DiceRollGame:
    """Manages the main application flow."""
    def __init__(self):
        """
        Initializes a new DiceRollGame instance.
        """
        self.game_engine = GameEngine(Settings())
    def run(self):
        """Runs the game loop."""
        while True:
            # Start a new game
            self.game_engine.start_game()
            break
# Example usage:
game = DiceRollGame()
game.run()