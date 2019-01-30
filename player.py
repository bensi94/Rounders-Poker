from constants import STATUS_ACTIVE, STATUS_FOLDED

class Player:

    def __init__(self, stack):
        self._stack = stack
        self._bet = 0
        self._status = STATUS_ACTIVE

    def give_hand(self, hand):
        self._hand = hand
        self._bet = 0
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
        self._bet = 0
        self._status = STATUS_FOLDED

    # The state of the player is an object that is used to pass to other players
    # To determine possible actions
    def get_state(self):
        return {
            "status": self._status,
            "stack": self._stack,
            "bet": self._bet
        }
