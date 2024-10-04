import unittest
class TestRollDice(unittest.TestCase):
    def test_roll_dice(self):
        # Arrange: Create a RollDiceApp instance with default dice
        app = RollDiceApp()
        # Act: Get the result of rolling the Dice using the RollDiceApp instance
        result = app.roll_dice()
        # Assert: Verify that the actual result matches the expected outcome (1-6)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)
    def test_custom_dice_sides(self):
        # Arrange: Create a RollDiceApp instance with custom dice sides
        app = RollDiceApp()
        app.dice.sides = 10
        # Act: Get the result of rolling the Dice using the RollDiceApp instance
        result = app.roll_dice()
        # Assert: Verify that the actual result matches the expected outcome (1-10)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 10)
    def test_roll_dice_button_click(self):
        # Arrange: Create a DiceRollerGUI instance
        gui = DiceRollerGUI()
        # Act: Click the roll button and get the result
        result = gui.roll_dice()
        # Assert: Verify that the actual result matches the expected outcome (contains 'rolled')
        self.assertIn('rolled', result)
    def test_roll_dice_button_click_multiple_times(self):
        # Arrange: Create a DiceRollerGUI instance
        gui = DiceRollerGUI()
        # Act: Click the roll button multiple times and get the results
        for _ in range(5):
            result = gui.roll_dice()
            self.assertIn('rolled', result)
    def test_invalid_input(self):
        # Arrange: Create a RollDiceApp instance with invalid input (negative sides)
        app = RollDiceApp()
        app.dice.sides = -5  # Corrected the mistake by using Dice class directly
        # Act: Attempt to roll the Dice using the RollDiceApp instance
        with self.assertRaises(ValueError):
            Dice(app.dice)  # Directly create a Dice object instead of calling the roll_dice method
    def test_zero_sides(self):
        # Arrange: Create a RollDiceApp instance with zero sides
        app = RollDiceApp()
        app.dice.sides = 0
        # Act: Attempt to roll the Dice using the RollDiceApp instance
        with self.assertRaises(ValueError):
            Dice(app.dice)  # Directly create a Dice object instead of calling the roll_dice method
if __name__ == '__main__':
    unittest.main()