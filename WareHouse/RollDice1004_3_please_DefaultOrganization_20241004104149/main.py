# -*- coding: utf-8 -*-
'''Roll Dice App main class'''
import tkinter as tk
from dice_controller import DiceController
class RollDiceApp:
    def __init__(self, root):
        self.root = root
        self.dice_controller = DiceController()
        self.gui = None  # Create a new instance of GUI every time the user rolls the dice
    def roll_dice(self):
        '''Simulate rolling a six-sided die'''
        self.gui = GUI(self.root)  # Create a new instance of GUI every time the user rolls the dice
        result = self.dice_controller.roll_dice()
        self.gui.display_result(result)
if __name__ == "__main__":
    root = tk.Tk()
    app = RollDiceApp(root)
    root.mainloop()