# -*- coding: utf-8 -*-

rewards = {'sauspiel': 20,
           'solo': 50,
           'wenz': 50}

games = [['eichel', 'sauspiel'], ['gras', 'sauspiel'], ['schellen', 'sauspiel'],
         ['eichel', 'solo'], ['gras', 'solo'], ['herz', 'solo'], ['schellen', 'solo'],
         [None, 'wenz']]

sauspiele = games[:3]
soli = games[3:7]
wenz = games[7]

class Game():
    def __init__(self, color, kind):
        
        if [color, kind] != [None, None]:            
            assert type(color)==str or color is None, 'color argument must be string or None type'
            assert type(kind)==str, 'kind argument must be string type'
            assert [color, kind] in games, 'Invalid game defined: ' + color + ' ' + kind
            
            self.kind = kind
            self.color = color
            
            self.reward = rewards[self.kind]


if __name__ == '__main__':
    game = Game(None, 'wenz')