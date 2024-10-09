# LANGUAGE: Python
'''
DOCSTRING: Entry point for the calculator app.
'''
from calculator_gui import CalculatorGUI
def main():
    gui = CalculatorGUI()
    gui.run()
if __name__ == "__main__":
    main()