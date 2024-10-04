# gui.py
'''
Graphical User Interface (Updated Code)
'''
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw  # Corrected Import Statement
class DiceGUI:
    def __init__(self, app):
        self.app = app
        self.root = self.app.root
        self.label = None
        self.result_image = None
    def run(self):
        label = tk.Label(self.root, text="Rolling...")
        label.pack()
        result = self.app.die.get_result()
        image = generate_dice_image(result)
        label = tk.Label(self.root, image=image)
        label.image = image  # Keep a reference!
        label.pack()