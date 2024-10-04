#!/usr/bin/env python3
'''
DOCSTRING: Main file: Initializes the game controller and starts the GUI event loop.
'''
import tkinter as tk
from gui import GUI
from game_controller import GameController
from dice_roller import DiceRoller  # <--- Added this line to fix the import issue
def main():
    # Create a new Tk instance (the root window)
    root = tk.Tk()
    # Initialize the game controller
    game_controller = GameController(root)
    # Create and start the GUI event loop
    gui = GUI(root, game_controller)
    root.mainloop()
if __name__ == "__main__":
    main()