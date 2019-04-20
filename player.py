# -*- coding: utf-8 -*-

from helper import Helper
from game import Game_static

class Player():
    def __init__(self, id, name):
        self.name = name
        self.credit = 0
        self.cards = None
        self.remaining_cards = None
        
    def set_cards(self, cards):
        self.cards = cards
        self.remaining_cards = cards
        
    def get_possible_games(self, state):
        """
        Get all games which a player can play based on his cards and the game 
        which has been already selected by another player and which may be
        overruled"""
        
        sauspiel, wenz, solo = False, False, False
        
        # Evaluate if there is already a potential game player
        # and if he/she can be overruled with a higher-order game
        if state.game is None:
            sauspiel = True
            wenz = True
            solo = True
        elif state.game.kind=='sauspiel':
            wenz = True
            solo = True
        elif state.game.kind=='wenz':
            solo = True
            
        possible_games = []

        if sauspiel:
            for sauspiel in Game_static.sauspiele:
                if len(Helper.get_cards(self.cards, color=[sauspiel[0]], 
                                        trumps=False, state=state))>0:
                    possible_games.append(sauspiel)
        
        if wenz:
            possible_games.append(Game_static.wenz)
        
        if solo:
            possible_games.extend(Game_static.soli)
            
        return possible_games
    
    def get_possible_cards(self, state):
        """
        Get all cards which a player can play based on his remaining cards, the cards
        that have been already played by other players in this trick, and the game
        which is being played"""
                    
    def play_card(self, card):
        pass