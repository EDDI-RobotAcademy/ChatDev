# main.py
'''
Main entry point of the application.
'''
import tkinter as tk
from game import Game
from player import Player
from utils import validate_player_name, is_positive_integer
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.player = None
        self.game = None
        self.initUI()
    def initUI(self):
        self.master.title('Dice Game')
        self.pack(fill='both', expand=True)
        self.nameLabel = tk.Label(self, text='Enter your name:')
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack()
        self.rollButton = tk.Button(self, text="Roll", command=self.on_roll_button_click)
        self.rollButton.pack()
    def on_roll_button_click(self):
        if not self.player:
            self.create_player()
        if self.game:
            self.remove_game()
        self.create_game()
        roll_value = self.game.roll_dice()
        print(f"Roll value: {roll_value}")
        self.update_score(roll_value)
    def create_player(self):
        name = self.nameEntry.get()
        if validate_player_name(name):
            self.player = Player(name)
        else:
            print("Invalid player name.")
    def remove_game(self):
        for widget in self.winfo_children():
            widget.destroy()
    def update_score(self, roll_value):
        self.player.score += roll_value
        self.scoreLabel = tk.Label(self, text=f"Score: {self.player.score}")
        self.scoreLabel.pack()