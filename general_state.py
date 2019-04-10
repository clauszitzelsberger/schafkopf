# -*- coding: utf-8 -*-

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
        self.game_player = None
        self.played_cards = None
        
    def set_game(self, player, game):
        self.game_player = player
        self.game = game
        