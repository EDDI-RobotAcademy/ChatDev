# python
'''
Calculator GUI Class
This class creates the graphical user interface components.
'''
import tkinter as tk
from calculator_logic import CalculatorLogic
class CalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.entry_field = tk.Entry(self.root, width=35)
        self.entry_field.grid(row=0, column=0, columnspan=4)
        self.create_buttons()
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row_val, col_val = 1, 0
        for button in buttons:
            tk.Button(self.root, text=button, width=10, command=lambda b=button: self.on_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1
        # Add clear button
        tk.Button(self.root, text="Clear", width=22, command=self.clear_input).grid(row=row_val, column=0, columnspan=4)
    def on_click(self, value):
        if value == '=':
            try:
                result = CalculatorLogic().calculate(self.entry_field.get(), '+', '')
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, str(result))
            except ValueError as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        else:
            self.entry_field.insert(tk.END, value)
    def clear_input(self):
        self.entry_field.delete(0, tk.END)