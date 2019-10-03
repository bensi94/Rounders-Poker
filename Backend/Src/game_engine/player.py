from game_engine import constants as const


class Player:

    def __init__(self, stack, seatnumber, user=''):
        self.stack = stack
        self.bet = 0
        self.status = const.STATUS_WAITING
        self.seatnumber = seatnumber
        self.last_action = ''
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

    # bet_amount function will be used for betting, raising and calling
    # because they work the same way.
    def bet_amount(self, amount):
        if amount > self.stack:
            # Returns False if the amount is invalid(more then stack)
            return False
        self.stack -= amount
        self.bet += amount
        # Returns True if the bet is valid
        return True

    def fold(self):
        self.status = const.STATUS_FOLDED

    def reset_bet(self):
        self.bet = 0

    def pay_blind(self, blind_val):
        if blind_val > self.stack:
            self.bet += self.stack
            self.stack = 0
        else:
            self.stack = self.stack - blind_val
            self.bet += blind_val
