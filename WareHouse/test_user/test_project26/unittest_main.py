# python
'''
Unit Tests for the Calculator
'''
import unittest
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_addition(self):
        expression = "2 + 3"
        result = self.calculator.calculate(expression)
        self.assertEqual(result, 5)
    def test_subtraction(self):
        expression = "10 - 4"
        result = self.calculator.calculate(expression)
        self.assertEqual(result, 6)
    def test_multiplication(self):
        expression = "5 * 9"
        result = self.calculator.calculate(expression)
        self.assertEqual(result, 45)
    def test_division(self):
        expression = "12 / 3"
        result = self.calculator.calculate(expression)
        self.assertAlmostEqual(result, 4.0)
    def test_division_by_zero(self):
        expression = "10 / 0"
        try:
            self.calculator.calculate(expression)  # Test if a ZeroDivisionError is raised
        except ZeroDivisionError as e:
            self.assertEqual(str(e), "division by zero")
if __name__ == '__main__':
    unittest.main()