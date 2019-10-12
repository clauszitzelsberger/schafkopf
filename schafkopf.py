# -*- coding: utf-8 -*-
import random

import card
from player import Player
from general_state import State

class Schafkopf():
    def __init__(self):
        self.game_number = 0
        
        # initialize cards and players
        self.cards = []
        for i in range(32):
            self.cards.append(card.initialize(id=i))
            
        players = ['Claus', 'Sepp', 'Hans', 'Kreszenz']
        self.players = []
        for i in range(len(players)):
            self.players.append(Player(id=i, name=players[i]))
            
    def reset(self):
        # Define dealer
        self.game_number += 1
        dealer_id = self.game_number % 4
        
        # Shuffle and deal cards
        random.seed(1)
        random.shuffle(self.cards)
        for i in range(len(self.players)):
            self.players[i].set_cards(self.cards[i*8:(i+1)*8])
        self.state = State(dealer_id)
    
    def step_game(self, game_player_id, game=[None, None]):
        """Player selects a game"""
        self.players[game_player_id].select_game(game)
        self.state.set_game(game_player_id, game)
    
    def step_card(self, player_id, card):
        """Player plays a card"""
        self.players[player_id].play_card(card)
        self.state.set_card(player_id, card)

    def trick_result(self):
        """Identifies who gets the trick, updates first player"""
        first_player = self.state.set_trick_results()
        return first_player

    def game_result(self):
        """Count values of cards, identifies the winner(s), updates credit"""
        pass

    @staticmethod    
    def set_order_of_players(first_player):
        """Returns a list of player ids in the correct order"""
        order = []
        for i in range(4):
            order.append((first_player + i) % 4)
        return order
    
if __name__ == '__main__':
    N_EPISODES=1
    schafkopf = Schafkopf()
    for e in range(1, N_EPISODES+1):
        schafkopf.reset()
        first_player = (schafkopf.state.dealer_id + 1) % 4
        players_order = schafkopf.set_order_of_players(first_player)
        
        # Select game
        for i in players_order:
            poss_games = schafkopf.players[i].get_possible_games(schafkopf.state)
            print(i)
            print([card['name'] for card in schafkopf.players[i].cards])
            print(poss_games)
            if len(poss_games)>0:
                sel_game_color = 'schellen'#input('Select game color: ')
                sel_game_type = 'solo'#input('Select game type: ')
                sel_game = [None if sel_game_color=='None' else sel_game_color, 
                            None if sel_game_type=='None' else sel_game_type]
                schafkopf.step_game(i, sel_game)
            print('\n')
        
        # Iterate over 8 tricks
        for j in range(1, 9):
            players_order = schafkopf.set_order_of_players(first_player)
            
            # Select card
            for i in players_order:
                poss_cards = schafkopf.players[i].get_possible_cards(schafkopf.state)
                print(poss_cards)
                sel_card_id = int(input('Select card id: '))
                sel_card = next((card for card in poss_cards if card['id'] == sel_card_id), None)
                assert sel_card is not None, 'Selected card not part of possbile cards list'
                schafkopf.step_card(i, sel_card)
             
            # Who gets the trick?   
            first_player = schafkopf.trick_result()
        schafkopf.game_result()