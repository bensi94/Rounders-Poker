from django.test import TestCase

from game_engine.player import Player
from game_engine.card import Card
from game_engine.constants import STATUS_FOLDED


class TestPlayer(TestCase):

    SEAT_NUMBER = 1

    def test_give_hand(self):
        player = Player(100, self.SEAT_NUMBER)
        card1 = Card('hearts', '8')
        card2 = Card('spades', '9')

        hand = (card1, card2)
        player.give_hand(hand)

        assert player.hand[0].__str__() == '8 of hearts'
        assert player.hand[1].__str__() == '9 of spades'

    def test_bet_valid(self):
        player = Player(100, self.SEAT_NUMBER)

        retrun_val = player.bet_amount(50)

        assert player.stack == 50
        assert player.bet == 50
        assert retrun_val is True

    def test_bet_invalid(self):
        player = Player(100, self.SEAT_NUMBER)

        retrun_val = player.bet_amount(200)

        assert player.stack == 100
        assert player.bet == 0
        assert retrun_val is False

    def test_fold(self):
        player = Player(100, self.SEAT_NUMBER)

        player.bet_amount(50)
        player.fold()

        assert player.stack == 50
        assert player.status == STATUS_FOLDED

    def test_get_player_obj(self):
        stack = 100
        bet = 50

        player = Player(stack, self.SEAT_NUMBER)
        player.bet_amount(bet)

        state = player.get_player_obj()

        assert state['stack'] == stack-bet
        assert state['bet'] == bet

    def test_pay_blind_full(self):
        stack = 100
        blind = 20

        player = Player(stack, self.SEAT_NUMBER)
        player.pay_blind(blind)

        assert player.bet == blind
        assert player.stack == stack - blind

    # Test when blind is more than stack
    def test_pay_blind_less(self):
        stack = 10
        blind = 20

        player = Player(stack, self.SEAT_NUMBER)
        player.pay_blind(blind)

        assert player.bet == stack
        assert player.stack == 0

    def test_reset_bet(self):
        player1 = Player(100, self.SEAT_NUMBER)
        player1.bet_amount(20)
        player1.reset_bet()

        assert player1.bet == 0
