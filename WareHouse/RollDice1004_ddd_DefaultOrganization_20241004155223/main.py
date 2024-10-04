# LANGUAGE: Python
# DOCSTRING: Main application class that encapsulates the entire Roll Dice App.
"""
Main application class that encapsulates the entire Roll Dice App.
"""
import pygame
from dice_roller import DiceRoller  # Importing DiceRoller from the new implementation of the dice_roller file
from gui_controller import GUIController
class RollDiceApp:
    def __init__(self):
        self.dice_roller = DiceRoller()
        self.gui_controller = GUIController(self.dice_roller)
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.gui_controller.handle_events(screen)
            self.gui_controller.drawGUI(screen)
            # Add the dice outcome to the GUI
            self.gui_controller.draw_dice_result(screen, self.dice_roller.get_outcome())
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
if __name__ == "__main__":
    app = RollDiceApp()
    app.run()