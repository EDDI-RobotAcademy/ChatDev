# LANGUAGE: Python
# DOCSTRING: Main application class
'''
app.py
Main application class.
'''
from game_logic import GameLogic
from gui import GUI
class App:
    def __init__(self):
        self.game_logic = GameLogic()
        self.gui = GUI()
    def run(self):
        self.gui.run()