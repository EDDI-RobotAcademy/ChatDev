# LANGUAGE: Python
# DOCSTRING: Main application class
"""
Main application class that encapsulates the entire Roll Dice App.
"""
import pygame
from dice_roller import DiceRoller  # Importing DiceRoller from the new implementation of the dice_roller file
class RollDiceApp:
    def __init__(self):
        self.dice_roller = DiceRoller()
        self.gui_controller = GUIController()
    def run(self):
        pygame.init()
        window_size = (800, 600)
        screen = pygame.display.set_mode(window_size)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.gui_controller.handle_events(screen)
            # Update game state
            outcome = self.dice_roller.get_dice_outcome()
            print(outcome)  # Outputting the dice outcome to the console
            self.gui_controller.drawGUI(screen)
            pygame.time.Clock().tick(60)
        pygame.quit()