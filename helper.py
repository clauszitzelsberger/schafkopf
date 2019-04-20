# -*- coding: utf-8 -*-

class Helper():
    
    @staticmethod
    def get_cards(cards, color=None, number=None, trumps=None, state=None):
        assert type(cards)==list, 'Cards arg must be list type'
        assert type(color)==list or color is None, 'Color arg must be list type or None'
        assert type(number)==list or number is None, 'Number arg must be list type or None'
        assert type(trumps)==bool or trumps is None, 'Trumps arg must be bool type or None'
        if type(trumps)==bool:
            assert state is not None, 'State needs to be defined'
            
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
        return [card.color for card in cards], [card.number for card in cards]
    
    @staticmethod
    def __intersection(lst1, lst2): 
        return [i for i in lst1 if i in lst2] 
    
    @staticmethod
    def __difference(lst1, lst2):
        """
        set theoretic difference of lst1 and lst2 (lst1 \ lst2)"""
        return [i for i in lst1 if i not in lst2]
        