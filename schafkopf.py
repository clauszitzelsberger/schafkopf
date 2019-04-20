# -*- coding: utf-8 -*-
import random

from card import Card
from player import Player
from general_state import State

class Schafkopf():
    def __init__(self):
        self.game_number = 0
        
        # initialize cards and players
        self.cards = []
        for i in range(32):
            self.cards.append(Card(id=i))
            
        players = ['Claus', 'Sepp', 'Hans', 'Kreszenz']
        self.players = []
        for i in range(len(players)):
            self.players.append(Player(id=i, name=players[i]))
            
    def reset(self):
        # Define dealer
        self.game_number += 1
        dealer_id = self.game_number % 4
        
        # Shuffle and deal cards
        random.shuffle(self.cards)
        for i in range(len(self.players)):
            self.players[i].set_cards(self.cards[i*8:(i+1)*8])
        self.state = State(dealer_id)
    
    def step_game(self, game_player_id, game):
        """Players select a game"""
        State.set_game(game_player_id, game)
    
    def step_card(self, player_id, card):
        """Player plays a card"""
        self.players[player_id].play_card(card)
        
    
    
if __name__ == '__main__':
    N_EPISODES=1
    schafkopf = Schafkopf()
    for e in range(1, N_EPISODES+1):
        schafkopf.reset()
        for i in range(len(schafkopf.players)):
            poss_games = schafkopf.players[i].get_possible_games(schafkopf.state)
            print(i)
            print([card.name for card in schafkopf.players[i].cards])
            print(poss_games)
            print('\n')
        