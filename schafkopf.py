# -*- coding: utf-8 -*-
import random

from card import Card
from player import Player
from general_state import State

class Schafkopf():
    def __init__(self):
        # initialize cards and players
        self.cards = []
        for i in range(32):
            self.cards.append(Card(id=i))
            
        players = ['Claus', 'Sepp', 'Hans', 'Kreszenz']
        self.players = []
        for player in players:
            self.players.append(Player(name=player))
            
    def reset(self, dealer_id):
        # Shuffle and deal cards
        random.shuffle(self.cards)
        for i in range(len(self.players)):
            self.players[i].cards = self.cards[i*8:(i+1)*8]
        self.state = State(dealer_id)
    
    def step(self):
        pass
    
    
if __name__ == '__main__':
    N_EPISODES=100
    dealer_id=0
    schafkopf = Schafkopf()
    for _ in range(N_EPISODES):
        schafkopf.reset(dealer_id)
        dealer_id = (dealer_id + 1) % 4
        