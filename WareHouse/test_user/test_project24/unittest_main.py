# LANGUAGE: Python
'''
The primary entry point for running all unit tests
'''
import unittest
from unittest_calculator import TestCalculator
from unittest_math_utils import TestMathUtils
class TestAll(unittest.TestCase):
    def test_all(self):
        self.assertTrue(all([TestCalculator().testAdd(),
                              TestCalculator().testSubtract(),
                              TestCalculator().testMultiply(),
                              TestCalculator().testDivide(),
                              TestMathUtils().test_arithmetic_operation(),
                              TestMathUtils().test_arithmetic_operation_subtract()]))