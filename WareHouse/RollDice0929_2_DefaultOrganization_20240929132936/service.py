# python
'''
Service for rolling dice and saving results.
'''
from services import DiceRollService
class DiceRollService:
    def __init__(self, repository):
        self.repository = repository
        self.domain = RollDiceDomain()
    def roll_dice(self):
        '''
        Roll the dice and save the result to the repository.
        Returns:
            int: The generated roll value.
        '''
        try:
            roll = self.domain.roll_dice()
            self.repository.save_roll(roll)
            return roll
        except Exception as e:
            print(f"Error rolling dice: {e}")