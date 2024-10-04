# python
'''
The `Dashboard` class handles displaying the last dice roll result in real-time.
'''
import tkinter as tk
class Dashboard:
    def __init__(self, root):
        self.root = root
        self.dashboard_label = tk.Label(root, text="Last Roll: ")
        self.dashboard_label.pack()
    # Update the dashboard label with the latest result
    def update(self, result):
        self.dashboard_label['text'] = f"Last Roll: {result}"