# LANGUAGE: Python
'''
Game logic class for managing the game state.
Modified the GameLogic class to have an `add_result()` method only, as it's sufficient for the current application.
Removed the non-existent `start_game()` method.
'''
class GameLogic:
    def __init__(self):
        '''
        Initialize the game logic class with an empty list to store rolled dice results.
        '''
        self.results = []
    def add_result(self, result):
        '''
        Add a rolled dice result to the game state.
        Args:
            result (str): The rolled dice result to be added.
        '''
        # Append the rolled dice result to the history listbox
        self.results.append(result)