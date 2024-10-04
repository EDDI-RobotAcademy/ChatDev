from dice import Dice
class Game:
    def __init__(self):
        # Initialize a new game with two dice
        self.dice = [Dice() for _ in range(2)]
    def start_game(self):
        # Roll both dice and sum up their values
        result = sum(die.roll_dice() for die in self.dice)
        return result
    def stop_game(self):
        # Not implemented yet
        pass  # Stop game is not needed as it's a simple roll-and-sum game