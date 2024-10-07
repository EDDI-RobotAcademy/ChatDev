# LANGUAGE: Python3
"""
DOCSTRING:
Main function to run the game.
"""
import tkinter as tk
from suggested_improvements import SuggestedImprovements
from dice_roller import DiceRoller
class Main:
    def __init__(self):
        root = tk.Tk()
        self.game = Game()
        my_gui = SuggestedImprovements(self.game)
        button = Button(root, text="Reset", command=lambda: my_gui.on_reset_game_button_click(DiceRoller()))
        button.pack()
        label = Label(root, text="Scores:")
        label.pack()
        root.mainloop()
if __name__ == "__main__":
    Main()