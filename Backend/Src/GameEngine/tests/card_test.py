from GameEngine.card import Card


# Should generate rank of suite by input
def test__str__():
    card = Card('clubs', 'ace')
    assert 'ace of clubs' == card.__str__()
