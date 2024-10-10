"""
This module contains unit tests for the ButtonHandler class.
"""
import unittest
from button_handler import ButtonHandler
class TestButtonHandler(unittest.TestCase):
    def test_handle_click(self):
        # Test handling a valid click event
        handler = ButtonHandler()
        result = handler.handle_click("button_1")
        self.assertEqual(result, "Button 1 clicked")
        # Test handling an invalid click event (non-existent button)
        handler = ButtonHandler()
        with self.assertRaises(ValueError):
            handler.handle_click("button_nonexistent")
    def test_get_model(self):
        # Test getting the calculator model
        handler = ButtonHandler()
        model = handler.get_model()
        self.assertIsInstance(model, CalculatorModel)
class TestButtonHandlerErrors(unittest.TestCase):
    def test_handle_click_error(self):
        # Test handling an invalid click event (non-string button name)
        handler = ButtonHandler()
        with self.assertRaises(TypeError):
            handler.handle_click(42)
    def test_get_model_error(self):
        # Test getting the calculator model when it doesn't exist
        handler = ButtonHandler()
        with self.assertRaises(ValueError):
            handler.get_model()