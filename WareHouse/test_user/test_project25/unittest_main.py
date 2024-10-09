# Python
'''
Entry point for running all unit tests.
'''
import unittest
def load_tests(loader, tests, pattern):
    tests = loader.discover('.')
    return tests
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], testRunner=unittest.TextTestRunner(verbosity=2))