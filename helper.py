# -*- coding: utf-8 -*-
NoneType = type(None)

class Helper():
    """Helper functions"""
    
    @staticmethod
    def get_cards(cards, color=None, number=None, trumps=None, state=None):
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
        if type(trumps)==bool:
            assert state is not None, 'State needs to be defined if trumps is criteria'
            
        card_colors, card_numbers = Helper.__card_lists(cards)
        
        card_ids = [i for i in range(len(cards))]
        
        if color is not None:
            card_ids = Helper.__intersection([i for i in range(len(cards)) if card_colors[i] in color], card_ids)
            
        if number is not None:
            card_ids = Helper.__intersection([i for i in range(len(cards)) if card_numbers[i] in number], card_ids)
        
        if trumps is not None:
            if trumps:
                card_ids = Helper.__intersection(Helper.get_trumps(cards, state), card_ids)
            else:
                card_ids = Helper.__difference(card_ids, Helper.get_trumps(cards, state))
                
        return card_ids
        
    @staticmethod        
    def get_trumps(cards, state):
        """Returns subset of trumps in cards list based on state (selected game)"""
        
        card_colors, card_numbers = Helper.__card_lists(cards)
        
        if state.game is None or state.game.kind == 'sauspiel':
            card_ids = [i for i in range(len(cards)) 
                if card_colors[i]=='herz' 
                or card_numbers[i] in ['unter', 'ober']]
        elif state.game.kind == 'solo':
            card_ids = [i for i in range(len(cards))
                if card_colors[i]==state.game.color
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
        