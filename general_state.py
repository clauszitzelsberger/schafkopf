# -*- coding: utf-8 -*-

class State():
    """
    Class which stores every information of the game which is
    available for every player:
        - dealer
        - which game is played
        - scores
        - etc.
    """
    def __init__(dealer_id):
        self.dealer_id = dealer_id