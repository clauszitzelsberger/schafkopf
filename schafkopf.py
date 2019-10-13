# -*- coding: utf-8 -*-
import random

import card
from player import Player
from general_state import State

random_playing = True

class Schafkopf():
    def __init__(self,
                 n_games=1,
                 players=['Claus', 'Sepp', 'Hans', 'Kreszenz'],
                 test=False):

        self.game_number = 0
        self.n_games = n_games
        #self.test = test

        self.api_dict = {'Selection': 'Game'}

        # initialize cards and players
        self.cards = []
        for i in range(32):
            self.cards.append(card.initialize(id=i))
            
        self.players = []
        for i in range(len(players)):
            self.players.append(Player(id=i, name=players[i]))

        self.reset()

    def api_get(self):
        """This function provides required information to select either a game or a card"""

        current_player_id = self.players_order[self.player_idx]
        self.api_dict['Player'] = current_player_id

        if self.api_dict['Selection'] == 'Game':
            self.api_dict['Cards'] = [card['name'] for card in self.players[current_player_id].cards]
            self.api_dict['Possibilities'] = \
                self.players[current_player_id].get_possible_games(self.state)
            self.api_dict['Possibilities'].extend([None])

        elif self.api_dict['Selection'] == 'Card':
            self.api_dict['Possibilities'] = \
                self.players[current_player_id].get_possible_cards(schafkopf.state)

        self.api_print()



    def api_set(self, selection):
        assert isinstance(int(selection), int), 'Input must be int type!'
        possibilities = range(len(self.api_dict['Possibilities']))
        selection = int(selection)
        assert selection in possibilities, 'Wrong selection!'

        selection = self.api_dict['Possibilities'][selection]

        if self.api_dict['Selection'] == 'Game':
            if selection is not None:
                self.step_game(self.api_dict['Player'], selection)
            self.player_idx += 1
            if self.player_idx == 4:
                self.player_idx = 0
                self.api_dict['Selection'] == 'Card'

        elif self.api_dict['Selection'] == 'Card':
            selection = next((card for card in self.api_dict['Possibilities'] if card['name'] == selection), None)
            self.step_card(self.api_dict['Player'], selection)



    def api_print(self):
        order = ['Player', 'Cards', 'Selection', 'Possibilities']
        for _, item in enumerate(order):
            if item in self.api_dict:
                if item == order[3]:
                    for j, possibility in enumerate(self.api_dict[item]):
                        print(f'{j}: {possibility}')
                else:
                    print(f'{item}: {self.api_dict[item]}')



    def reset(self):
        # Define dealer
        self.game_number += 1
        dealer_id = self.game_number % 4
        
        # Shuffle and deal cards
        random.seed(1)
        random.shuffle(self.cards)
        for i in range(len(self.players)):
            self.players[i].set_cards(self.cards[i*8:(i+1)*8])
        self.state = State(dealer_id)

        first_player = (self.state.dealer_id + 1) % 4
        self.players_order = self.set_order_of_players(first_player)
        self.player_idx = 0

        #print(f'Player: {first_player}')
        #print([card['name'] for card in schafkopf.players[i].cards])
        #print('Possible games:')
        #print(self.players[i].get_possible_games(schafkopf.state))
    
    def step_game(self, game_player_id, game=[None, None]):
        """Player selects a game"""
        self.players[game_player_id].select_game(game)
        self.state.set_game(game_player_id, game)
    
    def step_card(self, player_id, card):
        """Player plays a card"""
        self.players[player_id].play_card(card)
        self.state.set_card(player_id, card)

    def trick_result(self):
        """Identifies who gets the trick, updates first player"""
        first_player = self.state.set_trick_results()
        return first_player

    def game_result(self):
        """Identifies the winner(s), updates credit"""
        self.state.set_game_results()
        self.reset()

    @staticmethod    
    def set_order_of_players(first_player):
        """Returns a list of player ids in the correct order"""
        order = []
        for i in range(4):
            order.append((first_player + i) % 4)
        return order

if __name__ == '__main__':
    schafkopf = Schafkopf()

    while True:
        schafkopf.api_get()
        while True:
            try:
                selection = input('Selection: ')
                schafkopf.api_set(selection)
                break
            except Exception as e:
                print(e)

if __name__ == '__main__2':
    N_EPISODES=1
    schafkopf = Schafkopf()
    for e in range(1, N_EPISODES+1):
        schafkopf.reset()
        first_player = (schafkopf.state.dealer_id + 1) % 4
        players_order = schafkopf.set_order_of_players(first_player)

        # Select game
        for i in players_order:
            poss_games = schafkopf.players[i].get_possible_games(schafkopf.state)
            print(i)
            print([card['name'] for card in schafkopf.players[i].cards])
            print(poss_games)
            if len(poss_games)>0:
                sel_game_color = input('Select game color: ')
                sel_game_type = input('Select game type: ')
                sel_game = [None if sel_game_color=='None' else sel_game_color,
                            None if sel_game_type=='None' else sel_game_type]
                if sel_game != [None, None]:
                    schafkopf.step_game(i, sel_game)
            print('\n')

        # Iterate over 8 tricks
        for j in range(1, 9):
            players_order = schafkopf.set_order_of_players(first_player)

            # Select card
            for i in players_order:
                poss_cards = schafkopf.players[i].get_possible_cards(schafkopf.state)
                print(poss_cards)
                if random_playing:
                    poss_card_ids = [poss_card['id'] for poss_card in poss_cards]
                    sel_card_id = random.choice(poss_card_ids)
                else:
                    sel_card_id = int(input('Select card id: '))
                sel_card = next((card for card in poss_cards if card['id'] == sel_card_id), None)
                assert sel_card is not None, 'Selected card not part of possbile cards list'
                schafkopf.step_card(i, sel_card)

            # Who gets the trick?
            first_player = schafkopf.trick_result()
        schafkopf.game_result()