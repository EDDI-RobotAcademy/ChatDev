'''
This module provides a simple button handler.
It creates buttons for the calculator and handles their clicks.
'''
from calculator_model import CalculatorModel
class ButtonHandler:
    def __init__(self):
        """
        Initialize the button handler with an empty calculator model.
        Attributes:
            model (CalculatorModel): The calculator model to use.
        """
        self.model = CalculatorModel()
    def handle_click(self, button):
        """
        Handle a click on the specified button.
        Args:
            button (str): The button that was clicked (+, -, *, /, =).
        """
        if button == '=':
            try:
                result = self.model.calculate()
                print(f"Result: {result}")
            except ZeroDivisionError as e:
                print(str(e))
        elif button in ['+', '-', '*', '/']:
            self.model.set_operator(button)
        else:
            num = float(button)
            if button == '0':
                self.model.set_num1(0)
            else:
                self.model.set_num1(num)
    def get_model(self):
        """
        Get the current state of the calculator model.
        Returns:
            CalculatorModel: The current state of the calculator model.
        """
        return self.model