# python
'''
Unit Test Case for Main Entry Point
This file contains test cases to ensure the correct functionality of main entry point.
'''
import unittest
from calculator_logic import CalculatorLogic
class TestMain(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorLogic()
    def test_main_initiates_gui_correctly(self):
        # Arrange: Create a new instance of calculator gui
        from calculator_gui import CalculatorGUI  # Corrected import statement
        gui = CalculatorGUI()  
        # Act: Call main entry point function (no arguments)
        self.calculator.main()
        # Assert: Verify that the GUI is initialized correctly
        self.assertIsNotNone(gui.buttons)
if __name__ == '__main__':
    unittest.main()