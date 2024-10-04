# roll_dice_app.py (Python)
'''
Represents a Roll Dice App instance.
'''
from tkinter import Button, Label
from statistics_calculator import StatisticsCalculator
from dice import Dice
from roll import Roll
class RollDiceApp:
    def __init__(self, root):
        self.root = root
        # Initialize GUI components
        self.result_label = Label(self.root, text="Result: ")
        self.roll_button = Button(self.root, text="Roll", command=self.roll_dice)
        # Initialize statistics calculator and dice/roll objects
        self.stats_calculator = StatisticsCalculator()
        self.dice = Dice()
        self.rolls = []
    def roll_dice(self):
        # Roll the dice and store result in history
        try:
            roll_result = self.dice.roll()
            self.rolls.append(Roll(roll_result))
            # Update GUI to display new result
            self.result_label['text'] = f"Result: {roll_result}"
            # Calculate and update statistics display
            stats_text = self.stats_calculator.calculate(self.rolls)
            self.stats_label['text'] = stats_text
        except Exception as e:
            print(f"Error rolling dice: {e}")
    def run(self):
        # Configure GUI layout
        self.result_label.pack()
        self.roll_button.pack()
# Initialize statistics label to display calculations
self.stats_label = Label(self.root, text="Statistics: ")
from tkinter import Label