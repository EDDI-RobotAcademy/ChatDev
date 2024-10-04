# main.py
'''The main script to run the application.'''
from .roll_dice_app import RollDiceApp, GUIManager
import tkinter as tk
def main():
    app = RollDiceApp()
    gui = GUIManager()
    result = app.roll_dice()
    print(result)
    root = tk.Tk()
    gui = GUIManager(root)
    root.mainloop()
if __name__ == '__main__':
    main()