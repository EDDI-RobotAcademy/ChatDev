#!/usr/bin/env python3
"""
Unit Test File for app.py
This file contains unit test cases for the App class.
"""
import unittest
from app import App
class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()
    def test_run(self):
        self.app.run()
        # Add assertions to verify the GUI is running correctly