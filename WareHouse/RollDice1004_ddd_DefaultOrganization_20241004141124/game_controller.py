#!/usr/bin/env python3
'''
DOCSTRING: File: Game controller implementation.
'''
import random  # <--- Added this line to fix the import issue
class GameController:
    def __init__(self, root):
        # Initialize the GUI widgets
        self.root = root
        # Create a new DiceRoller instance
        self.dice_roller = DiceRoller()
    def roll_dice_clicked(self):
        '''
        DOCSTRING: Handle the dice roll button click event.
        '''
        result = self.dice_roller.roll_dice()
        gui = GUI(self.root, self)
        gui.update_result(result)
    def update_gui(self, state):
        '''
        DOCSTRING: Update the GUI to reflect the current game state.
        '''
        pass  # TO DO: implement this method