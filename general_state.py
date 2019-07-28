# -*- coding: utf-8 -*-

import game
NoneType = type(None)
max_score = 120

class State():
    """
    Stores every information of the game which is
    available for every player:
        - dealer
        - which game is played
        - scores
        - etc.
    """
    def __init__(self, dealer_id):
        self.dealer_id = dealer_id
        self.first_player = (dealer_id + 1) % 4
        self.game = None
        self.game_player_id = None
        self.played_cards = None
        self.scores = [0, 0, 0, 0]
        self.trick = 0
        
    def set_game(self, player_id, selected_game=[None, None]):
        """Sets game and respective player id"""
        
        if selected_game!=[None, None]:
            assert isinstance(player_id, int), 'player_id argument must be int type'
            assert isinstance(selected_game, list)
            assert len(selected_game)==2
            self.game_player_id = player_id
            self.game = game.initialize(selected_game[0], selected_game[1])
            
    def play_card(self, player_id, card):
        """Puts card into played_cards"""
        pass
            
    def update_scores(self, additional_scores=[0, 0, 0, 0]):
        """Update scores of each player"""
        
        assert isinstance(additional_scores, list)
        self.scores += additional_scores
        assert sum(self.scores)<=max_score
        
    