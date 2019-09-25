from game_engine.constants import STATUS_ACTIVE, STATUS_FOLDED


class Player:

    def __init__(self, stack, seat_number):
        self._stack = stack
        self._bet = 0
        self._status = STATUS_ACTIVE
        self._seat_number = seat_number

    def get_player_obj(self):
        return {
            "stack": self._stack,
            "bet": self._bet,
            "status": self._status
        }

    def give_hand(self, hand):
        self._hand = hand
        self._status = STATUS_ACTIVE

    def set_seat(self, seat):
        self._seat = seat

    def get_seat(self):
        return self._seat

    # Bet function will be used for betting, raising and calling
    # because they work the same way.
    def bet(self, amount):
        if amount > self._stack:
            # Returns False if the amount is invalid(more then stack)
            return False
        self._stack -= amount
        self._bet += amount
        # Returns True if the bet is valid
        return True

    def fold(self):
        self._status = STATUS_FOLDED

    def reset_bet(self):
        self._bet = 0

    def pay_blind(self, blind_val):
        if blind_val > self._stack:
            self._bet += self._stack
            self._stack = 0
        else:
            self._stack = self._stack - blind_val
            self._bet += blind_val

    # The state of the player is an object that is used to
    #  pass to other players to determine possible actions
    def get_state(self):
        return {
            "status": self._status,
            "stack": self._stack,
            "bet": self._bet
        }
