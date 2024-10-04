# Importing necessary modules
import tkinter as tk
from models import Dice
from services import RollService
class RollDiceApp:
    def __init__(self, root):
        self.root = root
        self.dice = Dice()
        self.roll_service = RollService()
        # Set up GUI components
        self.label = tk.Label(self.root, text="Roll the dice!")
        self.button = tk.Button(self.root, text="Roll", command=self.roll_dice)
        self.result_label = tk.Label(self.root)
        # Layout GUI components
        self.label.pack()
        self.button.pack()
        self.result_label.pack()
    def roll_dice(self):
        result = self.roll_service.roll_dice(self.dice)
        self.result_label.config(text=f"You rolled: {result['value']}")
if __name__ == "__main__":
    root = tk.Tk()
    app = RollDiceApp(root)
    root.mainloop()