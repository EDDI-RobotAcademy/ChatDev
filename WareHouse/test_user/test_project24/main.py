# LANGUAGE: Python
'''
GUI class: uses tkinter for graphical user interface (optional)
'''
import tkinter as tk
from calculator import Calculator  # Corrected Import Statement
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.calculator = Calculator()
    def display(self):
        # Create input fields and buttons
        num1_label = tk.Label(self.root, text="Number 1:")
        num1_entry = tk.Entry(self.root)
        num2_label = tk.Label(self.root, text="Number 2:")
        num2_entry = tk.Entry(self.root)
        add_button = tk.Button(self.root, text="Add", command=lambda: self.calculate(self.calculator.add))
        subtract_button = tk.Button(self.root, text="Subtract", command=lambda: self.calculate(self.calculator.subtract))
        multiply_button = tk.Button(self.root, text="Multiply", command=lambda: self.calculate(self.calculator.multiply))
        divide_button = tk.Button(self.root, text="Divide", command=lambda: self.calculate(self.calculator.divide))
    def calculate(self, operation):
        try:
            result = operation(int(num1_entry.get()), int(num2_entry.get()))
            result_label = tk.Label(self.root, text=f"Result: {result}")
            result_label.place(in_=self.root, x=250, y=200)
        except ValueError as e:
            error_label = tk.Label(self.root, text="Error: Please enter valid numbers")
            error_label.place(in_=self.root, x=100, y=300)
    def run(self):
        self.display()
        self.root.mainloop()
if __name__ == "__main__":
    gui = GUI()
    gui.run()