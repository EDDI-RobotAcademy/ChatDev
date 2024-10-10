# calculator_ui_model.py
'''
This module contains classes and functions related to the calculator user interface model.
'''
from calculator import CalculatorApp
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