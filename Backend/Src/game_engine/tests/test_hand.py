from django.test import TestCase

from game_engine.hand import Hand
from game_engine.player import Player


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

    def test_init_two_players(self):
        """In init both pay_blinds and deal_hand are called so we test them by doing this test"""
        player1 = Player(100, 1)
        player2 = Player(200, 2)

        players = [player1, player2]
        blinds = 10, 20

        hand = Hand(players, blinds)

        self.assertCards(hand)
        # Pay blinds is called in the constructor so we don't actually call it in the test
        self.assertEqual(hand._players[0].stack, 100 - 20)
        self.assertEqual(hand._players[0].bet, 20)
        self.assertEqual(hand._players[1].stack, 200 - 10)
        self.assertEqual(hand._players[1].bet, 10)
