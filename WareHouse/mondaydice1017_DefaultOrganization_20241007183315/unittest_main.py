# unittest_test_gui.py
"""
DOCSTRING: Unit Tests for GUI Class
"""
import unittest
from gui import GUI  # Modified import statement
class TestGUI(unittest.TestCase):
    def setUp(self):
        self.gui = GUI()
    def test_widgets_created_with_invalid_input(self):
        # Simulate invalid input scenario
        self.gui.input_widget.set_text("invalid")
        self.assertEqual(len(self.gui.widgets), 3)  # Correct widget count despite invalid input
if __name__ == '__main__':
    unittest.main()