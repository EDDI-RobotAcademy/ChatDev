"""
Unit test for gui module.
"""
import unittest
from app import GUI  # noqa: F401
class TestGUI(unittest.TestCase):
    def setUp(self):
        self.gui = GUI()
    def test_widgets_created(self):
        # Verify that three widgets are created by the GUI
        self.assertEqual(len(self.gui.widgets), 3)
    def test_additional_test_cases(self):
        # Additional test cases to cover other aspects of the GUI's behavior
        self.assertIsInstance(self.gui.title_label, QLabel)