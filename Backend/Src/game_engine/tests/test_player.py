from django.test import TestCase

from game_engine.player import Player
from game_engine import constants as const


class TestPlayer(TestCase):

    SEAT_NUMBER = 1

    def test_give_hand(self):
        player = Player(100, self.SEAT_NUMBER)
        card1 = '8h'
        card2 = '9s'

        hand = (card1, card2)
        player.give_hand(hand)

        assert player.cards[0] == '8h'
        assert player.cards[1] == '9s'

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
        assert player.status == const.STATUS_FOLDED

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
        player.pay_blind(blind, const.POST_BB)

        assert player.bet == blind
        assert player.stack == stack - blind

    # Test when blind is more than stack
    def test_pay_blind_less(self):
        stack = 10
        blind = 20

        player = Player(stack, self.SEAT_NUMBER)
        player.pay_blind(blind, const.POST_BB)

        assert player.bet == stack
        assert player.stack == 0

    def test_reset_bet(self):
        player1 = Player(100, self.SEAT_NUMBER)
        player1.bet_amount(20)
        player1.reset_bet()

        assert player1.bet == 0

    def test_get_possible_actions_01(self):
        """Hero is the big blind and it's called to him"""
        hero = Player(100, self.SEAT_NUMBER)

        hero.bet_amount(20)

        actions = [
            {
                "type": const.CHECK
            },
            {
                "type": const.RAISE,
                "min": 40,
                "max": 100
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(20, 0, 20))

    def test_get_possible_actions_02(self):
        """
        Hero is the third to do after, bet of 20 and min raise to 40.
        Checks that min raise size is correct
        """

        hero = Player(100, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CALL,
                "amount": 40
            },
            {
                "type": const.RAISE,
                "min": 60,
                "max": 100
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(40, 20, 20))

    def test_get_possible_actions_03(self):
        """Hero has bet 20, next player went all in for 39. Hero can only call or fold"""

        hero = Player(100, self.SEAT_NUMBER)
        hero.bet_amount(20)

        actions = [
            {
                "type": const.CALL,
                "amount": 39
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(39, 20, 20))

    def test_get_possible_actions_04(self):
        """All players are all in, with max as 60. Hero can only call or fold"""

        hero = Player(100, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CALL,
                "amount": 60
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(60, 20, 20, True))

    def test_get_possible_actions_05(self):
        """Bet is more than hero has for stack. Hero can only call or fold"""

        hero = Player(20, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CALL,
                "amount": 20
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(80, 40, 20))

    def test_get_possible_actions_06(self):
        """Post flop action has been checked to hero. Hero can, check, bet or fold"""

        hero = Player(100, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CHECK
            },
            {
                "type": const.BET,
                "min": 20,
                "max": 100
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(0, 0, 20))

    def test_get_possible_actions_07(self):
        """Post flop hero has less then one bb and can only bet all in, check or fold."""

        hero = Player(13, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CHECK
            },
            {
                "type": const.BET,
                "min": 13,
                "max": 13
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(0, 0, 20))

    def test_get_possible_actions_08(self):
        """Hero is next to act after Big Blind and can call, raise and fold"""

        hero = Player(100, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CALL,
                "amount": 20
            },
            {
                "type": const.RAISE,
                "min": 40,
                "max": 100
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(20, 0, 20))

    def test_get_possible_actions_09(self):
        """Hero is small blind"""

        hero = Player(100, self.SEAT_NUMBER)

        hero.pay_blind(10, const.POST_SB)

        actions = [
            {
                "type": const.CALL,
                "amount": 20
            },
            {
                "type": const.RAISE,
                "min": 40,
                "max": 100
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(20, 0, 20))

    def test_get_possible_actions_10(self):
        """Hero is small blind with small stack"""

        hero = Player(18, self.SEAT_NUMBER)

        hero.pay_blind(10, const.POST_SB)

        actions = [
            {
                "type": const.CALL,
                "amount": 18
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(20, 0, 20))

    def test_get_possible_actions_11(self):
        """Hero is last to do after raise of 100 and then all_in"""

        hero = Player(800, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CALL,
                "amount": 375
            },
            {
                "type": const.RAISE,
                "min": 475,
                "max": 800
            },
            {
                "type": const.FOLD,
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(375, 100, 20))

    def test_get_possible_actions_12(self):
        """Hero is doing after a big blind with small stack"""

        hero = Player(800, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CALL,
                "amount": 20
            },
            {
                "type": const.RAISE,
                "min": 40,
                "max": 800,
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(15, 0, 20))

    def test_get_possible_actions_13(self):
        """Hero is next to do preflop after an all in from the UTG player"""

        hero = Player(800, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CALL,
                "amount": 34
            },
            {
                "type": const.RAISE,
                "min": 40,
                "max": 800
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(34, 20, 20))

    def test_get_possible_actions_14(self):
        """Hero is next to do and can only call or fold because of stack size"""

        hero = Player(100, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CALL,
                "amount": 100,
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(200, 0, 20))

    def test_get_possible_actions_15(self):
        """Hero is small blind on the button in a heads up setting"""

        hero = Player(100, self.SEAT_NUMBER)
        hero.pay_blind(10, const.POST_SB)

        actions = [
            {
                "type": const.CALL,
                "amount": 20
            },
            {
                "type": const.RAISE,
                "min": 40,
                "max": 100
            },
            {
                "type": const.FOLD
            }
        ]

        self.assertEqual(actions, hero.get_possible_actions(20, 0, 20))

    def test_validate_action_valid(self):
        """Simple test that test the validate action function. With valid action"""

        hero = Player(100, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CALL,
                "amount": 20
            },
            {
                "type": const.FOLD
            }
        ]

        hero.possible_actions = actions

        hero.validate_action({
            "type": const.CALL,
            "amount": 20
        })

        # Don't need to assert anything, because nothing should happen

    def test_validate_action_invalid(self):
        """Simple test that test the validate action function. With invalid action"""

        hero = Player(800, self.SEAT_NUMBER)

        actions = [
            {
                "type": const.CALL,
                "amount": 375
            },
            {
                "type": const.RAISE,
                "min": 475,
                "max": 800
            },
            {
                "type": const.FOLD,
            }
        ]

        hero.possible_actions = actions

        with self.assertRaises(ValueError) as error:
            hero.validate_action({
                "type": const.RAISE,
                "amount": 200
            })

            self.assertEqual('Action failed: Invalid Amount', str(error.exception))

    def test_action(self):
        hero = Player(800, self.SEAT_NUMBER)
        hero.status = const.STATUS_ACTIVE

        action = {
            "type": const.BET,
            "amount": 50
        }

        hero.action(action)

        self.assertEqual(const.BET, hero.last_action)
        self.assertEqual(const.STATUS_ACTIVE, hero.status)
        self.assertEqual(750, hero.stack)
        self.assertEqual(50, hero.bet)
