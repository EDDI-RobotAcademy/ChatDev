# unittest_gui_main.py
import unittest
from gui_main import DiceRollerGUI
class TestDiceRollerGUIGUIImplementation(unittest.TestCase):
    def setUp(self):
        # Arrange: Create a DiceRollerGUI instance for each test
        self.gui = DiceRollerGUI()
    def test_roll_dice_button_click(self):
        # Arrange: Set up the GUI and click the roll button
        self.gui.roll_button.config(command=lambda: self.test_roll_dice_button_click())
        self.gui.root.after(1)  # Simulate a brief delay to allow events to propagate
        # Act: Call the roll_dice method on the GUI instance
        result = self.gui.roll_dice()
        # Assert: Verify that the actual result matches the expected outcome
        self.assertIsInstance(result, str)
        self.assertIn('rolled', result)
    def test_roll_dice_button_click_multiple_times(self):
        # Arrange: Set up the GUI and click the roll button multiple times
        for _ in range(5):
            self.gui.roll_button.config(command=lambda: self.test_roll_dice_button_click())
            self.gui.root.after(1)  # Simulate a brief delay to allow events to propagate
            result = self.gui.roll_dice()
            self.assertIsInstance(result, str)