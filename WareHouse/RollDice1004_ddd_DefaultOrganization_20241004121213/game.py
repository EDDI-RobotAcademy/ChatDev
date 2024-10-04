# game.py
'''Manages the game state, including the current score and number of rolls'''
class Game:
    def __init__(self):
        self.score = 0
        self.num_rolls = 0
    def update_score(self, result):
        self.score += result
    def get_score(self):
        return self.score