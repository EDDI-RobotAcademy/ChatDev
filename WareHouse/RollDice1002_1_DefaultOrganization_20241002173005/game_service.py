from abc import ABC, abstractmethod
class GameService(ABC):
    @abstractmethod
    def start_game(self):
        pass
    @abstractmethod
    def stop_game(self):
        pass
class StandardGameService(GameService):
    def __init__(self):
        # Initialize a new game service with no game
        self.game = None
    def roll_dice(self, die):
        return die.roll()
    def start_game(self):
        # Initialize a new game and start it rolling
        self.game = Game()
        return self.game.start_game()
    def stop_game(self):
        # Not implemented yet
        pass  # Stop game is not needed as it's a simple roll-and-sum game