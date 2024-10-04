# main.py
'''
Roll Dice App - Main Application
'''
import tkinter as tk
from dice_roller import DiceRoller
from dashboard import Dashboard
from statistics_calculator import StatisticsCalculator
class RollDiceApp:
    def __init__(self, root):
        self.root = root
        self.dice_roller = DiceRoller()
        self.dashboard = Dashboard(self.root)
        self.statistics_calculator = StatisticsCalculator()
    def run(self):
        self.dashboard.display()
        self.root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = RollDiceApp(root)
    app.run()