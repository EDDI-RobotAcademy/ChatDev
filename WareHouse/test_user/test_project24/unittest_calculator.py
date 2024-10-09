# LANGUAGE: Python
'''
The primary entry point for running unit tests for calculator functionality
'''
import unittest
class TestCalculator(unittest.TestCase):
    def testAdd(self):
        # Arrange
        num1 = 5
        num2 = 3
        expected_result = 8
        # Act
        actual_result = Calculator.add(num1, num2)
        # Assert
        self.assertEqual(actual_result, expected_result)
    def testSubtract(self):
        # Arrange
        num1 = 10
        num2 = 4
        expected_result = 6
        # Act
        actual_result = Calculator.subtract(num1, num2)
        # Assert
        self.assertEqual(actual_result, expected_result)
    def testMultiply(self):
        # Arrange
        num1 = 7
        num2 = 9
        expected_result = 63
        # Act
        actual_result = Calculator.multiply(num1, num2)
        # Assert
        self.assertEqual(actual_result, expected_result)
    def testDivide(self):
        # Arrange
        num1 = 12
        num2 = 3
        expected_result = 4
        # Act
        actual_result = Calculator.divide(num1, num2)
        # Assert
        self.assertAlmostEqual(actual_result, expected_result)