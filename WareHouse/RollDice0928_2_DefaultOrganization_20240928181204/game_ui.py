from tkinter import Tk, Label
class GameUI:
    def __init__(self, master=None):
        # Create a new Tkinter window
        self.root = Tk()
        self.label = Label(self.root)
        self.create_window()
    def create_window(self):
        # Create a label with current score
        self.label.pack()