# game.py
'''Defines the Game class to manage the game state and history.'''
class RollHistory:
    def __init__(self):
        self.roll_history = []
    def add_roll(self, result):
        if not self.roll_history:
            self.roll_history.append(result)
        else:
            self.roll_history.append({'roll_result': result})
class Game:
    def __init__(self):
        self.roll_history = RollHistory()
    def update_roll_history(self, roll_result):
        self.roll_history.add_roll(roll_result)