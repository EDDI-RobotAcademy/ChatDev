# FILENAME: suggested_improvements.py
LANGUAGE: Python
'''
DOCSTRING: Improving the game logic.
'''
from .game import Game, Player
class SuggestedImprovements:
    def __init__(self):
        self.game = Game()
    def on_reset_game_button_click(self):
        # Implementing a more robust score update method
        result = self.dice_roller.roll_dice()
        for player in self.game.players:
            player.update_score(result)
        # Update the game state properly after resetting
        self.game.reset_game()