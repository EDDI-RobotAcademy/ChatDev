# LANGUAGE: Python
'''
The primary entry point for running unit tests for math utility functions
'''
import unittest
class TestMathUtils(unittest.TestCase):
    def test_arithmetic_operation(self):
        # Arrange
        num1 = 5
        num2 = 3
        expected_result = 8
        # Act
        actual_result = MathUtils.arithmetic_operation(num1, num2)
        # Assert
        self.assertEqual(actual_result, expected_result)
    def test_arithmetic_operation_subtract(self):
        # Arrange
        num1 = 10
        num2 = 4
        expected_result = 6
        # Act
        actual_result = MathUtils.arithmetic_operation_subtract(num1, num2)
        # Assert
        self.assertEqual(actual_result, expected_result)