# python
"""
Module containing the GUI implementation for rolling a dice.
"""
import tkinter as tk
from app_roll_dice import RollDiceApp
class DiceRollerGUI:
    def __init__(self):
        """
        Initializes a new instance of the DiceRollerGUI class.
        Attributes:
            root (tkinter.Tk): The underlying Tkinter window.
            app (RollDiceApp): The underlying dice rolling application.
        """
        self.root = tk.Tk()
        self.app = RollDiceApp()
        # Create GUI widgets
        self.result_label = tk.Label(self.root, text="")
        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        # Layout GUI widgets
        self.result_label.pack()
        self.roll_button.pack()
    def roll_dice(self):
        """
        Simulates rolling the dice and updates the GUI with the result.
        Returns:
            None
        """
        try:
            result = self.app.roll_dice()
            self.result_label.config(text=result)
        except Exception as e:
            # Handle exceptions here, e.g., display an error message to the user
            print(f"Error occurred: {e}")
            self.result_label.config(text="An unexpected error occurred.")
    def run(self):
        """
        Starts the Tkinter event loop.
        Returns:
            None
        """
        self.root.mainloop()