# main.py
'''Main file that initializes and runs the Roll Dice App.'''
from tkinter import Tk, Label, Button, Entry, StringVar
from dice import roll_die, RollResult  # Modified import statement
from game_manager import GameManager
import random
class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Roll Dice App")
        # Initialize GUI components
        self.label = Label(self.root, text="Enter number of sides: ")
        self.label.pack()
        self.entry = Entry(self.root)
        self.entry.pack()
        self.button = Button(self.root, text="Roll", command=self.roll_dice)
        self.button.pack()
        self.result_label = Label(self.root, text="")
        self.result_label.pack()
    def roll_dice(self):
        try:
            num_sides = int(self.entry.get())
            if num_sides <= 0:
                self.result_label.config(text="Please enter a positive whole number for the number of sides.")
                return
            dice = roll_die(num_sides)  # Modified to use roll_die()
            result = dice
            # Display roll results with visual separation
            self.display_roll_result(result, f"You rolled: {result.value} ({result.rolls})")
        except ValueError:
            # Handle invalid input, e.g., display an error message or prompt the user to re-enter the value
            self.result_label.config(text="Invalid input. Please enter a whole number.")
        except TypeError as te:
            self.result_label.config(text=f"Error: {te}")
    def run(self):
        self.root.mainloop()
    def display_roll_result(self, result, message):
        # Create a new Label with the roll result and pack it
        roll_label = Label(self.root, text=message)
        roll_label.pack()
        # Add a small gap to separate the labels
        Label(self.root).pack()
if __name__ == "__main__":
    gui = GUI()
    game_manager = GameManager()
    gui.run()