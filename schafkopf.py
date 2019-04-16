# -*- coding: utf-8 -*-
import random

from card import Card
from player import Player
from general_state import State
from helper import Helper

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
        c = Helper.get_cards(self.players[0].cards, color=['herz'])
        pass
    
    def step(self):
        pass
    
    
if __name__ == '__main__':
    N_EPISODES=100
    dealer_id=0
    schafkopf = Schafkopf()
    for _ in range(N_EPISODES):
        schafkopf.reset()
        