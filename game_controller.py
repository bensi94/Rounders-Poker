# Each game controller control single table flow
# For now it's meant for cash game tables, might change to
# layer supertype pattern when tournaments come in later
from table import Table
from constants import MAX_PLAYERS, SMALL_BLIND, BIG_BLIND

class GameController:

    def __init__(self):
        self._table = Table(MAX_PLAYERS, (SMALL_BLIND, BIG_BLIND))
        self._players = []

     

