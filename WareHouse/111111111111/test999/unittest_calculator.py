'''
Calculator class unit tests.
'''
import unittest
class TestCalculator(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)
    def test_subtract(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(1, 2), -1)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(0, 0), 0)
    def test_multiply(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(1, 2), 2)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(0, 0), 0)
    def test_divide(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(1, 2), 0.5)
        self.assertEqual(calculator.divide(-1, 1), -1)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 1)
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b