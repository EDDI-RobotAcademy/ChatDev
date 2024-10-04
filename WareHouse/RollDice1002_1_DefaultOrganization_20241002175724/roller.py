"""
Manages a collection of Dice instances.
This module implements a simple class for managing multiple dice rolls. It includes methods for rolling all dice and resetting their values.
"""
class Roller:
    def __init__(self):
        """
        Initializes a new instance of the Roller class.
        This method sets up an empty dictionary to store multiple Dice instances, allowing for rolling multiple dice.
        """
        self.dice = {}
    def roll(self):
        """
        Rolls all specified dice and returns their results.
        This method retrieves a list of dice from the `dice` dictionary, rolls each one using its own instance of the Dice class,
        and returns the results as a single list.
        Returns:
            list: A list of results for each rolled die.
        """
        # Retrieve the list of dice to roll
        num_dice = len(self.dice)
        # Roll all specified dice
        results = []
        for i, (die_id, die) in enumerate(self.dice.items()):
            result = die.roll()
            results.append(f"Die {i+1}: {result}")
        return results
    def reset(self):
        """
        Resets the rolled values for each die.
        This method iterates over the `dice` dictionary and calls its `reset()` method to clear the rolled value for each instance.
        """
        self.dice = {}