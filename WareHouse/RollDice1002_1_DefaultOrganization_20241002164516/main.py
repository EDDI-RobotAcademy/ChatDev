import tkinter as tk
from dice import Dice
from settings import Settings
# Initialize the settings
settings = Settings()
settings.save_settings()
class DiceRollGame:
    """Manages the main application flow."""
    def __init__(self):
        """
        Initializes a new DiceRollGame instance.
        """
        self.game_engine = GameEngine(settings)
    # Run the game loop
    def run(self):
        while True:
            self.game_engine.start_game()