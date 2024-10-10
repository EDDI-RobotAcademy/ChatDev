# main.py
'''
This is the entry point of our calculator app.
'''
import tkinter as tk
from calculator import CalculatorApp
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x200")
        self.calculator = CalculatorApp(self)
if __name__ == "__main__":
    root = Main()
    root.mainloop()