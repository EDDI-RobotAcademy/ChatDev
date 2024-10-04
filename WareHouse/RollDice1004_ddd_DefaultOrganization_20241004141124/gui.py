#!/usr/bin/env python3
'''
DOCSTRING: File: Graphical user interface implementation.
'''
import tkinter as tk
class GUI:
    def __init__(self, root, game_controller):
        # Create a new Tk instance (the root window)
        self.root = root
        # Initialize the GUI widgets
        self.roll_button = tk.Button(self.root, text="Roll Dice", command=game_controller.roll_dice_clicked)
        self.result_label = tk.Label(self.root, text="")
        # Pack the GUI widgets
        self.roll_button.pack()
        self.result_label.pack()
    def update_result(self, result):
        '''
        DOCSTRING: Update the GUI with the dice roll result.
        '''
        self.result_label.config(text=f"You rolled: {result}")