# gui.py
'''
Contains functions for performing graphical user interface calculations.
Ensures robust handling of division by zero and invalid inputs.
'''
import tkinter as tk
class CalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.entry = tk.Entry(self.window)
        self.button = tk.Button(self.window, text="=", command=self.equals_clicked)
    # Update equals_clicked to use evaluate_expression
    def equals_clicked(self):
        expression = str(self.entry.get())
        if not expression or expression == '=':
            return
        result = self.calculation.evaluate_expression(expression)
        if result is None:
            result = "Error"
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, result)
    # Update error_occurred to add visual feedback (e.g., change button color or display alert)
    def error_occurred(self):
        pass
# Run the GUI application
gui = CalculatorGUI()
gui.window.mainloop()