# roll_service.py
# LANGUAGE: Python
'''
Service class to manage the dice rolls.
DOCSTRING:
Provides methods to get and set the current die roll,
as well as add a new roll result to the statistics.
'''
class RollService:
    def __init__(self):
        self.current_roll = None
    def get_current_roll(self):
        return self.current_roll
    def set_current_roll(self, value):
        self.current_roll = value
    def add_roll_result(self, roll_result):
        # Update the current roll and history in the RollResultProxy
        pass