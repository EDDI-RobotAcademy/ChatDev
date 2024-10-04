# roll_service.py
'''The RollService class generates a random number between 1 and 6, simulating the effect of rolling a die.'''
import random
class RollService:
    def __init__(self):
        pass
    def roll(self):
        # Generate a random result
        return random.randint(1, 6)
    def get_average_result(self):
        # Get multiple results and calculate the average
        results = [random.randint(1, 6) for _ in range(10)]
        return sum(results) / len(results)