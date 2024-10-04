from dice import Dice
class Roller:
    def __init__(self, game_service):
        self.game_service = game_service
    def handle_input(self, input_str):
        if input_str == "roll":
            return self.game_service.start_game()
        else:
            raise ValueError("Invalid input")
# Create an instance of StandardGameService
game_service = StandardGameService()
# Create an instance of Roller with the standard game service
roller = Roller(game_service)
# Handle user input (e.g., "roll" to start a new game)
print(roller.handle_input("roll"))