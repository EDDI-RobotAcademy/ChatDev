# unittest
import unittest
from gui_controller import GUIController
class TestGUIController(unittest.TestCase):
    def setUp(self):
        self.controller = GUIController()
    def test_draw_gui(self):
        screen = pygame.display.set_mode((800, 600))
        try:
            self.controller.drawGUI(screen)
        except Exception as e:
            self.assertEqual(str(e), "Error drawing GUI")
    def test_handle_events(self):
        event = pygame.event.Event(pygame.QUIT)
        self.controller.handle_events(event)
class TestGUIControllerExceptions(unittest.TestCase):
    def test_unexpected_event(self):
        controller = GUIController()
        try:
            controller.handle_events(pygame.event.Event("InvalidEvent"))
        except Exception as e:
            self.assertEqual(str(e), "Unexpected event occurred")