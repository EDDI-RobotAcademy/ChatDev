# roll.py
'''Encapsulates a single roll of the dice'''
class Roll:
    def __init__(self, die):
        self.die = die
        self.result = None
    def roll_die(self):
        self.result = self.die.roll()
    def get_result(self):
        return self.result