# python
'''
Domain logic for the Roll Dice App.
'''
import random
class RollDiceDomain:
    def roll_dice(self):
        '''
        Generate a random roll value between 1 and 6.
        Returns:
            int: The generated roll value.
        '''
        return random.randint(1, 6)