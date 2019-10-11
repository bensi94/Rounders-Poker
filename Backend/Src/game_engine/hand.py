from game_engine.deck import Deck
from collections import deque

from game_engine import constants as const


class Hand:

    # Players will come in in the correct order from the game_controller as a list
    def __init__(self, players, blinds):
        self._board = []
        self._pot = 0
        self._side_pots = []
        self._current_max_bet = 0
        self._players = players
        self._deck = Deck()
        self._small_blind, self._big_blind = blinds
        self.action_queue = deque()
        self.deal_hand()
        self.action_on_player = None
        self.last_legal_raise = 0
        self.stage = const.PREFLOP

    def deal_hand(self):
        for player in self._players:
            if player.status == const.STATUS_ACTIVE:
                cards = self._deck.get_hand()
                player.give_hand(cards)

        self.pay_blinds()

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

        self._pot = self._players[0].bet + self._players[1].bet

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

    # This method is used to update the table from all states, after a player action or after a deal
    def update_table(self):
        self.check_and_update_side_pots()

        # First we need to get the counts
        active_count = 0
        all_in_count = 0
        for player in self._players:
            if player.status == const.STATUS_ACTIVE:
                active_count += 1
            elif player.status == const.STATUS_ALL_IN:
                all_in_count += 1

        if all_in_count == 0 and active_count <= 1:
            return {
                "response": const.END_HAND
            }

        if not self.action_queue:
            if active_count <= 1:
                return {
                    "response": const.END_HAND
                }

            # If the action queue is empty and still has players, it means that there are
            # no remaining actions on that street
            if self.stage == const.PREFLOP:
                # PREFLOP --> FLOP
                self.stage = const.FLOP
                self._board = [*self._deck.get_flop()]
                self.fill_action_queue()
            elif self.stage == const.FLOP:
                # FLOP --> RIVER
                self.stage = const.TURN
                self._board.append(self._deck.get_next_card())
                self.fill_action_queue()
            elif self.stage == const.TURN:
                # TURN --> RIVER
                self.stage = const.RIVER
                self._board.append(self._deck.get_next_card())
                self.fill_action_queue()
            else:
                # River is done and hand needs to go to showdown
                return {
                    "response": const.END_HAND
                }

        self.action_on_player = self.action_queue.popleft()

        return {
            "response": const.PLAYER_ACTION,
            "player": self.action_on_player
        }

    def player_action(self, action, player):
        player.validate_action(action)
        old_player_bet = player.bet
        player.action(action)

        # if the action is a Bet or Raise the action Queue needs to be updated
        if action['type'] == const.BET or action['type'] == const.RAISE:
            # If there is a raise we need ot update the last legal raise
            if action['type'] == const.RAISE:
                # This happens if player goes all in for less than a legal raise
                if player.bet < self._big_blind * 2:
                    self.last_legal_raise = self._big_blind
                else:
                    if self._current_max_bet + self.last_legal_raise < player.bet:
                        self.last_legal_raise = player.bet - self._current_max_bet

            # Updateing the current_max_bet
            self._current_max_bet = player.bet
            self.update_action_queue()

        if (action['type'] == const.CALL or
                action['type'] == const.BET or action['type'] == const.RAISE):
            self._pot += action['amount'] - old_player_bet

    # Checks if a side pot should be created or updated
    def check_and_update_side_pots(self):

        # First we sort the players depending on how much they have already put out
        sorted_players = sorted(self._players, key=lambda sort_key: (
            sort_key.total_bets_in_hand, sort_key.stack))

        # Carry over is essentially used to move dead money (where the player is not all in)
        carry_overs = []
        # All new all_in amounts get added to t hits list
        previous_all_in_amounts = []

        for i, player in enumerate(sorted_players):

            # We only need to make a side pot if a player is all in
            if player.status == const.STATUS_ALL_IN:
                # Because it's sorted by total bet amount we know that all players with
                # more than current player can be part of this side pot
                player_count = len(sorted_players[i:])
                amount = player.total_bets_in_hand * player_count
                players = []

                # We need to collect all the players that can win the current side pot
                # They need to be active or all in
                for sub_player in sorted_players[i:]:
                    if (sub_player.status == const.STATUS_ACTIVE or
                            sub_player.status == const.STATUS_ALL_IN):
                        players.append(sub_player)

                for i, prev_amount in enumerate(previous_all_in_amounts):
                    # Because the prev all_in array is in fact sorted, because of the player sort
                    # We can use the amount that was the previous before to subtract form current
                    # previous, so we do not over subtract
                    if i != 0:
                        prev_amount = prev_amount - previous_all_in_amounts[i-1]

                    # If previous all ins are less then carry overs, we need to subtract them
                    # from the carry_overs because they are already in a side pot
                    for i, carry_over in enumerate(carry_overs):
                        if prev_amount < carry_over:
                            carry_overs[i] -= prev_amount

                    amount -= prev_amount * player_count

                amount += sum(carry_overs)

                self._side_pots.append({
                    "pot": amount,
                    "players": set(players)
                })

                carry_overs = []
                previous_all_in_amounts.append(player.total_bets_in_hand)
            else:
                carry_overs.append(player.total_bets_in_hand)

    def get_hand_obj(self):
        pass
