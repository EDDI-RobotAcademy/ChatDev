# python
'''
Graphical User Interface for Roll Dice App
'''
import tkinter as tk
from .RollDiceService import RollDiceService
class RollDiceGUI:
    def __init__(self):
        self.service = RollDiceService()
        self.root = tk.Tk()
        self.root.title("Roll Dice")
        # Create labels and entry fields
        self.label_result = tk.Label(self.root, text="Result:")
        self.label_result.pack()
        self.entry_label = tk.Label(self.root, text="Number of dice rolls:")
        self.entry_label.pack()
        self.entry_dice_rolls = tk.Entry(self.root)
        self.entry_dice_rolls.insert(0, "1")
        self.entry_dice_rolls.pack()
        # Create button to roll dice
        self.button_roll = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.button_roll.pack()
        # Create label to display result
        self.label_result_value = tk.Label(self.root, text="")
        self.label_result_value.pack()
    def roll_dice(self):
        num_rolls = int(self.entry_dice_rolls.get())
        results = []
        for _ in range(num_rolls):
            results.append(str(self.service.roll_dice()))
        self.label_result_value['text'] = ", ".join(results)
    def run(self):
        self.root.mainloop()