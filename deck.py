from constants import SUITES, RANKS
from card import Card
from random import shuffle

class Deck:

    cards = []
    currentCard = 0

    def __init__(self):
        for suite in SUITES:
            for rank in RANKS:
                self.cards.append(Card(suite, rank))


    def shuffleCards(self):
        self.currentCard = 0
        shuffle(self.cards)

    def deal(self):
         hands = [(self.cards[self.currentCard], self.cards[self.currentCard+1]), (self.cards[self.currentCard+2], self.cards[self.currentCard+3])]
         self.currentCard += 3
         return hands
