# python
"""
Module containing the business logic for rolling a dice.
"""
from domain_dice import Dice
class RollDiceApp:
    def __init__(self):
        """
        Initializes a new instance of the RollDiceApp class.
        Attributes:
            dice (Dice): The underlying dice entity.
        """
        self.dice = Dice()
    def roll_dice(self):
        """
        Simulates rolling the dice and returns the result.
        Returns:
            str: A human-readable string representing the rolled value.
        """
        try:
            result = self.dice.roll()
            return f"You rolled a {result}"
        except Exception as e:
            # Handle exceptions here, e.g., display an error message to the user
            print(f"Error occurred: {e}")
            return "An unexpected error occurred."