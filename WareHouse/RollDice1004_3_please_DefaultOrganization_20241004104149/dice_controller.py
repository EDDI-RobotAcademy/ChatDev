# -*- coding: utf-8 -*-
'''Dice controller class'''
class DiceController:
    def roll_dice(self):
        '''Simulate a six-sided die'''
        import random
        return random.randint(1, 6)  