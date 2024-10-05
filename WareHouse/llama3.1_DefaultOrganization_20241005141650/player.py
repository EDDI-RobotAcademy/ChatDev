# player.py
'''
Player data.
'''
class Player:
    def __init__(self, name):
        '''
        Initialize the player.
        Args:
            name (str): The player's name.
        '''
        self.name = name
        self.score = 0
        self.rolls_history = []