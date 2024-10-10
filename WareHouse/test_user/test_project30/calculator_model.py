# calculator_model.py
'''
This module contains classes and functions related to the calculator model.
'''
class CalculatorModel:
    def __init__(self):
        self.history = []
    def calculate_result(self, expression):
        try:
            # Your implementation here
            return eval(expression)
        except Exception as e:
            raise e
    def add_to_history(self, expression):
        self.history.append((expression, "Not calculated yet"))
    def subtract_from_history(self, expression):
        self.add_to_history(expression)
    def get_history(self):
        """
        Get all entries in the history list.
        Returns:
        list: A list of tuples containing the expressions and results.
        """
        return self.history
def calculate_and_display(expression):
    try:
        result = CalculatorModel().calculate_result(expression)
        print(result)
    except Exception as e:
        print(f"Error: {e}")