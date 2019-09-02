# -*- coding: utf-8 -*-

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
        self.game = None
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

        def highest_ober_or_unter(number='ober'):
            """Returns winner of trick """
            card_ids = self.get_cards(player_cards, number)
            if len(card_ids):
                cards = [player_cards[i] for i in ober_ids]

                # id < 8 => eicherl, id < 16 => gras, etc...
                return cards.index(min([i['id'] for i in cards]))

        player_cards = self.played_cards[self.trick]
        trump_ids = self.get_trumps(player_cards)

        if len(trump_ids) > 0:

            if self.game['kind'] != 'wenz':



            ober_ids = self.get_cards(player_cards, number='ober')
            if len(ober_ids) > 0:
                ober = [player_cards[i] for i in ober_ids]
                winner_trick = ober.index(min([i['id'] for i in ober]))


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
                card_ids = self.__intersection(self.get_trumps(cards, state), card_ids)
            else:
                card_ids = self.__difference(card_ids, self.get_trumps(cards, state))

        return card_ids

    def get_trumps(self, cards):
        """Returns subset of trumps in cards list based on state (selected game)"""

        card_colors, card_numbers = self.__card_lists(cards)

        if state.game is None or state.game['kind'] == 'sauspiel':
            card_ids = [i for i in range(len(cards))
                if card_colors[i]=='herz'
                or card_numbers[i] in ['unter', 'ober']]
        elif state.game['kind'] == 'solo':
            card_ids = [i for i in range(len(cards))
                if card_colors[i]==state.game['color']
                or card_numbers[i] in ['unter', 'ober']]
        else:
            card_ids = [i for i in range(len(cards))
                if card_numbers[i]=='unter']
        return card_ids

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

if __name__ == '__main__':
    state = State(1)
    state.set_trick_results()
