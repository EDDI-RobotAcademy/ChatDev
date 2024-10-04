# utils.py
'''
Utility Functions (No Changes Required)
'''
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw  # Corrected Import Statement
def generate_dice_image(result):
    # Simulate generating an image for the dice result
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    text = str(result)
    x, y = 10, 55
    w, h = font.getsize(text)
    draw.text((x,y), text, fill=(255, 255, 0))
    return ImageTk.PhotoImage(img)  # Modified to Return PhotoImage