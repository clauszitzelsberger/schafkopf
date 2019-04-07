# -*- coding: utf-8 -*-
import random

from card import Card
from player import Player

class Schafkopf():
    def __init__(self):
        # initialize cards and players
        self.cards = []
        for i in range(32):
            self.cards.append(Card(id=i))
            
        players = ['Claus', 'Sepp', 'Hans', 'Schorsch']
        self.players = []
        for player in players:
            self.players.append(Player(name=player))
    
    def reset(self):
        # Shuffle and deal cards
        random.shuffle(self.cards)
        for i in range(len(self.players)):
            self.players[i].cards = self.cards[i*8:(i+1)*8]
    
    def step(self):
        pass
    
    
if __name__ == '__main__':
    sk = Schafkopf()
    sk.reset()