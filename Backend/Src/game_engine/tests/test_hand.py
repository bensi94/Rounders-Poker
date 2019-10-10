from django.test import TestCase
from collections import deque
from unittest.mock import Mock

from game_engine.hand import Hand
from game_engine.player import Player
from game_engine import constants as const


class TestHand(TestCase):

    def assertCards(self, hand):
        all_cards = []

        for player in hand._players:
            card1, card2 = player.cards
            self.assertNotIn(card1, all_cards)
            self.assertNotIn(card2, all_cards)
            all_cards.append(card1)
            all_cards.append(card2)

        self.assertEqual(len(all_cards), len(set(all_cards)))

    def test_init_three_players(self):
        """In init both pay_blinds and deal_hand are called so we test them by doing this test"""
        player1 = Player(100, 1)
        player2 = Player(200, 2)
        player3 = Player(300, 3)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE
        player3.status = const.STATUS_ACTIVE

        players = [player1, player2, player3]
        blinds = 10, 20

        hand = Hand(players, blinds)

        self.assertCards(hand)
        # Pay blinds is called in the constructor so we don't actually call it in the test
        self.assertEqual(hand._players[0].stack, 100 - 10)
        self.assertEqual(hand._players[0].bet, 10)
        self.assertEqual(hand._players[1].stack, 200 - 20)
        self.assertEqual(hand._players[1].bet, 20)
        self.assertEqual(hand._players[2].stack, 300)
        self.assertEqual(hand._players[2].bet, 0)
        self.assertEqual(deque([player3, player1, player2]), hand.action_queue)

    def test_init_two_players(self):
        """In init both pay_blinds and deal_hand are called so we test them by doing this test"""
        player1 = Player(100, 1)
        player2 = Player(200, 2)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE

        players = [player1, player2]
        blinds = 10, 20

        hand = Hand(players, blinds)

        self.assertCards(hand)
        # Pay blinds is called in the constructor so we don't actually call it in the test
        self.assertEqual(hand._players[0].stack, 100 - 20)
        self.assertEqual(hand._players[0].bet, 20)
        self.assertEqual(hand._players[1].stack, 200 - 10)
        self.assertEqual(hand._players[1].bet, 10)
        self.assertEqual(deque([player2, player1]), hand.action_queue)

    def test_fill_action_queue(self):
        """
        This tests the fill_action_queue method that is used
        on the flop, turn and river to add all active players
        """
        # Setup
        player1 = Player(100, 1)
        player2 = Player(200, 2)
        player3 = Player(300, 3)
        player4 = Player(400, 4)

        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE
        player3.status = const.STATUS_FOLDED
        player4.status = const.STATUS_ACTIVE

        players = [player1, player2, player3, player4]

        hand = Hand(players, (10, 20))
        hand.action_queue = deque()

        # Execution
        hand.fill_action_queue()

        # Asserts
        self.assertEqual(deque([player1, player2, player4]), hand.action_queue)

    def test_update_action_queue(self):
        """
        This tests the update action_queue method that is calls everytime somone bets or raises

        OUR TEST CASE:
        6 players,
        action_queue before raise: [player6]
        player1: bet 20
        player2: called 20
        player3: has folded
        player4: is waiting
        player5: has raised to 50 (method would be called after this raise)
        player6: action on
        action_queue after raise: [player6, player1, player2]
        """

        # Setup
        player1 = Player(100, 1)
        player2 = Player(200, 2)
        player3 = Player(300, 3)
        player4 = Player(400, 4)
        player5 = Player(500, 5)
        player6 = Player(600, 6)

        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE
        player3.status = const.STATUS_FOLDED
        player4.status = const.STATUS_WAITING
        player5.status = const.STATUS_ACTIVE
        player6.status = const.STATUS_ACTIVE

        players = [player1, player2, player3, player4, player5, player6]

        hand = Hand(players, (10, 20))
        hand.action_queue = deque([player6])
        hand.update_action_queue(player5)

        self.assertEqual(deque([player6, player1, player2]), hand.action_queue)

    def test_player_action_bet(self):
        """
        This test checks what functions are called after a player a player_action: BET
        """
        player1 = Player(100, 1)
        player2 = Player(200, 2)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE

        players = [player1, player2]
        blinds = 10, 20

        hand = Hand(players, blinds)

        hand.update_action_queue = Mock()

        player1.get_possible_actions(0, 0, 20)

        action = {
            "type": const.BET,
            "amount": 50
        }

        hand.player_action(action, player1)
        hand.update_action_queue.assert_called_once()

    def test_player_action_correct_updates01(self):
        """This case happens when a player is first to raise the big blind"""

        player1 = Player(100, 1)
        player2 = Player(200, 2)
        player3 = Player(300, 3)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE
        player3.status = const.STATUS_ACTIVE

        players = [player1, player2, player3]
        blinds = 10, 20

        hand = Hand(players, blinds)
        hand.update_action_queue = Mock()

        player3.get_possible_actions(20, 0, 20)

        action = {
            "type": const.RAISE,
            "amount": 50
        }

        hand.player_action(action, player3)

        self.assertEqual(hand._current_max_bet, 50)
        self.assertEqual(hand.last_legal_raise, 30)
        self.assertEqual(hand._pot, 80)
        hand.update_action_queue.assert_called_once()

    def test_player_action_correct_updates02(self):
        """Player goes all in for less than 2 big blinds UTG"""

        player1 = Player(100, 1)
        player2 = Player(200, 2)
        player3 = Player(34, 3)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE
        player3.status = const.STATUS_ACTIVE

        players = [player1, player2, player3]
        blinds = 10, 20

        hand = Hand(players, blinds)
        hand.update_action_queue = Mock()

        player3.get_possible_actions(20, 0, 20)

        action = {
            "type": const.RAISE,
            "amount": 34
        }

        hand.player_action(action, player3)

        self.assertEqual(hand._current_max_bet, 34)
        self.assertEqual(hand.last_legal_raise, 20)
        self.assertEqual(hand._pot, 64)
        hand.update_action_queue.assert_called_once()

    def test_player_action_correct_updates03(self):
        """Big blind player re raises a raise heads up"""

        player1 = Player(200, 1)
        player2 = Player(200, 2)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE

        players = [player1, player2]
        blinds = 10, 20

        hand = Hand(players, blinds)
        hand.update_action_queue = Mock()

        player2.get_possible_actions(hand._current_max_bet, hand.last_legal_raise, hand._big_blind)

        hand.player_action({
            "type": const.RAISE,
            "amount": 60
        }, player2)

        self.assertEqual(hand._current_max_bet, 60)
        self.assertEqual(hand.last_legal_raise, 40)
        self.assertEqual(hand._pot, 80)
        hand.update_action_queue.assert_called_once()

        player1.get_possible_actions(hand._current_max_bet, hand.last_legal_raise, hand._big_blind)

        hand.player_action({
            "type": const.RAISE,
            "amount": 120
        }, player1)

        self.assertEqual(hand._current_max_bet, 120)
        self.assertEqual(hand.last_legal_raise, 60)
        self.assertEqual(hand._pot, 180)
        self.assertEqual(hand.update_action_queue.call_count, 2)

    def test_player_action_correct_updates04(self):
        """
        Action is post flop and goes like this:
            Player 1: BET 40
            Player 2: CALL 40
            Player 3: RAISE 100
            Player 4: FOLD
            Player 5: RE-RAISE ALL-IN 150
        Pot starts as 30 (SB + BB) in the example, for simplicity, would be more in full example
        """

        player1 = Player(200, 1)
        player2 = Player(200, 2)
        player3 = Player(300, 3)
        player4 = Player(400, 4)
        player5 = Player(150, 5)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE
        player3.status = const.STATUS_ACTIVE
        player4.status = const.STATUS_ACTIVE
        player5.status = const.STATUS_ACTIVE

        players = [player1, player2, player3, player4, player5]
        blinds = 10, 20

        hand = Hand(players, blinds)
        hand.update_action_queue = Mock()

        player1.reset_bet()
        player2.reset_bet()
        hand._current_max_bet = 0

        player1.get_possible_actions(hand._current_max_bet, hand.last_legal_raise, hand._big_blind)

        hand.player_action({
            "type": const.BET,
            "amount": 40
        }, player1)

        self.assertEqual(hand._current_max_bet, 40)
        self.assertEqual(hand.last_legal_raise, 0)
        self.assertEqual(hand._pot, 70)  # Would be more in full round
        self.assertEqual(hand.update_action_queue.call_count, 1)

        player2.get_possible_actions(hand._current_max_bet, hand.last_legal_raise, hand._big_blind)

        hand.player_action({
            "type": const.CALL,
            "amount": 40
        }, player2)

        self.assertEqual(hand._current_max_bet, 40)
        self.assertEqual(hand.last_legal_raise, 0)
        self.assertEqual(hand._pot, 110)
        self.assertEqual(hand.update_action_queue.call_count, 1)

        player3.get_possible_actions(hand._current_max_bet, hand.last_legal_raise, hand._big_blind)

        hand.player_action({
            "type": const.RAISE,
            "amount": 100
        }, player3)

        self.assertEqual(hand._current_max_bet, 100)
        self.assertEqual(hand.last_legal_raise, 60)
        self.assertEqual(hand._pot, 210)
        self.assertEqual(hand.update_action_queue.call_count, 2)

        player4.get_possible_actions(hand._current_max_bet, hand.last_legal_raise, hand._big_blind)

        hand.player_action({
            "type": const.FOLD,
        }, player4)

        self.assertEqual(hand._current_max_bet, 100)
        self.assertEqual(hand.last_legal_raise, 60)
        self.assertEqual(hand._pot, 210)
        self.assertEqual(hand.update_action_queue.call_count, 2)

        player5.get_possible_actions(hand._current_max_bet, hand.last_legal_raise, hand._big_blind)

        hand.player_action({
            "type": const.RAISE,
            "amount": 150
        }, player5)

        self.assertEqual(hand._current_max_bet, 150)
        self.assertEqual(hand.last_legal_raise, 60)
        self.assertEqual(hand._pot, 360)
        self.assertEqual(hand.update_action_queue.call_count, 3)

    def test_update_table01(self):
        """This test happens at the beginning of a hand after it's been dealt"""
        player1 = Player(200, 1)
        player2 = Player(200, 2)
        player3 = Player(300, 3)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE
        player3.status = const.STATUS_ACTIVE

        players = [player1, player2, player3]
        blinds = 10, 20

        hand = Hand(players, blinds)

        response = hand.update_table()

        self.assertEqual(response, {
            "response": const.PLAYER_ACTION,
            "player": player3
        })
        self.assertEqual(hand.action_on_player, player3)
        self.assertEqual(len(hand.action_queue), 2)
        self.assertEqual(hand._board, [])
        self.assertEqual(hand.stage, const.PREFLOP)

    def test_update_table02(self):
        """Should be testing that it proceed to next stage on empty action queue"""

        player1 = Player(200, 1)
        player2 = Player(200, 2)
        player3 = Player(300, 3)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE
        player3.status = const.STATUS_ACTIVE

        players = [player1, player2, player3]
        blinds = 10, 20

        hand = Hand(players, blinds)

        hand.action_queue = deque()
        response = hand.update_table()

        self.assertEqual(hand.action_on_player, player1)
        self.assertEqual(len(hand.action_queue), 2)
        self.assertEqual(len(hand._board), 3)
        self.assertEqual(response, {
            "response": const.PLAYER_ACTION,
            "player": player1
        })
        self.assertEqual(hand.stage, const.FLOP)

    def test_update_table03(self):
        """Should be ending hand if there is only one player active and he's not in the queue"""

        player1 = Player(200, 1)
        player2 = Player(200, 2)
        player3 = Player(300, 3)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_FOLDED
        player3.status = const.STATUS_FOLDED

        players = [player1, player2, player3]
        blinds = 10, 20

        hand = Hand(players, blinds)

        hand.action_queue = deque()
        response = hand.update_table()

        self.assertEqual(len(hand.action_queue), 0)
        self.assertEqual(hand._board, [])
        self.assertEqual(response, {
            "response": const.END_HAND
        })
        self.assertEqual(hand.stage, const.PREFLOP)
