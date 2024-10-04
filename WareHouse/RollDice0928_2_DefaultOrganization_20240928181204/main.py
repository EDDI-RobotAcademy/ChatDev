from game_ui import GameUI  # Corrected import statement
import tkinter as tk
import random
class ScoreManager:
    def __init__(self):
        self.total_score = 0
    def update_score(self, new_score):
        self.total_score += new_score
    def get_total_score(self):
        return self.total_score
def main():
    root = Tk()
    gui_instance = GameUI(root)
    label = gui_instance.create_window()
    score_manager = ScoreManager()
    dice = Dice()
    root.mainloop()
if __name__ == "__main__":
    main()