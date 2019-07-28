# -*- coding: utf-8 -*-

from game import Game
NoneType = type(None)

class State():
    """
    Class which stores every information of the game which is
    available for every player:
        - dealer
        - which game is played
        - scores
        - etc.
    """
    def __init__(self, dealer_id):
        self.dealer_id = dealer_id
        self.game = None
        self.game_player_id = None
        self.played_cards = None
        
    def set_game(self, player_id, game=[None, None]):
        
        if game!=[None, None]:
            assert isinstance(player_id, int), 'player_id argument must be int type'
            assert isinstance(game, list)
            assert len(game)==2
            assert isinstance(game[0], (str, NoneType))
            assert isinstance(game[1], str)
            self.game_player_id = player_id
            self.game = Game(game[0], game[1])
    