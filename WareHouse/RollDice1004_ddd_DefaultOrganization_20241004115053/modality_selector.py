# python
'''
A simple modality selector class that allows switching between different modes.
Currently supports application, dashboard, and image modality modes.
'''
import tkinter as tk
class ModalitySelector:
    def __init__(self):
        self.modality_modes = ["application", "dashboard", "image"]
    # Get the current modality mode
    def get_modality(self):
        return tk.StringVar().get()
    # Set a new modality mode based on user input
    def set_modality(self, mode):
        if mode in self.modality_modes:
            tk.StringVar().set(mode)