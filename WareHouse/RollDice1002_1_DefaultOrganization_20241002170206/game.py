'''
Game Engine
==========
A game engine for managing bets and players.
'''
import threading
from game_repository import GameRepository
from player import Player
class Game:
    def __init__(self, repository: GameRepository):
        self.repository = repository
        self.current_player_index: int = 0
        self.lock = threading.Lock()
    def authenticate_player(self, username: str, token: str) -> bool:
        with self.lock:
            return any(player.username == username and player.token == token for player in self.repository.players)
    def place_bet(self, player: Player, amount: float, bet_type: str) -> float:
        try:
            new_balance = self.update_bet(player, amount, bet_type)
            return new_balance
        except ValueError as e:
            print(f"Error: {e}")
            raise
    def update_bet(self, player: Player, amount: float, bet_type: str):
        if not self.authenticate_player(player.username, player.token):
            raise ValueError("Invalid player credentials")
        with self.lock:
            try:
                if bet_type in self.repository.bet_types:
                    new_balance = player.bet(amount, bet_type)
                    return new_balance
                else:
                    raise ValueError("Invalid bet type")
            except Exception as e:
                print(f"Error: {e}")
                raise