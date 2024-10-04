'''
Handles user input and updates the game state.
'''
import random
class Roller:
    def __init__(self, game_service):
        self.game_service = game_service
    def handle_input(self, input_str):
        # Handle user input (e.g., "roll" to start a new game)
        if input_str == "roll":
            return self.game_service.start_game()
        else:
            raise ValueError("Invalid input")