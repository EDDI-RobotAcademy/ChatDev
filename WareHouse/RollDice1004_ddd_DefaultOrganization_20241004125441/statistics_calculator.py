# statistics_calculator.py
'''
Statistics Calculator Class - Calculates and updates statistics.
'''
class StatisticsCalculator:
    def __init__(self):
        '''
        Initializes a new instance of the StatisticsCalculator class.
        Attributes:
            rolls (int): The number of rolls made.
            total (int): The sum of all rolled values.
        '''
        self.rolls = 0
        self.total = 0
    def update_statistics(self, rolled_dice_value):
        '''
        Updates the statistics with a new roll value.
        Args:
            rolled_dice_value (int): The newly rolled value.
        '''
        self.rolls += 1
        self.total += rolled_dice_value
    def get_averages(self):
        '''
        Gets the average of all rolls made so far.
        Returns:
            str: A message indicating that no rolls have been made yet, or the calculated average if there are any rolls.
        '''
        if self.rolls == 0:
            return "No rolls made yet."
        else:
            return f"Average roll value: {self.total / self.rolls}"