import pickle
class DiceRollHistoryDatabase:
    """
    Stores game history.
    """
    def __init__(self):
        """
        Initializes a new DiceRollHistoryDatabase instance.
        """
        self.history = []
    def save_game_history(self):
        """
        Saves the game history to a file.
        """
        with open("roll_history.dat", "wb") as file:
            pickle.dump(self.history, file)