# python
'''
Main application file.
'''
from repository import RollDiceRepository
from services import DiceRollService
def main():
    repository = RollDiceRepository()
    service = DiceRollService(repository)
    roll = service.roll_dice()
    print(f"Rolled: {roll}")
if __name__ == "__main__":
    main()