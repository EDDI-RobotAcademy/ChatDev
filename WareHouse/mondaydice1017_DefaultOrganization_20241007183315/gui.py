# LANGUAGE: Python
# DOCSTRING: User interface: `GUI`
'''
gui.py
User interface for the dice rolling game.
'''
import tkinter as tk
from game_logic import GameLogic
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.game_logic = GameLogic()
    def create_widgets(self):
        self.roll_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.score_label = tk.Label(self.root, text="Current Score: ")
        self.all_scores_label = tk.Label(self.root, text="All Rolled Scores: ")
        self.roll_button.pack()
        self.score_label.pack()
        self.all_scores_label.pack()
    def roll_dice(self):
        self.game_logic.roll_dice()
        self.update_score_labels()
    def update_score_labels(self):
        self.score_label.config(text=f"Current Score: {self.game_logic.current_score}")
        self.all_scores_label.config(text=f"All Rolled Scores: {', '.join(map(str, self.game_logic.all_rolled_scores))}")
    def run(self):
        self.create_widgets()
        self.root.mainloop()