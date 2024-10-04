# Importing necessary libraries
from tkinter import *
import random
from dice import Dice
class RollResult:
    def __init__(self):
        """
        Initializes the RollResult object with an empty list to store roll results.
        Attributes:
            results (list): The list of roll results.
        """
        self.results = []
class Application(Tk):
    """
    The main application class responsible for creating a GUI and handling user interactions.
    Attributes:
        master (Tk): The root window of the application.
    """
    def __init__(self, master=None):
        """
        Initializes the application frame.
        Args:
            master (Tk): The root window of the application.
        """
        super().__init__()
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        """
        Creates and configures the widgets in the application frame.
        """
        # Create a label to display the roll dice text
        self.dice_label = Label(self)
        self.dice_label["text"] = "Roll Dice"
        self.dice_label.pack(side="top")
        # Create a button to trigger the rolling of dice
        self.roll_button = Button(self)
        self.roll_button["text"] = "Roll"
        self.roll_button["command"] = self.on_roll
        self.roll_button.pack(side="bottom")
        # Create a label to display the results
        self.results_label = Label(self)
    def on_roll(self):
        max_attempts = 3  # You can adjust this value based on your needs.
        attempts = 0
        while True:
            try:
                dice_count = int(input("Enter the number of dice to roll: "))
                if dice_count <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
                attempts += 1
                if attempts >= max_attempts:
                    raise Exception("Maximum attempts exceeded.")
        # Roll the dice and display the results
        for i in range(dice_count):
            roll = Dice().roll()
            self.results_label["text"] = f"Roll {i+1}: {roll}"
            self.results_label.pack(side="bottom")