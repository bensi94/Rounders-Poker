from game_engine.deck import Deck
from collections import deque

from game_engine import constants as const


class Hand:

    # Players will come in in the correct order from the game_controller as a list
    def __init__(self, players, blinds):
        self._board = []
        self._pot = 0
        self._current_max_bet = 0
        self._players = players
        self._deck = Deck()
        self._small_blind, self._big_blind = blinds
        self.action_queue = deque()
        self.deal_hand()
        self.action_on_player = None
        self.last_legal_raise = 0

    def deal_hand(self):
        self.pay_blinds()
        for player in self._players:
            player.cards = self._deck.get_hand()

        # In heads up we can manually add the players to the first queue
        if len(self._players) == 2:
            if self._players[1].status == const.STATUS_ACTIVE:
                self.action_queue.append(self._players[1])
            if self._players[0].status == const.STATUS_ACTIVE:
                self.action_queue.append(self._players[0])
        else:
            # We use the update_action_queue as workaround for the initial fill
            self.update_action_queue(self._players[1])
            # Manually add the big blind to the action queue
            if self._players[1].status == const.STATUS_ACTIVE:
                self.action_queue.append(self._players[1])

    def pay_blinds(self):
        # Blinds are different if we are heads up
        if len(self._players) == 2:
            self._players[0].pay_blind(self._big_blind, const.POST_BB)
            self._players[1].pay_blind(self._small_blind, const.POST_SB)
            self._current_max_bet = self._players[0].bet
        else:
            self._players[0].pay_blind(self._small_blind, const.POST_SB)
            self._players[1].pay_blind(self._big_blind, const.POST_BB)
            self._current_max_bet = self._players[1].bet

    # This method is used after a bet or raise to add active players to the action Queue
    def update_action_queue(self, last_action_player):
        last_player_index = self._players.index(last_action_player)
        # We start on the player left to the one that did last
        current_index = last_player_index + 1

        # This loop treats the players_list as a circle
        while True:
            # If we go out of bounds the index is set to 0
            if current_index >= len(self._players):
                current_index = 0

            # We break out of the loop once we have finished the circle
            if current_index == last_player_index:
                break

            # Players that are active and not currently in the Queue will be added to it
            if (self._players[current_index] not in self.action_queue and
                    self._players[current_index].status == const.STATUS_ACTIVE):

                self.action_queue.append(self._players[current_index])

            current_index += 1

    # This method is used when flop, turn or river has just been dealt and no one has done yet
    def fill_action_queue(self):
        for player in self._players:
            if player.status == const.STATUS_ACTIVE:
                self.action_queue.append(player)

    def next_player_action(self):
        pass

    def player_action(self, action, player):
        player.validate_action(action)

        if action['type'] == const.BET or action['type'] == const.RAISE:
            self._current_max_bet = player.bet
            self.update_action_queue()

    def get_hand_obj(self):
        pass
