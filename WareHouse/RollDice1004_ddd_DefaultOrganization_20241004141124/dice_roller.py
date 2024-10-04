#!/usr/bin/env python3
'''
DOCSTRING: File: Dice roller implementation.
'''
import random  # <--- Added this line to fix the import issue
class DiceRoller:
    def roll_dice(self):
        '''
        DOCSTRING: Simulates a dice roll and returns a random number between 1 and 6.
        '''
        return random.randint(1, 6)