# calculator.py
'''
This module contains the GUI-related classes and functions.
'''
import tkinter as tk
from calculator_model import CalculatorModel, calculate_result
class CalculatorModel:
    def __init__(self):
        self.history = []
    def add_to_history(self, expression, result):
        """
        Add an entry to the history list with the given expression and result.
        Parameters:
        expression (str): The mathematical expression.
        result (int or str): The result of the calculation.
        """
        self.history.append((expression, result))
    def get_history(self):
        """
        Get all entries in the history list.
        Returns:
        list: A list of tuples containing the expressions and results.
        """
        return self.history
def calculate_result(expression):
    """
    Calculate the result of a mathematical expression.
    Parameters:
    expression (str): The mathematical expression to evaluate.
    Returns:
    int or str: The result of the calculation, or an error message if invalid input.
    """
    try:
        return eval(expression)
    except Exception as e:
        return "Error"
class CalculatorApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.model = CalculatorModel()
        self.create_widgets()
    def create_widgets(self):
        """
        Create the GUI-related widgets (entry fields and buttons) for user input.
        This method should be implemented to display a simple calculator interface.
        """
        # Entry field for user input
        self.entry_field = tk.Entry(self.master, width=20)
        self.entry_field.grid(row=0, column=0)
        # Button to calculate result
        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate_and_display)
        self.calculate_button.grid(row=0, column=1)
        # Label to display the history
        self.history_label = tk.Label(self.master, text="")
        self.history_label.grid(row=1, column=0, columnspan=2)
    def calculate_and_display(self):
        """
        Calculate and display the result based on user input.
        If the input is empty, show an error message; otherwise, perform calculation and update history.
        """
        expression = self.entry_field.get()
        # Check if the input is empty
        if not expression:
            self.history_label.config(text="Error: Please enter a valid expression.")
            return
        result = calculate_result(expression)
        self.model.add_to_history(expression, result)
        self.history_label.config(text=f"History:\n{self.get_history_string()}")
    def get_history_string(self):
        """
        Get the history list as a formatted string.
        Returns:
        str: A multiline string displaying each entry in the history list.
        """
        return "\n".join([f"{expr} = {result}" for expr, result in self.model.get_history()])