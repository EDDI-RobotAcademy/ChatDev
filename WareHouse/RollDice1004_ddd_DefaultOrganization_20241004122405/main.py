# main.py
'''
Roll Dice App Main Application (Updated Code)
'''
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw  # Corrected Import Statement
from dice import Die
class DiceRollAppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.die = Die()
    def run(self):
        gui = DiceGUI(self)
        gui.run()
        main_loop = self.root.mainloop()
# Rest of your code...