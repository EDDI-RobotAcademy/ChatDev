# python
'''
Calculator History File
'''
class CalculatorHistory:
    def __init__(self):
        self.history = []
    def add_history(self, item):
        self.history.append(item)
    def get_history(self):
        return str(self.history)