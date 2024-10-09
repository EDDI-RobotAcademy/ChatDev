import tkinter as tk
class CalcButton(tk.Button):
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.master = master
class CalculatorFrame(tk.Frame):
    def __init__(self, master):  # Constructor for the CalculatorFrame class
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.aseval = literal_eval  # Use safer evaluation library
    def create_widgets(self):
        """
        Creates display labels and buttons.
        """
        # Create display label
        self.display_label = tk.Label(master=self, text="", justify=tk.LEFT)
        self.display_label.pack()
        # Create number buttons
        for i in range(10):
            button = CalcButton(master=self, text=str(i))
            button.config(command=lambda i=i: self.append_to_display(str(i)))
            button.pack(side=tk.LEFT)
        # Create arithmetic operation buttons
        buttons = [
            tk.Button(master=self, text="+", command=lambda: self.append_to_display("+")),
            tk.Button(master=self, text="-", command=lambda: self.append_to_display("-")),
            tk.Button(master=self, text="*", command=lambda: self.append_to_display("*")),
            tk.Button(master=self, text="/", command=lambda: self.append_to_display("/"))
        ]
        for button in buttons:
            button.pack(side=tk.LEFT)
        # Create equals and clear buttons
        buttons = [
            tk.Button(master=self, text="=", command=self.calculate),
            tk.Button(master=self, text="Clear", command=self.clear)
        ]
        for button in buttons:
            button.pack(side=tk.LEFT)
    def append_to_display(self, value):
        """
        Appends a value to the display label.
        """
        current_value = self.display_label.cget("text")
        if current_value == "":
            self.display_label.config(text=value)
        else:
            self.display_label.config(text=current_value + " " + value)
    def calculate(self):
        """
        Performs calculation and displays result.
        """
        try:
            calculation = self.display_label.cget("text")
            result = self.aseval(calculation)  # Use safer evaluation library
            if calculation.count("/") == 1 and "0" in calculation.split("/")[1]:
                self.display_label.config(text="Error: Division by zero")
            else:
                self.display_label.config(text=str(result))
        except Exception as e:
            self.display_label.config(text="Error: " + str(e))
    def clear(self):
        """
        Clears the display label.
        """
        self.display_label.config(text="")