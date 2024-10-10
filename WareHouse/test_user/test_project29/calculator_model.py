'''
This module provides a simple calculator model.
It allows users to perform basic arithmetic operations like addition, subtraction, multiplication, and division.
'''
class CalculatorModel:
    def __init__(self):
        """
        Initialize the calculator model with default values.
        Attributes:
            num1 (float): The first number in the calculation.
            num2 (float): The second number in the calculation.
            operator (str): The arithmetic operator (+, -, *, /).
        """
        self.num1 = 0
        self.num2 = 0
        self.operator = ''
    def set_num1(self, num):
        """
        Set the first number in the calculation.
        Args:
            num (float): The first number to set.
        """
        self.num1 = num
    def set_num2(self, num):
        """
        Set the second number in the calculation.
        Args:
            num (float): The second number to set.
        """
        self.num2 = num
    def set_operator(self, op):
        """
        Set the arithmetic operator.
        Args:
            op (str): The operator to set (+, -, *, /).
        """
        self.operator = op
    def clear(self):
        """
        Clear all values in the calculator model.
        """
        self.num1 = 0
        self.num2 = 0
        self.operator = ''
    def calculate(self):
        """
        Calculate the result of an arithmetic operation.
        Returns:
            float: The result of the arithmetic operation.
        """
        num1 = self.num1
        operator = self.operator
        num2 = self.num2
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return num1 / num2
            else:
                raise ZeroDivisionError("Cannot divide by zero")