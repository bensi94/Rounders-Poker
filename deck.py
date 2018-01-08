from constants import SUITES, RANKS
from card import Card
from random import shuffle

class Deck:

    cards = []

    def __init__(self):
        for suite in SUITES:
            for rank in RANKS:
                self.cards.append(Card(suite, rank))

    def shuffleCards(self):
        shuffle(self.cards)
