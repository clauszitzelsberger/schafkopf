# -*- coding: utf-8 -*-

import game
#import card

class Player():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.credit = 0
        self.cards = None
        self.remaining_cards = None
        self.davonlaufen_possible = False
        self.davongelaufen = False
        self.rufsau = None
        self.possible_cards = []
        self.possible_games = []
        
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
        if state.game['kind'] is None:
            sauspiel = True
            wenz = True
            solo = True
        elif state.game['kind']=='sauspiel':
            wenz = True
            solo = True
        elif state.game['kind']=='wenz':
            solo = True
            
        self.possible_games = []

        if sauspiel:
            for sauspiel in game.sauspiele:
                if len(state.get_cards(self.cards, color=[sauspiel[0]], 
                                        trumps=False))>0:
                    if len(state.get_cards(self.cards, color=[sauspiel[0]],
                                           number=['sau']))==0:
                        self.possible_games.append(sauspiel)
        
        if wenz:
            self.possible_games.append(game.wenz)
        
        if solo:
            self.possible_games.extend(game.soli)
                                  
        return self.possible_games
    
    def get_possible_cards(self, state):
        """
        Get all cards which a player can play based on his remaining cards, the cards
        that have been already played by other players in this trick, and the game
        which is being played"""
        
        lead_card = state.played_cards[state.trick][state.first_player]
        
        if state.game['kind'] == 'sauspiel':
            
            rufsau = {'color': state.game.color,
                      'number': 'sau'}
            
            # Check if player has rufsau
            ids_list = state.get_cards(self.remaining_cards, 
                                       color=[rufsau['color']], 
                                       number=[rufsau['number']])
            
            if len(ids_list)==1:
                has_rufsau = True
                rufsau = self.remaining_cards[ids_list[0]]
        
            # Player is first one to play a card in this trick
            if state.first_player==self.id:
                
                assert lead_card==[None, None]
                
                # Check if player has rufsau
                if not has_rufsau:
                    self.possible_cards = self.remaining_cards
                
                # Player has rufsau
                else:
                    # Player has more than 3 cards with rufsau's color
                    # davonlaufen is possible
                    if len(state.get_cards(self.remaining_cards,
                                            color=[rufsau[0]],
                                            trumps=False))>=4:
                        self.davonlaufen_possible = True
                        self.rufsau = rufsau
                        self.possible_cards = self.remaining_cards
                    # Player has less then 4 cards with rufsau's color
                    # Can play either rufsau or any other card with a color unlike rufsau
                    else:
                        colors_unlike_rufsau = [c for c in self.remaining_cards.colors if c!=rufsau['color'] ]
                        possible_cards = state.get_cards(self.remaining_cards,
                                                          color=colors_unlike_rufsau)
                        possible_cards.append(rufsau)
                        self.possible_cards = possible_cards
             
            # Player is not the first one in this trick
            else:
                
                # Lead card is a trump
                if len(state.get_trumps([lead_card], state))>0:
                    
                    # Player has at least on trump in remaining cards
                    ids_list = state.get_trumps(self.remaining_cards)
                    
                    if ids_list>0:
                        self.possible_cards = [self.remaining_cards[i] for i in ids_list]
                    
                    # No trump in remaining cards
                    else:
                        if self.davongelaufen:
                            self.possible_cards = self.remaining_cards
                        else:
                            if has_rufsau and state.trick==8:
                                self.possible_cards = self.remaining_cards.copy
                                self.possible_cards.remove(rufsau)
                            else:
                                self.possible_cards = self.remaining_cards
                                
                # Lead card has rufsaus's color and player has rufsau and not davongelaufen
                elif ((lead_card['color']==state.game['color']) and 
                      has_rufsau and 
                      (not self.davongelaufen)):
                    self.possible_cards = [rufsau]
                
                # Other cases
                else:
                    ids_list = state.get_cards(self.remaining_cards, color=lead_card['color'])
                    
                    # Player has lead cards color
                    if len(ids_list)>0:
                        self.possible_cards = [self.remaining_cards[i] for i in ids_list]
                    else:
                        if self.davongelaufen:
                            self.possible_cards = self.remaining_cards
                        else:
                            if has_rufsau and state.trick==8:
                                self.possible_cards = self.remaining_cards.copy
                                self.possible_cards.remove(rufsau)
                            else:
                                self.possible_cards = self.remaining_cards
                                
        # Wenz or Solo
        else:
            # Player is first one to play a card in this trick
            if state.first_player == self.id:
                self.possible_cards = self.remaining_cards
            else:
                # Lead card is a trump    
                if len(state.get_trumps([lead_card]))>0:
                    # Player has at least on trump in remaining cards
                    ids_list = state.get_trumps(self.remaining_cards)
                    
                    if len(ids_list)>0:
                        self.possible_cards = [self.remaining_cards[i] for i in ids_list]
                    
                    # No trump in remaining cards
                    else:
                        self.possible_cards = self.remaining_cards
                        
                # Lead card is a color
                else:
                    ids_list = state.get_cards(self.remaining_cards, color=[lead_card['color']])
                    
                    # Player has lead cards color
                    if len(ids_list)>0:
                        self.possible_cards = [self.remaining_cards[i] for i in ids_list]
                    else:
                        self.possible_cards = self.remaining_cards
                
        return self.possible_cards
            
    def select_game(self, game):
        """Checks selected game"""
        assert game in self.possible_games

                
    def play_card(self, card):
        """Checks selected card and removes card from remaining_cards"""
        assert card in self.possible_cards #not required, because assertion already in schafkopf.py
        
        if self.davonlaufen_possible and card!=self.rufsau:
            self.davongelaufen=True
        
        self.remaining_cards.remove(card)
        self.possible_cards = []