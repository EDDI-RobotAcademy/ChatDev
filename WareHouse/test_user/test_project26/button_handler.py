# python
'''
Button Click Event Handling
'''
class ButtonHandler:
    @staticmethod
    def button_click(value, input_field, output_field):  # Add parameters for the input field and output field
        '''
        Perform an action when a button is clicked.
        Args:
            value (str): The value of the button clicked.
            input_field: The current input field.
            output_field: The current output field.
        '''
        calculator = Calculator()
        current_expression = input_field.get()  # Get the current expression from the input field
        if current_expression:  # Check if there's an existing expression
            current_expression += " " + value  # Append the button value to the existing expression
        else:
            current_expression = value  # If no existing expression, set it to the button value
        input_field.delete(0, tk.END)  # Clear the input field
        input_field.insert(tk.END, current_expression)  # Insert the new expression into the input field
        result = calculator.calculate(current_expression)
        if result is not None:
            output_field.config(text=str(result))