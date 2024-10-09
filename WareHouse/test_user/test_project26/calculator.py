# python
'''
Calculator Logic Implementation
'''
import numexpr as ne  # Import the safer alternative for evaluating mathematical expressions
class Calculator:
    def __init__(self):
        self.expression = ""
        self.result = 0
    def calculate(self, expression):
        '''
        Perform a simple arithmetic calculation on the given expression.
        Args:
            expression (str): The mathematical expression to evaluate.
        Returns:
            int or float: The result of the calculation.
        '''
        try:
            result = ne.evaluate(expression)  # Use numexpr to safely evaluate expressions
            return result
        except Exception as e:
            print(f"Error occurred during calculation: {e}")
            return None
    def clear(self):
        self.expression = ""
        self.result = 0