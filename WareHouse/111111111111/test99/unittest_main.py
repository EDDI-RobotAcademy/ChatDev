'''
Main entry point for unit tests.
'''
import unittest
from unittest_add import TestAddFunctionality
from unittest_subtract import TestSubtractFunctionality
from unittest_multiply import TestMultiplyFunctionality
from unittest_divide import TestDivideFunctionality
def run_all_tests():
    unittest.main()
if __name__ == "__main__":
    run_all_tests()