# External
from collections import deque

# Internal
from GameEngine.constants import SUITES, RANKS
from GameEngine.card import Card
from random import shuffle


class Deck:

    def __init__(self):
        list_of_cards = []
        for suite in SUITES:
            for rank in RANKS:
                list_of_cards.append(Card(suite, rank))
        shuffle(list_of_cards)
        self._cards = deque(list_of_cards)

    def get_hand(self):
        return (self._cards.popleft(), self._cards.popleft())

    def get_flop(self):
        self._cards.popleft()  # Burn card (standard in texas hold'em poker)
        return (self._cards.popleft(),
                self._cards.popleft(),
                self._cards.popleft())

    # Used to get turn or river
    def get_next_card(self):
        self._cards.popleft()  # Burn card (standard in texas hold'em poker)
        return self._cards.popleft()
