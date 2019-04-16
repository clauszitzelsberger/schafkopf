# -*- coding: utf-8 -*-

rewards = {'Sauspiel': 20,
           'Solo': 50,
           'Wenz': 50
           }
games = [['Eichel', 'Sauspiel'], ['Gras', 'Sauspiel'], ['Schellen', 'Sauspiel'],
         ['Eichel', 'Solo'], ['Gras', 'Solo'], ['Herz', 'Solo'], ['Schellen', 'Solo'],
         [None, 'Wenz']]

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
    game = Game(None, 'Wenz')