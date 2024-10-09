# LANGUAGE: Python
'''
DOCSTRING: Main module for unit testing.
Runs the test modules in a single run.
'''
import unittest
if __name__ == '__main__':
    unittest.main(module='calculation_unittest', exit=False)
    unittest.main(module='gui_unittest', exit=False)