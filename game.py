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

def initialize(color, kind):
    assert type(color)==str or color is None, 'color argument must be string or None type'
    assert type(kind)==str, 'kind argument must be string type'
    assert [color, kind] in games, 'Invalid game defined: ' + color + ' ' + kind
    
    game = {'kind': kind,
            'color': color,
            'reward': rewards[kind]}
    return game