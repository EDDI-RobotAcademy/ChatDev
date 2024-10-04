# python
'''
GUI Presentation File (Part of DDD)
'''
import tkinter as tk
class GUI:
    '''
    Represents the graphical user interface of the Roll Dice App.
    '''
    def __init__(self):
        '''
        Initializes a new instance of the GUI class.
        :return: None
        '''
        self.root = None
    def create_window(self):
        '''
        Creates a new window with a title 'Roll Dice' for the application.
        :return: None
        '''
        self.root = tk.Tk()
        self.root.title("Roll Dice")
    def add_button(self, text, command):
        '''
        Adds a new button to the window.
        :param text: The text to display on the button
        :param command: The function to call when the button is clicked
        :return: None
        '''
        self.button = tk.Button(self.root, text=text, command=command)
        self.button.pack()
    def update_label(self, result):
        '''
        Updates the label with the result.
        :param result: The result to display on the label
        :return: None
        '''
        self.label = tk.Label(self.root, text=f"Result: {result}")
        self.label.pack()