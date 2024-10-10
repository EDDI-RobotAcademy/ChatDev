# calculator_model.py
'''
This module contains classes and functions related to the calculator model.
'''
from calculator import CalculatorModel
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