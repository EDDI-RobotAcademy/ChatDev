import threading
class GameRepository:
    def __init__(self):
        self.players = []
        self.bet_types = {}
        self.lock = threading.Lock()
    def add_player(self, player):
        with self.lock:
            self.players.append(player)
    def get_current_player_index(self):
        return 0
    def update_bet(self, player, amount, bet_type):
        with self.lock:
            new_balance = player.bet(amount, bet_type)
            # Implement synchronization mechanism here
            return new_balance