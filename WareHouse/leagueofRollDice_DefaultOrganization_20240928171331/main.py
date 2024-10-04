# Importing necessary libraries
from application import *

class RollResult:
    def __init__(self):
        """
        Initializes the RollResult object with an empty list to store roll results.
        Attributes:
            results (list): The list of roll results.
        """
        self.results = []
    def add_result(self, result):
        if not isinstance(result, int) or not 1 <= result <= 6:
            raise ValueError("Invalid dice roll result")
        self.results.append(result)
    def get_results(self):
        return ', '.join(str(r) for r in sorted(set(self.results)))
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.dice_count = 0
        self.roll_result = RollResult()
        self.input_entry = None
        self.create_widgets()
        self.set_up_input_box()
    def create_widgets(self):
        input_label = Label(self, text="Enter the number of dice to roll:")
        input_label.pack()
        self.input_entry = Entry(self)
        self.input_entry.pack()
        roll_button = Button(self, text="Roll Dice", command=self.roll_dice)
        roll_button.pack()
        reset_button = Button(self, text="Reset Roll Count", command=self.reset_roll_count)
        reset_button.pack()
    def set_up_input_box(self):
        pass
    def roll_dice(self):
        max_attempts = 3  
        attempts = 0
        while True:
            try:
                self.dice_count = int(self.input_entry.get())
                if self.dice_count <= 0:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
                attempts += 1
                if attempts >= max_attempts:
                    raise Exception("Maximum attempts exceeded.")
        dice_roll = Dice()
        for _ in range(self.dice_count):
            self.roll_result.add_result(dice_roll.roll())
        result_label = Label(self, text=self.roll_result.get_results())
        result_label.pack()
        success_message = Label(self, text="Dice rolled successfully!", fg="green")
        success_message.pack()
    def reset_roll_count(self):
        self.dice_count = 0
        self.roll_result = RollResult()
        input_label = Label(self, text="Enter the number of dice to roll:")
        input_label.pack()
    def run_app(self):
        app.mainloop()
class Dice:
    def roll(self):
        return random.randint(1, 6)
if __name__ == "__main__":
    gui = GUI()
    gui.run_app()