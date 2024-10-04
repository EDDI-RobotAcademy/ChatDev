# game.py
'''
Game logic to update the score.
'''
import tkinter as tk
from dice import Dice
class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.score_manager = ScoreManager()
        self.dice = Dice()
    def play_game(self):
        # Get user input for number of rolls
        num_rolls = int(input("Enter the number of rolls: "))
        rolls = [self.dice.roll() for _ in range(num_rolls)]
        result = self.dice.calculate_result(rolls)
        # Update score manager with new score
        self.score_manager.update_score(result)
        # Display updated score to user
        self.root.title(f"Score: {self.score_manager.get_total_score()}")
    def run(self):
        self.play_game()
        self.root.mainloop()
game = Game()
game.run()