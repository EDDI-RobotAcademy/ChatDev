'''
Main entry point for unit tests.
'''
import unittest
from unittest_calculator import TestCalculator
def run_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromName('TestCalculator')
    unittest.TextTestRunner(verbosity=2).run(test_suite)
if __name__ == "__main__":
    run_tests()