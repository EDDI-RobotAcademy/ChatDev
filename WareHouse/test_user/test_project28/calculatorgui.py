# python
'''
Calculator GUI File
'''
import tkinter as tk
class CalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        # Removed relative import and used absolute path instead
    def perform_calculation(self, calculation_str):
        try:
            result = eval(calculation_str)
            print(f"Result: {result}")
            self.history.add_calculation_to_history(calculation_str)
        except Exception as e:
            print(f"Error evaluating calculation: {e}")