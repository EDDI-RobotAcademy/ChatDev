import pickle
from dice import Dice  # Import the Dice class from the dice module
class GameEngine:
    """
    Manages the game flow.
    """
    def __init__(self):
        """
        Initializes a new GameEngine instance.
        """
        self.difficulty_level = "hard"
        self.dice = None
        self.roll_history = []
    def start_game(self):
        """
        Starts a new game.
        """
        print("Game started!")
        while True:
            # Handle user input
            self.handle_user_input(input())
            # ... (add more game logic here)
    def handle_user_input(self, input_value):
        try:
            if input_value == "roll":
                # Roll the dice
                self.dice = Dice(6)  # create a new dice with 6 sides
                roll_result = self.dice.roll()
                print(f"You rolled: {roll_result}")
                self.validate_roll(roll_result)
            elif input_value == "save":
                # Save game history
                self.save_game_history()
            elif input_value == "difficulty":
                # Change difficulty level
                if input_value == "easy":
                    self.difficulty_level = "easy"
                elif input_value == "hard":
                    self.difficulty_level = "hard"
                else:
                    print("Invalid difficulty level. Please try again.")
            elif input_value == "quit":
                # Quit the game
                print("Game quit!")
                break
            else:
                print("Invalid input. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
    def validate_roll(self, roll_result):
        """
        Validates the roll result.
        Args:
            roll_result (int): The rolled dice value.
        """
        if 1 <= roll_result <= 6:
            print("Valid roll!")
        else:
            print("Invalid roll!")
    def save_game_history(self):
        """
        Saves the game history to a file.
        """
        with open("roll_history.dat", "wb") as file:
            pickle.dump(self.roll_history, file)