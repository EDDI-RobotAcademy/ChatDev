import random
class Dice:
    """Represents a single six-sided die."""
    def __init__(self, sides=6):
        """
        Initializes a new Dice instance.
        """
        self.sides = sides
    # Roll the dice
    def roll(self):
        return random.randint(1, self.sides)