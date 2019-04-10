# -*- coding: utf-8 -*-

class Player():
    def __init__(self, id, name):
        self.name = name
        self.credit = 0
        self.cards = None
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

        return possible_games"""
    
    def __describe_cards(self):
        colors = []
        for card in self.cards:
            if card.not_ober_unter:
                colors.append(card.color)
        return set(colors)