# LANGUAGE: Python3
"""
DOCSTRING:
Provides a Player class to manage player scores.
"""
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def update_score(self, score_update):
        self.score += score_update