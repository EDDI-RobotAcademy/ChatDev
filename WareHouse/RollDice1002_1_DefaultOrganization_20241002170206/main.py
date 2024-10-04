'''
Main Application
==============
The main application for testing the game engine.
'''
from game_repository import GameRepository
from game import Game
from player import Player
def main():
    # Initialize the game repository and players
    repository = GameRepository()
    player1 = Player('Player 1', 100)
    player2 = Player('Player 2', 50)
    # Add players to the repository
    repository.add_player(player1)
    repository.add_player(player2)
    # Create a new game instance
    game = Game(repository)
    # Place bets on both players
    bet_amount = 20
    bet_type = 'WIN'
    new_balance = game.place_bet(player1, bet_amount, bet_type)
    print(f"Player 1's new balance: {new_balance}")
    new_balance = game.place_bet(player2, bet_amount, bet_type)
    print(f"Player 2's new balance: {new_balance}")
if __name__ == "__main__":
    main()