# -*- coding: utf-8 -*-

class Player():
    def __init__(self, id, name):
        self.name = name
        self.credit = 0
        self.cards = None
        self.remaining_cards = None
        
    def set_cards(self, cards):
        self.cards = cards
        self.remaining_cards = cards
        
    def get_cards(self, color=None, number=None, trumps=None, state=None):
        assert type(color)==list or color is None, 'Color arg must be list type or None'
        assert type(number)==list or number is None, 'Number arg must be list type or None'
        assert type(trumps)==bool or trumps is None, 'Trumps arg must be bool type or None'
        if type(trumps)==bool:
            assert state is not None, 'State needs to be defined'
            
            
        
        
        if trumps:
            assert state is not None, 'State needs to be defined if trumps are requested'
        if color is not None:
            assert type(color)==list, 'Color arg must be list type'
        if number is not None:
            assert type(number)==list, 'Number arg must be list tpye'
        
        cards = []
        if trumps:
            pass
        else:
            for card in self.remaining_cards:
                if (card.color in color)==True and (card.number in number)==True:
                    cards.append(card)
                    
    """
    def get_possible_games(self, state):
        #game_player = state_overall.state_overall['game_player']
        #game =  state_overall.state_overall['game']
        #dealed_cards = self.state_player['dealed_cards']
        #possible_games = self.rules.games

        # No player defined: one is free to choose a game
        if state.game_player == None:
            
            
            # iterate over every color (except herz)
            for color in [0,1,3]:
                if len(self.\
                    rules.\
                    get_specific_cards2(cards_list=dealed_cards,
                    card=[color, None],
                    game=[color, 0]))==0\
                    or [color,7] in dealed_cards:
                    possible_games.remove([color, 0])
        elif game[1] == 0: #someone already selected a sauspiel
            for color in [0,1,3]:
                possible_games.remove([color, 0])
        elif game[1] == 2: #someone already selected a wenz
            for color in [0,1,3]:
                possible_games.remove([color, 0])
            possible_games.remove([None, 2])
        else:
            possible_games = []

        return possible_games
    
    def __card_colors(self):
        colors = []
        for card in self.cards:
            if card.not_ober_unter:
                colors.append(card.color)
        return set(colors)"""