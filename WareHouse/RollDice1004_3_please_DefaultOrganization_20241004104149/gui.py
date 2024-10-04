# -*- coding: utf-8 -*-
'''Graphical User Interface class'''
import tkinter as tk
class GUI:
    def __init__(self, root):
        self.root = root
        self.result_label = None
    def setup(self):
        '''Initialize the GUI once'''
        if not hasattr(self, 'button'):  # Check if the button has already been created
            self.button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
            self.button.pack()
            self.result_label = tk.Label(self.root, text="")
            self.result_label.pack()
    def display_result(self, result):
        '''Display the result of rolling a die'''
        self.result_label.config(text=f"Result: {result}")