import tkinter as tk
from dice import Dice
from settings import Settings
class GameEngine:
    """Manages the game flow."""
    def __init__(self, settings):
        """
        Initializes a new GameEngine instance.
        """
        self.settings = settings
        self.dice = None  # Initialize dice as None
        self.roll_history = []  # Initialize roll history as an empty list
    # Handle user input
    def handle_user_input(self, input_value):
        try:
            if input_value == "roll":
                # Roll the dice
                self.dice = Dice(6)  # Create a new Dice instance with sides=6
                roll_result = self.dice.roll()
                print(f"You rolled: {roll_result}")
                self.validate_roll(roll_result)
            elif input_value == "save":
                self.save_game_history()
            else:
                print("Invalid input. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
    # Start a new game
    def start_game(self):
        """
        Starts a new game.
        """
        print("Game started!")
        while True:
            self.handle_user_input(input())