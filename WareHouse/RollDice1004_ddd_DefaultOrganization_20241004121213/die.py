# die.py
'''Represents a single die with properties like face value and result'''
class Dice:
    def __init__(self):
        self.face_value = 6
    def roll(self):
        import random
        return random.randint(1, self.face_value)