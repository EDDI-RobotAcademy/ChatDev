# python
'''
Calculator Calculations File
'''
class CalculatorCalculations:
    def __init__(self):
        self.history = []
    def add_calculation(self, calculation):
        self.history.append(calculation)
    def clear_last_calculation(self):
        if len(self.history) > 0:
            del self.history[-1]
    def reset_all_calculations(self):
        self.history.clear()
    def perform_calculation(self, calculation):
        """
        Perform a mathematical operation based on the input string.
        Args:
            calculation (str): The input string containing the mathematical expression.
        Returns:
            result: The result of the mathematical operation.
        """
        try:
            return eval(calculation)
        except Exception as e:
            # Handle any exceptions that occur during evaluation
            print(f"Error evaluating calculation: {e}")