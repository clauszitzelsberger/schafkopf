# -*- coding: utf-8 -*-
import unittest
import numpy as np
from helper import Helper
from card import Card

class TestHelper(unittest.TestCase):
    def test_get_cards(self):
        cards = []
        for i in range(32):
            cards.append(Card(id=i))
        
        self.assertEqual(Helper.get_cards(cards), 
                         list(np.arange(32)))
        self.assertEqual(Helper.get_cards(cards, 
                                          color=['eichel', 'schellen']),
                         list(np.append(np.arange(8), np.arange(24,32))))
        self.assertEqual(Helper.get_cards(cards, 
                                          color=['eichel'], 
                                          number=['siebener', 'koenig']),
                         [0, 6])
        
if __name__ == '__main__':
    unittest.main()