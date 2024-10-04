'''User Interface class implementation'''
class UserInterface:
    """Handles user input and displays game state."""
    def __init__(self, game_engine):
        """
        Initializes a new User Interface instance.
        Args:
            game_engine (GameEngine): The GameEngine instance to be used in the UI.
        """
        self.game_engine = game_engine
        self.window = tk.Tk()
        self.window.title("Dice Roll Game")
        self.window.geometry("300x200")
        self.entry_label = tk.Label(self.window, text="Enter a number (1-6) or 'roll' to roll the dice:")
        self.entry_label.pack()
        self.entry_field = tk.Entry(self.window)
        self.entry_field.pack()
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()
        self.roll_button = tk.Button(self.button_frame, text="Roll", command=self.roll_dice)
        self.roll_button.pack(side=tk.LEFT)
        self.save_button = tk.Button(self.button_frame, text="Save Game History", command=self.save_game_history)
        self.save_button.pack(side=tk.LEFT)
    def display_game_state(self):
        """Displays the current game state."""
        self.result_label['text'] = ""
    def roll_dice(self):
        """
        Rolls the dice and updates the game state.
        Returns:
            None
        """
        try:
            roll_result = int(self.entry_field.get())
            if 1 <= roll_result <= 6:
                self.game_engine.dice = Dice(roll_result)  # create a new dice with the specified number of sides
                roll_result = self.game_engine.dice.roll()
                print(f"You rolled: {roll_result}")
                self.validate_roll(roll_result)
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number or 'roll'.")
    def validate_roll(self, roll_result):
        """Validates the result of a dice roll."""
        if roll_result < 1 or roll_result > 6:
            print("Invalid roll! Roll again.")
        else:
            print(f"Valid roll: {roll_result}")
            self.result_label['text'] = f"You rolled: {roll_result}"
    def save_game_history(self):
        """Saves the game history to the database."""
        # Save current roll result to the database
        self.game_engine.roll_history.add_roll(self.game_engine.dice.roll_result)
        print("Game saved successfully!")
        self.result_label['text'] = "Game saved successfully!"
    def load_game_history(self, filename):
        """Loads the game history from a file."""
        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
                # Load roll history from the file
                self.game_engine.roll_history.rolls.extend(data["rolls"])
                print("Game loaded successfully!")
            self.result_label['text'] = "Game loaded successfully!"
        except FileNotFoundError:
            print("File not found.")
    def start(self):
        """Starts the game loop."""
        self.window.mainloop()