# python
'''
Application Service for Roll Dice App
'''
from .RollDiceDomain import SixSidedDie, RollDiceDomain
class RollDiceService:
    def __init__(self):
        self.domain = RollDiceDomain(SixSidedDie())
    def roll_dice(self):
        return self.domain.roll_dice()