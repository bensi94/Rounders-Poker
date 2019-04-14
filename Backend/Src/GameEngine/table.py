# External
from collections import OrderedDict
import random

# Internal
from GameEngine.constants import PENDING, RUNNING


class Table:

    def __init__(self, max_players, blinds):
        self._max_players = max_players
        self._small_blind, self._big_blind = blinds

        self._seats = OrderedDict()
        # Assign seats at the table to None and players will
        for seat in range(1, max_players+1):
            self._seats[seat] = None

        # Pending means the game is not running at table
        self._state = PENDING
        self._seat_count = 0
        # Dealer button
        self._button = None

    def sit_at_table(self, user, seat):
        if seat not in self._seats:
            return False, 'Invalid seat, user not seated'
        elif self._seats[seat] is not None:
            return False, 'Seat occupied, user not seated'

        self._seats[seat] = user
        self._seat_count += 1

        # If game is not running and two or
        # more player are seated the game starts
        if self._state == PENDING and self._seat_count > 1:
            self._state = RUNNING
            self._init_button()
        return True, 'User seated at seat: ' + str(seat)

    # Puts the dealer button in a valid
    def _init_button(self):
        valid_seats = []
        for seat in self._seats.keys():
            if self._seats[seat] is not None:
                valid_seats.append(seat)
        self._button = random.choice(valid_seats)

    def empty_seat(self, seat):
        if seat in self._seats:
            self._seat_count -= 1
            self._seats[seat] = None

        if self._seat_count < 2:
            self._state = PENDING

    def move_button(self):
        self._button += 1
        if self._button > self._max_players:
            self._button = 1

        while self._seats[self._button] is None:
            self._button += 1
            if self._button > self._max_players:
                self._button = 1

    def get_button(self):
        return self._button

    def update_blinds(self, blinds):
        self._small_blind, self._big_blind = blinds

    def get_blinds(self):
        return self._small_blind, self._big_blind
