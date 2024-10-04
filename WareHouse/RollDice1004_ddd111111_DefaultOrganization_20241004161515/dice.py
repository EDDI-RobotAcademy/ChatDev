# dice.py
# LANGUAGE: Python
'''
Domain model for a single die.
DOCSTRING:
Represents a single die with properties like face value and current state.
'''
class Dice:
    def __init__(self):
        self.face_value = 0
        self.current_state = "idle"
        self.previous_rolls = []
    def roll(self):
        import random
        self.face_value = random.randint(1, 6)
        self.current_state = "rolled"
        return DiceRollResult(self)
class DiceRollResult:
    def __init__(self, die):
        self.die = die
    @property
    def face_value(self):
        return self.die.face_value
    @face_value.setter
    def face_value(self, value):
        self.die.face_value = value