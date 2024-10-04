# main.py
'''Main entry point for the roll dice app'''
import tkinter as tk
from die import Dice
from roll import Roll
from game import Game
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Roll Dice App")
        self.game = Game()
        # Create GUI elements
        self.score_label = tk.Label(self.root, text="Score: 0")
        self.roll_button = tk.Button(self.root, text="Roll", command=self.on_roll)
        self.result_label = tk.Label(self.root, text="")
        # Layout GUI elements
        self.score_label.pack()
        self.roll_button.pack()
        self.result_label.pack()
    def on_roll(self):
        roll = Roll(Dice())
        result = roll.get_result()
        self.game.update_score(result)
        # Update GUI with new score and result
        self.score_label['text'] = f"Score: {self.game.get_score()}"
        self.result_label['text'] = f"Result: {result}"
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = MainApp()
    app.run()