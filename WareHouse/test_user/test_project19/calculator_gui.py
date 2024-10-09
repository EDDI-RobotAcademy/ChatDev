# LANGUAGE: Python
'''
DOCSTRING: Calculator GUI module. Creates the graphical user interface using Tkinter.
'''
import tkinter as tk
from calculator_logic import CalculatorLogic
class CalculatorGUI:
    def __init__(self):
        self.logic = CalculatorLogic()
        self.root = tk.Tk()
        self.entry_label = tk.Label(self.root, text="Number 1:")
        self.entry_label.pack()
        self.number_entry = NumberEntry(self.root)
        self.number_entry.pack()
        self.operator_label = tk.Label(self.root, text="Operator:")
        self.operator_label.pack()
        self.operator_entry = OperatorEntry(self.root)
        self.operator_entry.pack()
        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.pack()
        self.result_text = tk.Text(self.root, height=1, width=20)
        self.result_text.pack()
    def get_input(self):
        num1 = float(self.number_entry.get())
        operator = self.operator_entry.get()
        if operator == "+":
            result = self.logic.add(num1, 10)
        elif operator == "-":
            result = self.logic.subtract(num1, 10)
        elif operator == "*":
            result = self.logic.multiply(num1, 10)
        elif operator == "/":
            try:
                result = self.logic.divide(num1, 10)
            except ValueError as e:
                print(e)
                return
        elif operator == "^":
            result = self.logic.power(num1, 10)
        elif operator == "sqrt":
            result = self.logic.square_root(10)
        elif operator == "%":
            result = self.logic.modulo(num1, 10)
        elif operator == "!":
            try:
                result = self.logic.factorial(int(num1))
            except ValueError as e:
                print(e)
                return
        elif operator == "|x|":
            result = self.logic.absolute_value(num1)
        elif operator == "exp":
            try:
                result = self.logic.exponential(num1, 10)
            except ValueError as e:
                print(e)
                return
        elif operator == "∛":
            try:
                result = self.logic.cube_root(num1)[0]
            except ValueError as e:
                print(e)
                return
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, str(result))
    def run(self):
        button = tk.Button(self.root, text="Calculate", command=self.get_input)
        button.pack()
        self.root.mainloop()
class NumberEntry(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entry = tk.Entry(self)
        self.pack()
        self.entry.pack()
class OperatorEntry(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.option_var = tk.StringVar()
        self.dropdown = tk.OptionMenu(self, self.option_var, "+", "-", "*", "/", "^", "sqrt", "%", "!", "|x|", "exp", "∛")
        self.pack()
        self.dropdown.pack()
root = tk.Tk()
my_gui = CalculatorGUI()
my_gui.run()