from django.test import TestCase

from game_engine.hand import Hand
from game_engine.player import Player


class TestHand(TestCase):

    def test_pay_blinds(self):
        player1 = Player(100, 1)
        player2 = Player(200, 2)
        player3 = Player(300, 3)

        players = [player1, player2, player3]
        blinds = 10, 20

        hand = Hand(players, blinds)
        hand.pay_blinds()

        assert hand._players[0].stack == 100 - 10
        assert hand._players[0].bet == 10
        assert hand._players[1].stack == 200 - 20
        assert hand._players[1].bet == 20
        assert hand._players[2].stack == 300
        assert hand._players[2].bet == 0

    def test_pay_blinds_two_players(self):
        player1 = Player(100, 1)
        player2 = Player(200, 2)

        players = [player1, player2]
        blinds = 10, 20

        hand = Hand(players, blinds)
        hand.pay_blinds()

        assert hand._players[0].stack == 100 - 20
        assert hand._players[0].bet == 20
        assert hand._players[1].stack == 200 - 10
        assert hand._players[1].bet == 10
