import pickle
class Settings:
    """Stores and loads game settings."""
    def __init__(self):
        """
        Initializes a new Settings instance.
        """
        self.difficulty_level = 1
    # Load difficulty level from the file
    @staticmethod
    def load_settings(filename):
        with open(filename, "rb") as file:
            data = pickle.load(file)
            return data
    # Save difficulty level to a file
    def save_settings(self):
        with open("settings.dat", "wb") as file:
            pickle.dump({"difficulty_level": self.difficulty_level}, file)