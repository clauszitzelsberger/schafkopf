# -*- coding: utf-8 -*-

from game import Game

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
        
    def set_game(self, player_id, game):
        assert type(player_id)==int, 'player_id argument must be int type'
        assert type(game)==list and len(game)==2 and type(game[0])==type(game[1])==str, \
            'game argument must be a list of two strings'
        self.game_player_id = player_id
        self.game = Game(game[0], game[1])
        