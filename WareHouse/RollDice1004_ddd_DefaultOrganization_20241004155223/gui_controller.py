# LANGUAGE: Python
# DOCSTRING: Controller class that handles events and draws the GUI.
"""
Controller class that handles events and draws the GUI.
This class is responsible for handling user input (e.g., mouse clicks, key presses)
and updating the game state accordingly. It also draws the game board and any other graphics.
"""
import pygame
class GUIController:
    def __init__(self, dice_roller):
        self.dice_roller = dice_roller
        self.screen = None
    def handle_events(self, screen):
        # Add event handling code here (e.g., check for mouse clicks, key presses)
        pass
    def drawGUI(self, screen):
        # Draw the game board and any other graphics here
        pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 200))  # Draw a red rectangle
    def draw_dice_result(self, screen, outcome):
        # Draw the dice outcome on the screen
        font = pygame.font.SysFont("Arial", 24)
        text = font.render(str(outcome), True, (0, 0, 255))
        screen.blit(text, (300, 300))
    def get_outcome(self):
        return self.dice_roller.get_outcome()