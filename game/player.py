from game.resources import *


class Player(ResourceConsumer):
    def __init__(self, id):
        super().__init__(player=True)
        self.player_id = id

    @staticmethod
    def players(num_players):
        players = [Player(i) for i in range(num_players)]
        return players

