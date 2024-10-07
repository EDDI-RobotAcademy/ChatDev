"""
Unit test for app module.
"""
import unittest
from app import App  # noqa: F401
class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()
    def test_run(self):
        # Verify that the GUI is running correctly
        with self.assertRaises(SystemExit):
            self.app.run()