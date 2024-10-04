# python
'''
DOCSTRING:
This module defines the RollDiceApp class, which represents the main application.
'''
from tkinter import ttk
from dice import Dice
import tkinter.messagebox as messagebox
class RollDiceApp:
    def __init__(self, root):
        self.root = root
        self.dice = Dice()
        self.label = ttk.Label(root, text="Roll Dice App")
        self.label.pack()
        roll_button = ttk.Button(root, text="Roll Dice", command=self.roll_dice)
        roll_button.pack()
        quit_button = ttk.Button(root, text="Quit", command=self.quit)
        quit_button.pack()
        sides_label = ttk.Label(root, text="Number of Sides:")
        sides_label.pack()
        self.sides_entry = ttk.Entry(root)
        self.sides_entry.pack()
    def update_label(self):
        self.label['text'] = f"Current Roll: {self.dice.roll_value}"
        self.root.after(1000, self.update_label)
    def roll_dice(self):
        try:
            sides = int(self.sides_entry.get())
            if sides > 500: # added a limit to handle large numbers of sides
                messagebox.showerror("Error", "Number of sides exceeds the maximum value")
                return
            self.dice = Dice(sides)
            self.dice._generate_roll()  # Call _generate_roll directly instead of roll()
            self.label['text'] = f"Current Roll: {self.dice.roll_value}"
        except ValueError:
            messagebox.showerror("Error", "Invalid number of sides")
    def quit(self):
        answer = messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if answer:
            self.root.destroy()