# -*- coding: utf-8 -*-
# Note: There are two different meaning of card_ids
# 1. index in a list of cards
# 2. unique id which is used in card.py
# TODO: card_ids and card_idx should be used

import numpy as np

import game
NoneType = type(None)
max_score = 120

class State():
    """
    Stores every information of the game which is
    available for every player:
        - dealer
        - which game is played
        - scores
        - etc.
    and handles overall methods which are valid for all players
    like results, scores, etc.
    """
    def __init__(self, dealer_id):
        self.dealer_id = dealer_id
        self.first_player = (dealer_id + 1) % 4
        self.game = {'kind': None, 'color': None}
        self.game_player_id = None
        self.played_cards = [[None]*4]*8
        self.scores = [0, 0, 0, 0]
        self.trick = 0

    def set_game(self, player_id, selected_game=[None, None]):
        """Sets game and respective player id"""

        if selected_game!=[None, None]:
            assert isinstance(player_id, int), 'player_id argument must be int type'
            assert isinstance(selected_game, list)
            assert len(selected_game)==2
            self.game_player_id = player_id
            self.game = game.initialize(selected_game[0], selected_game[1])

    def set_card(self, player_id, card):
        """Puts card into played_cards"""
        self.played_cards[self.trick][player_id] = card

    def set_trick_results(self):
        """Returns winner of trick and updates first_player, scores and trick"""

        highest_card = self.get_highest_card()
        winner_trick = highest_card

        self.first_player = winner_trick

        # Update scores
        additional_scores = [0, 0, 0, 0]
        additional_scores[winner_trick] = sum([card['value'] for card in self.played_cards[self.trick]])
        self.update_scores(additional_scores)

        self.trick += 1

        return winner_trick

    def set_game_results(self):
        """
        Evaluates game, updates credit, identifies winner(s)
        """
        opponents = [0, 1, 2, 3]
        opponents.remove(self.game_player_id)

        if self.game['kind'] == 'sauspiel':
            team_mate = self.get_team_mate()

    def get_team_mate(self):
        """
        Returns team mate player id for sauspiel only
        """
        assert self.game['kind'] == 'sauspiel', "No team mate for solo or wenz"

        rufsau = {'color': self.game['color'],
                  'number': 'sau'}

        # Identify which player played rufsau
        played_cards = np.array(self.played_cards)
        played_cards = np.squeeze(played_cards.reshape(32, -1, 2), axis=1)
        return played_cards.tolist().index(rufsau)%4


    def update_scores(self, additional_scores=[0, 0, 0, 0]):
        """Update scores of each player"""

        assert isinstance(additional_scores, list)
        self.scores += additional_scores
        assert sum(self.scores)<=max_score

    def get_cards(self, cards, color=None, number=None, trumps=None):
        """Returns subset of cards based on given criteria

        params
        =====
            cards (list), remaining cards
            color (list), list of colors to be selected from cards list
            number (list), list of numbers to be selected from cards list
            trumps (bool), whether trumps should be selected of not
            state (state class), to determine which trumps to be selected based on game
        """
        assert isinstance(cards, list)
        assert isinstance(color, (list, NoneType))
        assert isinstance(number, (list, NoneType))
        assert isinstance(trumps, (bool, NoneType))

        card_colors, card_numbers = self.__card_lists(cards)

        card_ids = [i for i in range(len(cards))]

        if color is not None:
            card_ids = self.__intersection([i for i in range(len(cards)) if card_colors[i] in color], card_ids)

        if number is not None:
            card_ids = self.__intersection([i for i in range(len(cards)) if card_numbers[i] in number], card_ids)

        if trumps is not None:
            if trumps:
                card_ids = self.__intersection(self.get_trumps(cards), card_ids)
            else:
                card_ids = self.__difference(card_ids, self.get_trumps(cards))

        return card_ids

    def get_trumps(self, cards):
        """Returns subset of trumps in cards list based on state (selected game)"""

        card_colors, card_numbers = self.__card_lists(cards)

        if self.game['kind'] is None or self.game['kind'] == 'sauspiel':
            card_ids = [i for i in range(len(cards))
                if card_colors[i]=='herz' or card_numbers[i] in ['unter', 'ober']]
        elif self.game['kind'] == 'solo':
            card_ids = [i for i in range(len(cards))
                if card_colors[i]==self.game['color'] or card_numbers[i] in ['unter', 'ober']]
        else:
            card_ids = [i for i in range(len(cards))
                if card_numbers[i]=='unter']
        return card_ids

    def get_highest_card(self):
        """Returns highest card id, player who got the trick resp"""

        def get_highest_card_of_a_kind(cards):
            """Returns card with the highest id which is the highest card if a list of
            - obers and unters (for sauspiel and solo)
            - unters (for wenz)
            - cards with one color only
            is provided
            """
            card_ids = [card['id'] for card in cards]
            return card_ids.index(max(card_ids))

        played_cards = self.played_cards[self.trick]
        lead_card = played_cards[self.first_player]

        # If no trumps in played cards, highest card with color of lead card wins
        trump_ids = self.get_trumps(played_cards)
        if len(trump_ids) == 0:
            lead_card_color_card_ids = self.get_cards(played_cards, color=[lead_card['color']])
            lead_card_color_cards = self.__card_ids_to_card_objs(lead_card_color_card_ids, played_cards)
            highest_card_id = get_highest_card_of_a_kind(lead_card_color_cards)
        else:
            # If there are trumps in played cards, distinguish if there are also obers and unters
            trumps = self.__card_ids_to_card_objs(trump_ids, played_cards)
            ober_unter_ids = self.get_cards(trumps, number=['unter', 'ober'])
            obers_unters = self.__card_ids_to_card_objs(ober_unter_ids, played_cards)

            # If there are no obers and unters in played cards
            if len(ober_unter_ids) == 0:
                highest_card_id = get_highest_card_of_a_kind(trumps)
            else:
                highest_card_id = get_highest_card_of_a_kind(obers_unters)

        return highest_card_id


    @staticmethod
    def __card_lists(cards):
        """Returns two lists, one for color, one for number given a cards list"""
        return [card['color'] for card in cards], [card['number'] for card in cards]

    @staticmethod
    def __intersection(lst1, lst2):
        """Returns all elements which are in both lists"""
        return [i for i in lst1 if i in lst2]

    @staticmethod
    def __difference(lst1, lst2):
        """Returns theoretic difference of lst1 and lst2 (lst1 \ lst2)"""
        return [i for i in lst1 if i not in lst2]

    @staticmethod
    def __card_ids_to_card_objs(card_ids, cards):
        assert isinstance(card_ids, list)
        assert isinstance(cards, list)
        return [cards[i] for i in card_ids]

if __name__ == '__main__':
    state = State(1)
    state.set_trick_results()
