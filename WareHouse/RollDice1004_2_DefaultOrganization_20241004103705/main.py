# python
'''
Main Entry Point for Roll Dice App
'''
from .roll_dice_gui import RollDiceGUI
def main():
    gui = RollDiceGUI()
    gui.run()
if __name__ == "__main__":
    main()