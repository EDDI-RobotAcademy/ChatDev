# LANGUAGE: Python
'''
Calculator class to perform arithmetic operations
'''
from utils import Calculator
class Calculator:
    @staticmethod
    def add(num1, num2):
        return num1 + num2
    @staticmethod
    def subtract(num1, num2):
        return num1 - num2
    @staticmethod
    def multiply(num1, num2):
        return num1 * num2
    @staticmethod
    def divide(num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError as zde:
            raise zde