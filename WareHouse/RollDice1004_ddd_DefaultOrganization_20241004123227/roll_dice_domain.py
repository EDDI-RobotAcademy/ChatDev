# FILENAME: roll_dice_domain.py
# LANGUAGE: Python
'''
Domain class for rolling dice
The RollDiceDomain class encapsulates the logic for simulating two virtual dice rolls.
It ensures that each die is rolled independently and returns a string representation of the result.
Note:
    * The __init__ method initializes self.dice1 and self.dice2 to None, indicating no previous roll has occurred.
    * The roll_dice method uses random.randint to simulate rolling two virtual dice (1-6). It then stores the results in self.dice1 and self.dice2. Finally, it returns a string representation of the rolled dice result.
References:
    * random.randint documentation: https://docs.python.org/3/library/random.html#random.randint
'''
import random
class RollDiceDomain:
    def __init__(self):
        '''
        Initialize the domain class with no previous roll.
        Attributes:
            self.dice1 (int): The value of Die 1.
            self.dice2 (int): The value of Die 2.
        '''
        self.dice1 = None
        self.dice2 = None
    def roll_dice(self):
        '''
        Roll the dice and return a string representation of the results.
        Returns:
            str: A string representation of the rolled dice result (e.g., "Die 1: 3, Die 2: 5").
        '''
        # Ensure that self.dice1 and self.dice2 are not None
        if self.dice1 is not None or self.dice2 is not None:
            raise ValueError("Cannot roll dice with previous results.")
        try:
            # Simulate rolling two virtual dice (1-6) using random.randint
            self.dice1 = random.randint(1, 6)
            self.dice2 = random.randint(1, 6)
            # Return a string representation of the rolled dice result
            return f"Die 1: {self.dice1}, Die 2: {self.dice2}"
        except Exception as e:
            # Catch and handle any exceptions that might occur during simulation
            print(f"Error rolling dice: {e}")
            return None
# Example usage:
domain = RollDiceDomain()
print(domain.roll_dice())