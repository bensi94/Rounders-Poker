from deck import Deck

class Hand:

    def __init__(self, players, blinds):
        self._board = []
        self._pot = 0
        self._players = players
        self._deck = Deck()
        self._small_blind, self._big_blind = blinds

    def deal_hand(self):
        self.pay_blinds()
        self.deal()

    def pay_blinds(self):
        if len(self._players) == 2:
            self._players[0].pay_blind(self._big_blind)
            self._players[1].pay_blind(self._small_blind)
        else:
            self._players[0].pay_blind(self._small_blind)
            self._players[1].pay_blind(self._big_blind)

    def deal():
        for player in self._players