from card import Card

#Should generate rank of suite by input
def test_isCard():
    card = Card('clubs', 'ace')
    assert 'ace of clubs' == card.isCard()
