# Importing necessary libraries
import random
class Dice:
    """
    Represents a dice with six sides.
    Attributes:
        sides (list): The list of possible outcomes for the dice roll.
    """
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]
    def roll(self):
        """
        Returns a random outcome from the list of possible outcomes.
        Returns:
            int: The result of the dice roll.
        """
        return random.choice(self.sides)