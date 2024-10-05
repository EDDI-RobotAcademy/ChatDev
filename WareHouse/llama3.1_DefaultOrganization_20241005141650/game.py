# game.py
'''
Game logic.
'''
import random
class Game:
    def __init__(self, player_name):
        '''
        Initialize the game.
        Args:
            player_name (str): The player's name.
        '''
        self.player_name = player_name
        self.dice = [Dice() for _ in range(5)]
    def roll_dice(self):
        '''
        Roll the dice.
        '''
        roll_values = [dice.value for dice in self.dice]
        print(f"Roll values: {', '.join(map(str, roll_values))}")
        return sum(roll_values)
class Dice:
    def __init__(self):
        '''
        Initialize a die.
        This is a simple implementation of a die.
        Each time the die is rolled, it generates a random number between 1 and 6.
        '''
        self.value = random.randint(1, 6)