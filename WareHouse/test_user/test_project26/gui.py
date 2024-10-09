# gui.py
'''
Tkinter GUI Implementation
'''
import tkinter as tk
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Calculator")
        # Create input field and output field with a default font
        self.input_field = tk.Entry(self.root, width=50)
        self.output_field = tk.Label(self.root, text="", justify=tk.LEFT, font=("Arial", 12))  # Set a default font for the GUI elements
        # Pack the input field and output field
        self.input_field.pack()
        self.output_field.pack()