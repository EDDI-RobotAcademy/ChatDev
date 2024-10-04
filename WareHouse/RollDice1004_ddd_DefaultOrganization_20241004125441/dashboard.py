# dashboard.py
'''
Dashboard Class - Displays real-time information and statistics.
'''
from tkinter import Label, Button, Frame
class Dashboard:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.label = Label(self.root, text="Roll Dice App")
        self.button = Button(self.root, text="Roll Dice", command=self.on_roll_dice_click)
    def display(self):
        '''
        Displays the Dashboard on the screen.
        '''
        self.label.pack()
        self.button.pack()
        self.frame.pack()
    def on_roll_dice_click(self):
        '''
        Handles the button click event by rolling a dice and updating the label text.
        '''
        dice_roller = DiceRoller()
        rolled_dice_value = dice_roller.get_rolled_dice_value()
        self.label['text'] = f"Rolled: {rolled_dice_value}"