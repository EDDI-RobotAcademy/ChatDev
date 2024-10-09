# LANGUAGE: Python
'''
DOCSTRING: Calculator logic module. Provides methods for performing mathematical operations.
'''
class CalculatorLogic:
    def __init__(self):
        pass
    # Implemented methods
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2
    # Additional methods
    def power(self, base, exponent):
        return base ** exponent
    def square_root(self, number):
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return number ** 0.5
    def modulo(self, dividend, divisor):
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend % divisor
    # Extra methods for completeness
    def factorial(self, num):
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        elif num == 0 or num == 1:
            return 1
        else:
            return num * self.factorial(num-1)
    def absolute_value(self, number):
        return abs(number)
    def exponential(self, base, exponent):
        if exponent < 0:
            raise ValueError("Exponent cannot be negative for exponential operation")
        return base ** exponent
    def cube_root(self, number):
        if number < 0:
            raise ValueError("Cannot calculate cube root of negative number")
        return round(number ** (1. / 3)), 3