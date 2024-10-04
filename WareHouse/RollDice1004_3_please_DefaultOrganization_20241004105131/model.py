# python
'''
Domain Model File (Part of DDD)
'''
class Die:
    '''
    Represents a single six-sided die.
    '''
    def roll(self):
        '''
        Rolls the die and returns a random integer between 1 and 6.
        :return: A random integer
        '''
        import random
        return random.randint(1, 6)