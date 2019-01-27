#External 
from collections import deque
import itertools
import random

#Internal
from constants import SUITES, RANKS
from card import Card
from random import shuffle


class Deck:

    def __init__(self):
        list_of_cards = []
        for suite in SUITES:
            for rank in RANKS:
                list_of_cards.append(Card(suite, rank))
        shuffle(list_of_cards)
        self.cards = deque(list_of_cards)

    def get_hand(self):
        return (self.cards.popleft(), self.cards.popleft())

    def get_flop(self):
        self.cards.popleft() # Burn card (standard in texas hold'em poker)
        return (self.cards.popleft(), self.cards.popleft(), self.cards.popleft())

    # Used to get turn or river
    def get_next_card(self):
        self.cards.popleft()  # Burn card (standard in texas hold'em poker)
        return self.cards.popleft()