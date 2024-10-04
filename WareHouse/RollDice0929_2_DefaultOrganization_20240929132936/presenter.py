# python
'''
Presenter for the Roll Dice App.
'''
from tkinter import Label
class RollDicePresenter:
    def __init__(self, root):
        self.root = root
        self.label = Label(self.root, text="")
        self.label.pack()
    def update_label(self, roll):
        '''
        Update the label with a new roll value.
        Args:
            roll (int): The new roll value.
        Returns:
            None
        '''
        self.label['text'] = f"You rolled: {roll}"