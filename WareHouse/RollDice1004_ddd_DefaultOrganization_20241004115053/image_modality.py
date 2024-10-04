# python
'''
The `ImageModality` class handles visualizing dice roll results as an image.
Contains methods to draw a simple dice image using Tkinter canvas.
'''
import tkinter as tk
class ImageModality:
    def __init__(self, root):
        self.root = root
        self.image_label = tk.Label(root)
        self.image_label.pack()
    # Draw a simple dice image based on the result
    def draw_dice(self, result):
        canvas = tk.Canvas(self.image_label, width=100, height=100)
        canvas.pack()
        # Simple dice face drawing (just a placeholder for now)
        canvas.create_rectangle(10, 10, 20, 20)  # Center point of the dice