"""
GUI for the calculator application.
Provides a simple text-based interface to perform basic arithmetic operations.
"""
import tkinter as tk
from utils import add, subtract, multiply, divide
class CalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        # Entry field for user input
        self.entry_field = tk.Entry(self.window)
        self.entry_field.grid(row=0, column=0, columnspan=4)
        # Display field to show the result
        self.result_field = tk.Label(self.window, text="", fg="black", bg="white")
        self.result_field.grid(row=1, column=0, columnspan=4)
        # Buttons for arithmetic operations
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]
        self.create_buttons(buttons)
        # Create equals and clear buttons
        tk.Button(self.window, text="=", command=self.calculate).grid(row=4, column=0)
        tk.Button(self.window, text="C", command=self.clear).grid(row=4, column=1)
    def create_buttons(self, buttons):
        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                tk.Button(self.window, text=button, command=lambda value=button: self.append_to_entry(value)).grid(row=i+1, column=j)
    def append_to_entry(self, value):
        self.entry_field.insert(tk.END, value)
    def calculate(self):
        try:
            result = eval(self.entry_field.get())
            self.result_field.config(text=str(result))
        except Exception as e:
            self.result_field.config(text="Error")
    def clear(self):
        self.entry_field.delete(0, tk.END)
        self.result_field.config(text="")
    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    gui = CalculatorGUI()
    gui.run()