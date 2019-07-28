# -*- coding: utf-8 -*-

from helper import Helper
import game
import card

class Player():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.credit = 0
        self.cards = None
        self.remaining_cards = None
        self.davonlaufen_possible = False
        self.davonlaufen = False
        
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
            for sauspiel in game.sauspiele:
                if len(Helper.get_cards(self.cards, color=[sauspiel[0]], 
                                        trumps=False, state=state))>0:
                    possible_games.append(sauspiel)
        
        if wenz:
            possible_games.append(game.wenz)
        
        if solo:
            possible_games.extend(game.soli)
            
        return possible_games
    
    def get_possible_cards(self, state):
        """
        Get all cards which a player can play based on his remaining cards, the cards
        that have been already played by other players in this trick, and the game
        which is being played"""
        
        lead_card = state.played_cards[state.trick][state.first_player]
        
        if state.game.kind == 'sauspiel':
            
            rufsau = {'color': state.game.color,
                      'number': 'sau'}
        
            # Player is first one to play a card in this trick
            if state.first_player == self.id:
                
                assert lead_card==[None, None]
                
                # Check if player has rufsau
                ids_list = Helper.get_cards(self.remaining_cards, 
                                               color=[rufsau['color']], 
                                               number=[rufsau['number']])
                if len(ids_list)==0:
                    return self.remaining_card
                
                # Player has rufsau
                else:
                    rufsau = self.remaining_cards[ids_list[0]]
                    # Player has more than 3 cards with rufsau's color
                    # davonlaufen is possible
                    if len(Helper.get_cards(self.remaining_cards,
                                            color=[rufsau[0]],
                                            trumps=False))>=4:
                        self.davonlaufen_possible = True
                        return self.remaining_cards
                    # Player has less then 4 cards with rufsau's color
                    # Can play either rufsau or any other card with a color unlike rufsau
                    else:
                        colors_unlike_rufsau = [c for c in self.remaining_cards.colors if c!=rufsau['color'] ]
                        possible_cards = Helper.get_cards(self.remaining_cards,
                                                          color=colors_unlike_rufsau)
                        possible_cards.appen(rufsau)
                        return possible_cards
             
            # Player is not the first one in this trick
            else:
                
                # Lead card is a trump
                if len(Helper.get_trumps([lead_card], state))>0:
                    
                    # Player has at least on trump in remaining cards
                    ids_list = Helper.get_trumps(self.remaining_cards, state)
                    
                    if ids_list>0:
                        return [self.remaining_cards[i] for i in ids_list]
                    
                
            
            
                    
    def play_card(self, card):
        """Removes card from remaining_cards and puts card in played_cards at 
        States"""
        pass