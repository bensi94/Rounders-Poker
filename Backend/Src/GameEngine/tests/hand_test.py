from GameEngine.hand import Hand
from GameEngine.player import Player


def test_pay_blinds():
    player1 = Player(100)
    player2 = Player(200)
    player3 = Player(300)

    players = [player1, player2, player3]
    blinds = 10, 20

    hand = Hand(players, blinds)
    hand.pay_blinds()

    assert hand._players[0]._stack == 100 - 10
    assert hand._players[0]._bet == 10
    assert hand._players[1]._stack == 200 - 20
    assert hand._players[1]._bet == 20
    assert hand._players[2]._stack == 300
    assert hand._players[2]._bet == 0


def test_pay_blinds_two_players():
    player1 = Player(100)
    player2 = Player(200)

    players = [player1, player2]
    blinds = 10, 20

    hand = Hand(players, blinds)
    hand.pay_blinds()

    assert hand._players[0]._stack == 100 - 20
    assert hand._players[0]._bet == 20
    assert hand._players[1]._stack == 200 - 10
    assert hand._players[1]._bet == 10
