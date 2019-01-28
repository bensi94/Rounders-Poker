from collections import OrderedDict
import random

class Table:
    
    def __init__(self, max_players, blinds):
        self._max_players = max_players
        self._small_blind, self._big_blind = blinds
        
        self._seats = OrderedDict()
        # Assign seats at the table to None and players will
        for seat in range(1, max_players+1):
            self._seats[seat] = None
        
        # Pending means the game is not running at table
        self._state = 'PENDING'
        self._player_count = 0
        # Dealer button
        self._button = None

    def sit_at_table(self, player, seat):
        if seat not in self._seats:
            return 'Invalid seat, player not seated'
        elif self._seats[seat] != None:
            return 'Seat occupied, player not seated'

        self._seats[seat] = player
        self._player_count += 1

        # If game is not running and two or more player are seated the game starts
        if self._state == 'PENDING' and self._player_count > 1:
            self._state = 'RUNNING'
            self._init_button()
        return 'Player seated at seat: ' + str(seat)

    # Puts the dealer button in a valid 
    def _init_button(self):
        valid_seats = []
        for seat in self._seats.keys():
            if self._seats[seat] != None:
                valid_seats.append(seat)
        self._button = random.choice(valid_seats)

    def empty_seat(self, seat):
        if seat in self._seats:
            self._player_count -= 1
            self._seats[seat] = None

        if self._player_count < 2:
            self._state = 'PENDING'
        
    def move_button(self):
        self._button += 1
        if self._button > self._max_players:
            self._button = 1
        
        while self._seats[self._button] == None:
            self._button += 1
            if self._button > self._max_players:
                self._button = 1
