# gui_manager.py
'''The GUIManager class manages the graphical user interface.'''
import tkinter as tk
class GUIManager:
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Roll Dice")
        self.button = tk.Button(self.root, text="Roll", command=self.handle_roll)
        self.button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
    def handle_roll(self):
        result = roll_dice_app.roll_dice()
        self.result_label['text'] = str(result)