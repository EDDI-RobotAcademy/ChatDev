# python
'''
Calculator GUI File
'''
import tkinter as tk
from .calculator_app import CalculatorApp
from calculator_calculations import CalculatorCalculations
from calculator_history import CalculatorHistory
class CalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)
        self.entry_label = tk.Label(self.root, text="Enter a calculation:")
        self.entry_label.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        self.history_label = tk.Label(self.root, text="")
        self.history_label.pack()
    def perform_calculation(self):
        try:
            result = eval(self.entry_label.cget("text"))
            self.result_label.config(text="Result: " + str(result))
            history = CalculatorHistory()
            history.add_history(str(result))
            self.history_label.config(text=history.get_history())
        except Exception as e:
            print(f"Error evaluating calculation: {e}")