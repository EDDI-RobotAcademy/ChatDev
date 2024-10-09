# main.py
'''Simple Calculator App Entry Point'''
from gui import GUI
from button_handler import ButtonHandler
def main():
    # Initialize GUI and calculator state
    gui = GUI()
    calculator = Calculator()
    # Start the GUI event loop
    def calculate_expression():
        nonlocal self  # Add this line to access the 'self' variable from the outer scope
        current_expression = self.input_field.get()  
        if current_expression:  
            try:
                result = eval(current_expression) 
                print(result)
            except Exception as e:
                print(f"Error: {str(e)}")