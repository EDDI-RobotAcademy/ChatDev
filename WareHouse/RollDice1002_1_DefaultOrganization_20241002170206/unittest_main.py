import unittest
from game_repository import GameRepository
from game import Game
from player import Player
class TestBettingLogic(unittest.TestCase):
    def test_place_bet(self):
        game = Game(GameRepository())
        player1 = Player("John Doe", 100.0)
        player2 = Player("Jane Smith", 50.0)
        game.repository.add_player(player1)
        game.repository.add_player(player2)
        new_balance1, _ = game.place_bet(player1, 10, BetAmount.WIN), game.place_bet(player2, 15, BetAmount.LOSS)
        self.assertEqual(new_balance1['balance'], 90.0)
        self.assertEqual(new_balance2['balance'], 35.0)
    def test_update_bet_invalid(self):
        with self.assertRaises(ValueError):
            Game(GameRepository()).place_bet(Player("Invalid", 100), 10, 'Invalid')
if __name__ == '__main__':
    unittest.main()