# roll_dice_app.py
'''RollDiceApp is responsible for initializing the application and providing access to its functionality.'''
class RollDiceApp:
    def __init__(self):
        self.roll_service = RollService()
        self.gui_manager = GUIManager()
    def start(self):
        # Initialize the app and display the GUI
        self.gui_manager.display_menu()
    def roll_dice(self):
        # Call the roll service to generate a random result
        result = self.roll_service.roll()
        return result
    def show_results(self):
        # Get multiple results using the RollService class
        results = [self.roll_service.roll() for _ in range(10)]
        # Print each result as well as the average result
        print("Results:")
        for i, result in enumerate(results):
            print(f"Roll {i+1}: {result}")
        print("\nAverage Result:", self.roll_service.get_average_result())