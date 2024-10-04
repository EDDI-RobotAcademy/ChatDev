"""
Main application entry point.
This module implements a simple graphical user interface (GUI) for rolling dice. It includes buttons and text output areas for displaying results.
"""
import tkinter as tk

from dice import Dice  # Import the Dice class from dice.py
class App(tk.Tk):
    def __init__(self):
        """
        Initializes a new instance of the App class.
        This method sets up the main window and its components, including labels, entries, buttons, and text output areas.
        """
        super().__init__()
        self.title("Roll Dice App")
        self.geometry("300x200")
        # Create UI elements
        self.dice_label = tk.Label(self, text="Enter number of dice to roll:")
        self.dice_entry = tk.Entry(self)
        self.roll_button = tk.Button(self, text="Roll", command=self.roll_dice)
        self.output_text = tk.Text(self)
        # Create a Roller instance
        self.roller = Roller()
    def roll_dice(self):
        """
        Handles the button click event for rolling dice.
        This method retrieves the number of dice to roll from the entry field, checks if it's within valid range (1-6),
        rolls the dice using the `Dice` class, and displays the results in the text output area.
        """
        try:
            num_dice = int(self.dice_entry.get())
            if num_dice < 1 or num_dice > 6:
                raise ValueError("Number of dice must be between 1 and 6.")
            # Roll the specified number of dice
            results = []
            for _ in range(num_dice):
                result = self.roller.roll()
                results.append(result)
            # Display the roll results
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "\n".join(results))
        except ValueError as e:
            # Handle invalid input (e.g., non-numeric value or out-of-range number of dice)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, str(e))
if __name__ == "__main__":
    app = App()
    app.mainloop()