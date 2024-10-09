# python
'''
Calculator App Main File
'''
import tkinter as tk
from calculator_calculations import CalculatorCalculations
from calculator_history import CalculatorHistory
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.history = CalculatorHistory()
        self.calculations = CalculatorCalculations()
# This file will contain the GUI and main functionality of our app