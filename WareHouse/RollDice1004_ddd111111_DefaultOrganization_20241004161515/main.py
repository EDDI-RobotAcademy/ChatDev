# main.py
# LANGUAGE: Python
'''
Main entry point of the application.
DOCSTRING:
This script initializes the roll dice app, setting up the domain model,
application layer services, and infrastructure layer.
'''
import tkinter as tk; import ttk from tkinter import ttk
from roll_dice_app.gui_handler import GUIHandler
from roll_dice_app.roll_service import RollService
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Roll Dice App")
        # Initialize GUI handler
        self.gui_handler = GUIHandler(self.root)
        # Create main application window
        self.main_window = ttk.Frame(self.root)
        self.main_window.pack(fill="both", expand=True)
    def run(self):
        self.roll_service = RollService()
        self.dashboard_service = DashboardService(self.roll_service)
        self.gui_handler.update_gui(self.dashboard_service.update_dashboard())
        self.root.mainloop()
if __name__ == "__main__":
    app = MainApp()
    app.run()