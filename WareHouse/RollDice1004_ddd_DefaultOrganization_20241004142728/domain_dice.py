# python
"""
Module containing the Dice entity and its related logic.
"""
import random
class Dice:
    def __init__(self, sides=6):
        """
        Initializes a new instance of the Dice class.
        Args:
            sides (int): The number of sides on the dice. Defaults to 6.
        """
        self.sides = sides
    def roll(self):
        """
        Simulates rolling the dice and returns the result.
        Returns:
            int: A random integer between 1 and the number of sides.
        """
        return random.randint(1, self.sides)