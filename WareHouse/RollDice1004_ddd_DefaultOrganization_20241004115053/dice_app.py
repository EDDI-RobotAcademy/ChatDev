# python
'''
The core application logic for the Roll Dice App.
Contains the `DiceApp` class which handles user interactions and dice roll results.
'''
import tkinter as tk
class DiceApp:
    def __init__(self, root):
        self.root = root
        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()
        self.roll_button = tk.Button(root, text="Roll", command=self.roll_dice)
        self.roll_button.pack()
    def roll_dice(self):
        import random
        result = random.randint(1, 6) * 2 + random.randint(1, 6)
        self.result_label['text'] = f"Result: {result}"
class Dashboard:
    def __init__(self, root):
        self.root = root
        self.dashboard_label = tk.Label(root, text="Dashboard")
        self.dashboard_label.pack()
# Add a method to update the dashboard with real-time results
def update_dashboard(self, result):
    self.dashboard_label['text'] = f"Last Roll: {result}"