from game_engine import constants as const


class Player:

    def __init__(self, stack, seatnumber, user=''):
        self.stack = stack
        self.bet = 0
        self.total_bets_in_hand = 0
        self.status = const.STATUS_WAITING
        self.seatnumber = seatnumber
        self.last_action = ''
        self.possible_actions = []
        self.user = user
        self.cards = ('', '')

    def __str__(self):
        return str(self.get_player_obj())

    def __repr__(self):
        return self.__str__()

    def get_player_obj(self):
        return {
            "user": self.user,
            "seatnumber": self.seatnumber,
            "status": self.status,
            "last_action": self.last_action,
            "stack": self.stack,
            "bet": self.bet
        }

    def give_hand(self, hand):
        self.hand = hand
        self.status = const.STATUS_ACTIVE
        self.total_bets_in_hand = 0
        self.reset_bet()
        self.last_action = ''

    def action(self, action):
        action_type = action['type']
        if action_type == const.CALL or action_type == const.BET or action_type == const.RAISE:
            self.bet_amount(action['amount'])
        elif action_type == const.FOLD:
            self.fold()
            self.status = const.STATUS_FOLDED

        self.last_action = action_type

    # bet_amount function will be used for betting, raising and calling
    # because they work the same way.
    def bet_amount(self, amount):
        if amount > self.stack:
            # Returns False if the amount is invalid(more then stack)
            return False
        self.stack -= amount - self.bet
        self.bet = amount

        if self.stack == 0:
            self.status = const.STATUS_ALL_IN
        # Returns True if the bet is valid
        return True

    def fold(self):
        self.status = const.STATUS_FOLDED

    def reset_bet(self):
        self.bet = 0

    def pay_blind(self, blind_val, action_name):
        if blind_val > self.stack:
            self.bet += self.stack
            self.stack = 0
            self.status = const.STATUS_ALL_IN
        else:
            self.stack = self.stack - blind_val
            self.bet += blind_val

        self.last_action = action_name

    def get_possible_actions(
            self, current_max_bet, last_legal_raise, big_blind, all_players_all_in=False):

        actions = []

        # PASSIVE PART (CHECK/CALL)
        if current_max_bet == 0 or current_max_bet == self.bet:
            actions.append({
                "type": const.CHECK
            })
        else:
            amount = 0

            # Checks if player stack is less then the current bet
            if self.stack + self.bet < current_max_bet:
                amount = self.stack + self.bet
            # If the player can afford it, the call needs to be at least on BB
            elif current_max_bet < big_blind:
                amount = big_blind
            else:
                amount = current_max_bet

            actions.append({
                "type": const.CALL,
                "amount": amount
            })

        # AGRESSIVE PART (BET/RAISE)
        if not all_players_all_in and current_max_bet < self.stack + self.bet:
            if current_max_bet == 0:
                actions.append({
                    "type": const.BET,
                    "min": self.stack if self.stack < big_blind else big_blind,
                    "max": self.stack
                })
            else:
                max_bet = self.stack + self.bet
                min_raise_allowed = 0

                # Checks for the case when the big_blind can not afford the blind
                if current_max_bet < big_blind:
                    min_raise_allowed = big_blind*2
                elif last_legal_raise == 0:
                    min_raise_allowed = current_max_bet*2
                elif current_max_bet < big_blind*2:
                    min_raise_allowed = big_blind*2
                else:
                    min_raise_allowed = current_max_bet + last_legal_raise

                if (current_max_bet == self.bet or  # This case only occurs if player is big blind
                        self.bet == 0 or current_max_bet - last_legal_raise >= self.bet):
                    actions.append({
                        "type": const.RAISE,
                        "min": max_bet if max_bet < min_raise_allowed else min_raise_allowed,
                        "max": max_bet
                    })

        # FOLD PART
        actions.append({
            "type": const.FOLD
        })

        self.possible_actions = actions
        return actions

    # Takes in a action and checks it valid based what actions are possible
    def validate_action(self, action):
        for a in self.possible_actions:
            # First the type has to be correct
            if action['type'] == a['type']:
                # If it's a call the amount needs to be correct
                if action['type'] == const.CALL and action['amount'] != a['amount']:
                    raise ValueError('Action failed: Invalid Amount')
                # If it's a bet it needs to be in the correct min/max range
                elif action['type'] == const.BET or action['type'] == const.RAISE:
                    if action['amount'] < a['min'] or action['amount'] > a['max']:
                        raise ValueError('Action failed: Invalid Amount')
                    else:
                        return
                else:
                    return

        raise ValueError('Action failed: Invalid action type')
