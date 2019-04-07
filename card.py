# -*- coding: utf-8 -*-

class Card():
    def __init__(self, id):
        self.id = id
        if id < 8:
            self.color = 'eichel'
        elif id < 16:
            self.color = 'gras'
        elif id < 24:
            self.color = 'herz'
        else:
            self.color = 'schellen'
            
        number = [
                'siebener',
                'achter',
                'neuner',
                'zehner',
                'unter',
                'ober',
                'koenig',
                'sau'
                ]
        
        self.number = number[id%8]