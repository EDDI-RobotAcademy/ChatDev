# statistics_calculator.py (Python)
'''
Represents a Statistics Calculator instance.
'''
from roll import Roll
class StatisticsCalculator:
    def calculate(self, rolls):
        total = 0
        for roll in rolls:
            total += roll.result
        return f"Total: {total}"