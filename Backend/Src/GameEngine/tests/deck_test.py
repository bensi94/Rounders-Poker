from deck import Deck

#Should generate 52 cards
def test_cards_total():
    deck = Deck()
    assert len(deck._cards) == 52

#All cards should be unique
def test_all_cards_unique():
    seen = set()
    uniq = []
    deck = Deck()
    for card in deck._cards:
        if card.__str__() not in seen:
            uniq.append(card.__str__())
            seen.add(card.__str__())
    assert len(uniq) == 52


# Get hand should return two cards from the deck
# The length of the deck should be 50 after dealing two cards
def test_get_hand():
    deck = Deck()
    card1, card2 = deck.get_hand()
    assert card1.__str__() != card2.__str__()
    assert len(deck._cards) == 50


# Get flop in two player scenario
def test_get_flop():
    deck = Deck()
    deck.get_hand() # Hand for player 1, 52-2=50
    deck.get_hand() # Hand for player 2, 50-2=48

    card1, card2, card3 = deck.get_flop() # 48-4(flop+burn card) = 44
    assert card1.__str__() != card2.__str__() != card3.__str__()
    assert len(deck._cards) == 44


# Get turn in two player scenario
def test_get_next_card_turn():
    deck = Deck()
    deck.get_hand() # Hand for player 1, 52-2=50
    deck.get_hand() # Hand for player 2, 50-2=48
    deck.get_flop() # flop + burn card, 48-3-1 = 44
    deck.get_next_card()  # Turn + burn card, 44-1-1 = 42

    assert len(deck._cards) == 42

# Get river in two player scenario
def test_get_next_card_river():
    deck = Deck()
    deck.get_hand()  # Hand for player 1, 52-2=50
    deck.get_hand()  # Hand for player 2, 50-2=48
    deck.get_flop()  # flop + burn card, 48-3-1 = 44
    deck.get_next_card()  # Turn + burn card, 44-1-1 = 42
    deck.get_next_card()  # River + burn card, 42-1-1 = 40
    assert len(deck._cards) == 40

