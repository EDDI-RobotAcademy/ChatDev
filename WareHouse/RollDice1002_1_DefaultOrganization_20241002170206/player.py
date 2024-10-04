'''
Player Model
==========
A model representing a game player.
'''
class Player:
    def __init__(self, username: str, balance: float):
        self.username = username
        self.balance = balance
        self.token = None
    def set_token(self, token: str):
        self.token = token
    def bet(self, amount: float, bet_type: str) -> dict:
        if (amount > 0 and amount <= self.balance) or (amount == 0):
            new_balance = self.balance - amount
            return {'balance': new_balance, 'bet_type': bet_type}
        else:
            raise ValueError("Invalid bet amount")