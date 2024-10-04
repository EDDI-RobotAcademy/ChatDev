# FILENAME: dice_gui.py
# LANGUAGE: Python
'''
GUI class for displaying the rolled dice result
The DiceGui class encapsulates the logic for creating a GUI to display the rolled dice result.
It ensures that the "Roll Dice" button command is valid and updates the displayed result accordingly.
References:
    * tkinter documentation: https://docs.python.org/3/library/tkinter.html
'''
import tkinter as tk
class DiceGui:
    def __init__(self):
        '''
        Initialize the GUI class with a Tkinter window.
        Attributes:
            self.root (tk.Tk): The Tkinter window instance.
        '''
        self.root = tk.Tk()
        self.result_label = tk.Label(self.root, text="")
        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.history_listbox = tk.Listbox(self.root)
    def roll_dice(self):
        '''
        Roll the dice and update the displayed result.
        Note:
            * This method uses the RollDiceDomain class to simulate rolling two virtual dice.
            * It then updates the displayed result in the GUI accordingly.
        '''
        domain = RollDiceDomain()
        result = domain.roll_dice()
        # Update the displayed result
        self.result_label.config(text=result)
        # Append the rolled dice result to the history listbox
        self.history_listbox.insert(tk.END, result)
    def run(self):
        '''
        Run the GUI event loop.
        Note:
            * This method ensures that the GUI remains responsive and updates accordingly.
        '''
        self.result_label.pack()
        self.roll_button.pack()
        self.history_listbox.pack()
# Example usage:
gui = DiceGui()
gui.run()
self.root.mainloop()