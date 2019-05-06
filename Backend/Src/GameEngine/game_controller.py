# Each game controller control single table flow
# For now it's meant for cash game tables, might change to
# layer supertype pattern when tournaments come in later
from table import Table
from hand import Hand
from constants import MAX_PLAYERS, SMALL_BLIND, BIG_BLIND

class GameController:

    def __init__(self):
        self._table = Table(MAX_PLAYERS, (SMALL_BLIND, BIG_BLIND))
        self._players = {}

    # This function uses the button to order the players in right order
    # Button player last, others before
    def get_button_ordered_players(self):
        button = self._table.get_button()
        players_positions = sorted(self._players.keys())
        more_then_button = []
        less_then_button = []

        # Here we do a little tricks around the button to position the
        # players in the right order
        for position in players_positions:
            if position < button:
                less_then_button.append(self._players[position])
            elif position > button:
                more_then_button.append(self._players[position])

        # If there are players in higher seat then button they come first
        # Then seat 1 to button and the button seat last
        return more_then_button + less_then_button + [self._players[button]]

    
    def run_hand(self):
        self._hand = Hand(self.get_button_ordered_players(), self._table.get_blinds())
        self._hand.deal_hand()
