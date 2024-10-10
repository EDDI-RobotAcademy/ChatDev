from button_handler import ButtonHandler
def main():
    """
    Start the calculator program.
    Returns:
        None
    """
    # Create a button handler with an empty calculator model
    handler = ButtonHandler()
    # Print welcome message
    print("Welcome to the calculator program!")
    # Run the calculator loop
    while True:
        try:
            # Get user input
            button = input("Enter a button (+, -, *, /, 0-9): ")
            # Handle click on the specified button
            handler.handle_click(button)
        except ZeroDivisionError as e:
            print(str(e))
        # Check if user wants to quit
        if button == 'q':
            break
    # Print goodbye message
    print("Goodbye!")
if __name__ == "__main__":
    main()