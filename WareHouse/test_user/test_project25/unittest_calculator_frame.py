# Python
'''
Unit test cases for the CalculatorFrame class in calculator.py.
'''
import unittest
from calculator import CalculatorFrame
class TestCalculatorFrame(unittest.TestCase):
    def setUp(self):
        self.frame = CalculatorFrame(None)
    def test_create_widgets(self):
        # Test that create_widgets method creates display label and buttons
        self.frame.create_widgets()
        self.assertIsNotNone(self.frame.display_label)
        for i in range(10):
            button = self.frame.winfo_children()[i]
            self.assertIsInstance(button, CalculatorFrame.CalcButton)
    def test_append_to_display(self):
        # Test append_to_display method appends value to display label
        self.frame.append_to_display("1")
        self.assertEqual(self.frame.display_label.cget("text"), "1")
    def test_calculate_division_by_zero(self):
        # Test calculate method handles division by zero error
        self.frame.append_to_display("10 / 0")
        self.frame.calculate()
        self.assertEqual(self.frame.display_label.cget("text"), "Error: Division by zero")
    def test_calculate_invalid_syntax(self):
        # Test calculate method raises exception for invalid syntax
        with unittest.mock.patch.object(self.frame.aseval, side_effect=SyntaxError()):
            self.frame.append_to_display("(10 / 0)")
            self.frame.calculate()
            self.assertEqual(self.frame.display_label.cget("text"), "Error: Invalid syntax")
    def test_clear_display(self):
        # Test clear method clears display label
        self.frame.append_to_display("1")
        self.frame.clear()
        self.assertIsNone(self.frame.display_label.cget("text"))