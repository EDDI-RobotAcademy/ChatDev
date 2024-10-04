import random
class Dice:
    def __init__(self):
        # Initialize a new die with a random value between 1 and 6
        self.value = random.randint(1, 6)
    @abstractmethod
    def roll_dice(self):
        pass
    def roll(self):
        # Simulate rolling the die by generating a new random value
        self.value = random.randint(1, 6)
        return self.value