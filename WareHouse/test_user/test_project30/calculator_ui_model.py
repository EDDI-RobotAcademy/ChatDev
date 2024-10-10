# calculator_ui_model.py
'''
This module contains classes and functions related to the calculator user interface model.
'''
import tkinter as tk
from calculator import CalculatorApp, CalculatorModel
class CalculatorUIModel:
    def __init__(self):
        self.app = CalculatorApp()
    def get_app(self):
        """
        Get the GUI application instance.
        Returns:
        tk.Frame: The Tkinter Frame representing the GUI application.
        """
        return self.app
    def create_widgets(self):
        # Create entry field for user input
        self.entry_field = tk.Entry(self.master, width=20)
        self.entry_field.grid(row=0, column=0)
        # Create buttons for arithmetic operations
        self.addButton = tk.Button(self.master, text="+", command=self.app.add_to_history)
        self.addButton.grid(row=1, column=0)
        self.subtractButton = tk.Button(self.master, text="-", command=self.app.subtract_from_history)
        self.subtractButton.grid(row=1, column=1)
        # Create button to calculate result
        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.app.calculate_and_display)
        self.calculate_button.grid(row=2, column=0)
        # Create label to display the history
        self.history_label = tk.Label(self.master, text="")
        self.history_label.grid(row=3, column=0, columnspan=2)
calculator_ui.py