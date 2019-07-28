# -*- coding: utf-8 -*-

import numpy as np

number = ['siebener',
          'achter',
          'neuner',
          'zehner',
          'unter',
          'ober',
          'koenig',
          'sau']

value = [0, 0, 0, 10, 2, 3, 4, 11]

class Card():
    def __init__(self, id):
        
        # Id and one hot encoded id
        self.id = id
        self.one_hot = np.zeros(32)
        self.one_hot[id] = 1
        
        # Color and number
        if id < 8:
            self.color = 'eichel'
        elif id < 16:
            self.color = 'gras'
        elif id < 24:
            self.color = 'herz'
        else:
            self.color = 'schellen'
        self.number = number[id%8]
        
        # Value of card
        self.value = value[id%8]
        
        # Display name
        self.name = (self.color + ' ' + self.number)
        
        # Distinguish betwenn Unter+Ober and rest of cards
        if self.number in ['unter', 'ober']:
            self.not_ober_unter = False
        else:
            self.not_ober_unter = True