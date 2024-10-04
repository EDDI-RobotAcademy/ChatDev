# python
'''
Main entry point for the Roll Dice App.
'''
from dice_app import DiceApp
import tkinter as tk
class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.dice_app = DiceApp(self.root)
        self.dice_app.mainloop()
if __name__ == "__main__":
    main = Main()