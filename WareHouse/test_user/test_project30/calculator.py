# calculator.py
'''
This module contains the GUI-related classes and functions.
'''
import tkinter as tk
class CalculatorModel:
    def __init__(self):
        self.history = []
    def add_to_history(self, expression, result):
        self.history.append((expression, result))
    def get_history(self):
        return self.history
def calculate_result(expression):
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
        # Create entry fields and buttons for user input
        pass  # We'll implement this in the next file
import math
from calculator_model import calculate_result