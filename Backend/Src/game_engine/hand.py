from game_engine.deck import Deck


class Hand:

    # Players will come in in the correct order from the game_controller as a list
    def __init__(self, players, blinds):
        self._board = []
        self._pot = 0
        self._players = players
        self._deck = Deck()
        self._small_blind, self._big_blind = blinds
        self.deal_hand()

    def deal_hand(self):
        self.pay_blinds()
        for player in self._players:
            player.cards = self._deck.get_hand()

    def pay_blinds(self):
        if len(self._players) == 2:
            self._players[0].pay_blind(self._big_blind)
            self._players[1].pay_blind(self._small_blind)
        else:
            self._players[0].pay_blind(self._small_blind)
            self._players[1].pay_blind(self._big_blind)
