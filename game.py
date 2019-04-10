# -*- coding: utf-8 -*-

class Game():
    def __init__(self, color, kind):
        
        if [color, kind] != [None, None]:
                
            self.games = [
                    ['Eichel', 'Sauspiel'], ['Gras', 'Sauspiel'], ['Schellen', 'Sauspiel'],
                    ['Eichel', 'Solo'], ['Gras', 'Solo'], ['Herz', 'Solo'], ['Schellen', 'Solo'],
                    [None, 'Wenz']]
            
            assert type(color)==str or color is None, 'color argument must be string or None type'
            assert type(kind)==str, 'kind argument must be string type'
            assert [color, kind] in self.games, 'Invalid game defined: ' + color + ' ' + kind
            
            self.kind = kind
            self.color = color
            rewards = {
                    'Sauspiel': 20,
                    'Solo': 50,
                    'Wenz': 50
                    }
            self.reward = rewards[self.kind]
        
if __name__ == '__main__':
    game = Game(None, 'Wenz')