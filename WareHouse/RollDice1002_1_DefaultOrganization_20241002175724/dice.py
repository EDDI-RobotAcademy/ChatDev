"""
Main application entry point.
This module implements a simple graphical user interface (GUI) for rolling dice. It includes buttons and text output areas for displaying results.
"""
import tkinter as tk
from .roller import Roller  # Corrected import statement
class App(tk.Tk):
    def __init__(self):
        '''
        Initializes a new instance of the App class.
        This method sets up the root window of the application and creates necessary widgets such as buttons, labels, and entry fields for user input.
        '''
        super().__init__()
        self.title("Roll Dice")
        self.geometry("300x200")
        # Create button to roll dice
        roll_button = tk.Button(self, text="Roll Dice", command=self.roll_dice)
        roll_button.pack(pady=20)
        # Create label to display results
        result_label = tk.Label(self, text="")
        result_label.pack()
    def roll_dice(self):
        '''
        Rolls the specified number of dice and displays their results in a label.
        This method retrieves the number of dice from an entry field, rolls each die using the Roller class,
        and updates the displayed results accordingly.
        '''
        num_dice = int(self.num_dice_entry.get())  # Get the number of dice from the entry field
        if num_dice <= 0:
            result_label.config(text="Please enter a positive integer.")
            return
        roller = Roller()  # Create an instance of the Roller class
        results = roller.roll(num_dice)  # Roll the specified number of dice and get their results
        result_string = "\n".join(results)
        result_label.config(text=result_string)
# Define the Roller class
class Roller:
    def __init__(self):
        '''
        Initializes a new instance of the Roller class.
        This method sets up an empty dictionary to store multiple Dice instances, allowing for rolling multiple dice.
        '''
        self.dice = {}
    def roll(self, num_dice):
        '''
        Rolls all specified dice and returns their results.
        This method retrieves a list of dice from the `dice` dictionary, rolls each one using its own instance of the Dice class,
        and returns the results as a single string.
        Args:
            num_dice (int): The number of dice to roll.
        Returns:
            str: A string containing the results for each rolled die, separated by newline characters.
        '''
        # Roll all specified dice
        result_string = ""
        for i in range(num_dice):
            die_id = f"Die {i+1}"
            if die_id not in self.dice:
                self.dice[die_id] = Dice()  # Create a new instance of the Dice class
            result = self.dice[die_id].roll()  # Roll this die and get its result
            result_string += f"{result}\n"
        return result_string
# Define the Dice class
class Dice:
    def __init__(self):
        '''
        Initializes a new instance of the Dice class.
        This method sets up an attribute to store the rolled value, initialized to 0.
        '''
        self.rolled = False
        self.value = 0
    def roll(self):
        '''
        Rolls this die and returns its result.
        This method increments the rolled value by a random number between 1 and 6 (inclusive), simulating the roll of a standard six-sided die,
        and returns the new value as an integer.
        Returns:
            int: The result of rolling this die, which is a positive integer between 1 and 6 inclusive.
        '''
        if self.rolled:
            return self.value
        import random
        # Roll this die by generating a random number between 1 and 6 (inclusive)
        roll_result = random.randint(1, 6)
        # Update the rolled value for future rolls
        self.rolled = True
        self.value = roll_result
        return roll_result