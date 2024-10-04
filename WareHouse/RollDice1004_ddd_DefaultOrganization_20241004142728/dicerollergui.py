# gui_main.py
"""
Module containing the graphical user interface (GUI) implementation.
"""
import tkinter as tk
from app_roll_dice import RollDiceApp
class DiceRollerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.app = RollDiceApp()
        # Create GUI widgets
        self.result_label = tk.Label(self.root, text="")
        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        # Layout GUI widgets
        self.result_label.pack()
        self.roll_button.pack()
    def roll_dice(self):
        result = self.app.roll_dice()
        self.result_label.config(text=result)
    def run(self):
        self.root.mainloop()