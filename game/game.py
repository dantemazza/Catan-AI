from game.bank import *
from game.player import *
from game.board import *

class Game:
    def __init__(self, num_players=4, width=5):
         self.players = Player.players(num_players)
         self.bank = Bank()
         self.turn_num = 0
         self.player_turn = 0
         self.board = Board(width=width)

    def get_players(self):
        return self.players

    def get_player(self, player_id):
        return self.get_players()[player_id] 

