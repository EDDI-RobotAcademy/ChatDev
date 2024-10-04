# Service classes for business logic.
from models import Dice
class RollService:
    @staticmethod
    def roll_dice(dice):
        """Rolls the dice and returns a dictionary with result details."""
        result = dice.roll()
        return {"result": f"Dice rolled: {result}", "value": result}