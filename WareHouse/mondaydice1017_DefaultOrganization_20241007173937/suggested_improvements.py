# LANGUAGE: Python3
"""
DOCSTRING:
Improvement class for the game.
"""
from game import Game, Player
class SuggestedImprovements:
    def __init__(self, game):
        self.game = game
    def on_reset_game_button_click(self, dice_roller):
        result = dice_roller.roll_dice()
        for player in self.game.players:
            player.update_score(result)
        self.game.reset_game()