# main.py (Python)
'''
Main entry point of the Roll Dice App.
'''
from tkinter import Tk
from roll_dice_app import RollDiceApp
def main():
    # Create a Tkinter window
    root = Tk()
    # Create an instance of RollDiceApp
    app = RollDiceApp(root)
    # Run the application
    app.run()
    # Start the Tkinter event loop
    root.mainloop()
if __name__ == "__main__":
    main()