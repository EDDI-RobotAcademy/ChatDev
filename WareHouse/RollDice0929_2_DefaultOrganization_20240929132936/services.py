# python
'''
Service for rolling dice and saving results.
'''
from repository import RollDiceRepository
class DiceRollService:
    def __init__(self, repository):
        self.repository = repository
        self.domain = None  # Removed the incorrect import of domain.py
    def roll_dice(self):
        '''
        Roll the dice and save the result to the repository.
        Returns:
            int: The generated roll value.
        '''
        try:
            if not self.domain:  # Initialize the domain attribute only once
                # TODO: Add a factory method or dependency injection for creating the domain object
                pass
            roll = self.domain.roll_dice()
            self.repository.save_roll(roll)
            return roll
        except Exception as e:
            print(f"Error rolling dice: {e}")