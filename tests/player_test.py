from player import Player


#Player should get name and starting stack
def test_init():
    player = Player('Benedikt', 10000, True)
    assert 'Benedikt' == player._name
    assert 10000 == player._stack
    assert True == player._isDealer

#Player is not dealer
def test_isNotDealer():
    player = Player('Benedikt', 10000, False)
    assert False == player._isDealer

#Player should pay blind and return amount paid
def test_payBlind():
    player = Player('Benedikt', 10000, False)
    amountPaid = player.payBlind(20)
    assert player._stack == 9980
    assert amountPaid == 20


#Player should only pay what they have in stack
def test_payBlind():
    player = Player('Benedikt', 10000, False)
    amountPaid = player.payBlind(20000)
    assert player._stack == 0
    assert amountPaid == 10000
