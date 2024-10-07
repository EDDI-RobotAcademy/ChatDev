#!/usr/bin/env python3
"""
Unit Test File for gui.py
This file contains unit test cases for the GUI class.
"""
import unittest
from gui import GUI
class TestGUI(unittest.TestCase):
    def setUp(self):
        self.gui = GUI()
    def test_create_widgets(self):
        self.gui.create_widgets()
        self.assertEqual(len(self.gui.root.winfo_children()), 3)