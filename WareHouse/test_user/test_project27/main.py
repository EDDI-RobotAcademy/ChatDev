# python
'''
Main Program Entry Point
This program initializes the GUI calculator.
'''
import tkinter as tk
from calculator_gui import CalculatorGUI
def main():
    gui = CalculatorGUI()
    gui.root.mainloop()
if __name__ == "__main__":
    main()