# unittest_main.py
import unittest
from tkinter import Tk, ttk
class TestMain(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
    def tearDown(self):
        self.root.destroy()
    def test_init_valid_input(self):
        # Arrange: Valid input (default sides=6)
        # Act:
        # No action is required, as we're testing the constructor.
        # Assert:
        self.assertIsInstance(self.root, Tk)
    def test_run_app(self):
        # Arrange: Create a Tk instance
        main_app = MainApp(self.root)
        # Assert:
        self.assertIsNotNone(main_app.root.winfo_exists())
    def test_roll_dice_large_sides(self):
        # Arrange: Large number of sides (1000) for roll_dice method
        self.root.roll_dice(1000)
        # Act: Test the roll_dice method with large number of sides
        # Assert:
        # Assuming roll_dice method returns the rolled value and displays it in the label widget
        current_roll_label = self.root.get_current_roll_label()
        self.assertIn("Current Roll:", current_roll_label['text'])
    def test_quit_button_click(self):
        # Arrange: Create a Tk instance
        main_app = MainApp(self.root)
        # Act: Simulate clicking the "Quit" button
        # Assert:
        self.assertTrue(main_app.quit())
if __name__ == '__main__':
    unittest.main()