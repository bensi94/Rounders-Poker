from deck import Deck

#Should generate 52 cards
def test_cards_total():
    deck = Deck()
    assert len(deck.cards) == 52

#First card should be ace of clubs
def test_first_card():
    deck = Deck()
    assert deck.cards[0].isCard() == 'ace of clubs'

#Last card should be king of spades
def test_last_card():
    deck = Deck()
    assert deck.cards[51].isCard() == 'king of spades'

#All cards should be unique
def test_all_cards_unique():
    seen = set()
    uniq = []
    deck = Deck()
    for card in deck.cards:
        if card.isCard() not in seen:
            uniq.append(card.isCard())
            seen.add(card.isCard())
    assert len(uniq) == 52

#Deal should return list of two card tuples, with unique cards,
def test_deal():
    deck = Deck()
    seen = set()
    deal = deck.deal()
    assert deal[0][0]._suite == "clubs" and deal[0][0]._rank == "ace"
    assert deal[1][1]._suite == "clubs" and deal[1][1]._rank == "4"
    assert deck.currentCard == 3
