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
        return
        player1 = Player(100, 1)
        player2 = Player(200, 2)
        player1.status = const.STATUS_ACTIVE
        player2.status = const.STATUS_ACTIVE

        players = [player1, player2]
        blinds = 10, 20

        hand = Hand(players, blinds)

        hand.update_action_queue = Mock()

        action = {
            "type": const.BET,
            "amount": 50
        }

        hand.player_action(action)

    def test_player_action_last_call(self):
        """
        This test checks what functions are called after a
        player_action: LAST CALL in queue
        """
        pass
