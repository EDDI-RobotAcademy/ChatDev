# python
'''
Calculator History File
'''
class CalculatorHistory:
    def __init__(self):
        self.history = []
    def add_calculation_to_history(self, calculation):
        self.history.append(calculation)
    def display_history(self):
        return '\n'.join(self.history)