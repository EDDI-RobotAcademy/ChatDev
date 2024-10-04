'''
Game Repository
================
A repository for managing game-related data.
'''
import threading
from typing import List
class GameRepository:
    def __init__(self):
        self.players: List[Player] = []
        self.bet_types = {
            'WIN': 'Bet amount wins',
            'LOSS': 'Player loses',
            'PUSH': 'Result is a push'
        }
        self.lock = threading.Lock()
    def add_player(self, player: Player):
        with self.lock:
            self.players.append(player)
    def get_current_player_index(self) -> int:
        return 0
    def update_bet(self, player: Player, amount: float, bet_type: str):
        with self.lock:
            try:
                new_balance = player.bet(amount, bet_type)
                # Ensure the lock is released even if an error occurs
                try:
                    return new_balance
                finally:
                    # Remove the player from the list after updating
                    self.players.remove(player)
            except ValueError as e:
                print(f"Error: {e}")
                raise