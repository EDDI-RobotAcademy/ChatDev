# calculator_ui.py
'''
This module contains the GUI-related classes and functions.
'''
import tkinter as tk
from calculator import CalculatorModel, calculate_result
class CalculatorApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.model = CalculatorModel()
        self.create_widgets()
    def create_widgets(self):
        # Create entry fields and buttons for user input
        self.entry_field = tk.Entry(self)
        self.entry_field.pack()
        self.button_frame = tk.Frame(self)
        self.button_frame.pack()
        self.equals_button = tk.Button(self.button_frame, text="=", command=self.calculate_and_display)
        self.equals_button.pack(side=tk.LEFT)
        # Create history display
        self.history_label = tk.Label(self, text="History:")
        self.history_label.pack()
        self.history_text = tk.Text(self, height=5)
        self.history_text.pack()
    def calculate_and_display(self):
        expression = self.entry_field.get()
        result = calculate_result(expression)
        self.model.add_to_history(expression, result)
        self.history_text.delete(1.0, tk.END)
        for expression, result in self.model.get_history():
            self.history_text.insert(tk.END, f"{expression} = {result}\n")