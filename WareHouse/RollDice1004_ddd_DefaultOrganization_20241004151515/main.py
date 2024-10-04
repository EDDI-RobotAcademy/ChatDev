# python
'''
DOCSTRING:
This is the main entry point of the Roll Dice App.
'''
import tkinter as tk, tkinter.ttk as ttk
from roll_dice_app import RollDiceApp
class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.roll_dice_app = RollDiceApp(self.root)
    def start(self):
        self.roll_dice_app.update_label()
        self.root.mainloop()
if __name__ == "__main__":
    main = Main()
    main.start()