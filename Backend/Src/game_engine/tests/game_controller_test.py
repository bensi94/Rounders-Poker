from game_engine.game_controller import GameController
from django.test import TestCase
from unittest import mock

from game_engine import constants as const
from core.models.table import Table


class TestGameController(TestCase):

    def setUp(self):
        self.table = Table.objects.create(
            name='Table1',
            small_blind=10,
            big_blind=20,
        )
        self.controller = GameController(self.table.id)
        self.controller.broadcast_state = mock.Mock()

    def random_mock(self, input):
        return input[0]

    def test_setup_table_two_active(self):
        """Tests setting up a table when a new player has sat down and they're waiting"""

        # SETUP
        self.controller.add_player.__wrapped__(self.controller, 'bensi94', 500, 1, 1)
        self.controller.add_player.__wrapped__(self.controller, 'bensi', 100, 2, 2)

        with mock.patch('random.choice', self.random_mock):
            # EXECUTION
            self.controller.setup_table.__wrapped__(self.controller)

            # ASSERTS
            self.assertEqual(self.controller._game_state, {
                "stage": const.PREFLOP,
                "dealer_seat": 1,
                "sb_seat": 1,
                "bb_seat": 2,
                "small_blind": 10,
                "big_blind": 20,
                "community_cards": [],
                "pot": 0,
                "action_on_seat": 1
            })

            self.assertEqual(self.controller._players['bensi94']['player'].get_player_obj(), {
                "user": "bensi94",
                "seatnumber": 1,
                "status": const.STATUS_ACTIVE,
                "last_action": "",
                "stack": 500,
                "bet": 0
            })

            self.assertEqual(self.controller._players['bensi']['player'].get_player_obj(), {
                "user": "bensi",
                "seatnumber": 2,
                "status": const.STATUS_ACTIVE,
                "last_action": "",
                "stack": 100,
                "bet": 0
            })

            self.table = Table.objects.get(pk=self.table.id)

            self.assertEqual(self.table.dealer_seat, 1)
            self.assertEqual(self.table.sb_seat, 1)
            self.assertEqual(self.table.bb_seat, 2)
            self.assertEqual(self.table.status, Table.ACTIVE)

    def test_setup_table_running_four(self):
        """Tests setting up a table with four playing players"""

        self.table.dealer_seat = 4
        self.table.sb_seat = 5
        self.table.bb_seat = 6
        self.table.save()

        # SETUP
        self.controller.add_player.__wrapped__(self.controller, 'player_1', 500, 2, 1)
        self.controller.add_player.__wrapped__(self.controller, 'player_2', 100, 3, 2)
        self.controller.add_player.__wrapped__(self.controller, 'player_3', 200, 5, 3)
        self.controller.add_player.__wrapped__(self.controller, 'player_4', 300, 7, 4)

        # EXECUTION
        self.controller.setup_table.__wrapped__(self.controller)

        # ASSERTS
        self.assertEqual(self.controller._game_state, {
            "stage": const.PREFLOP,
            "dealer_seat": 5,
            "sb_seat": 7,
            "bb_seat": 2,
            "small_blind": 10,
            "big_blind": 20,
            "community_cards": [],
            "pot": 0,
            "action_on_seat": 3
        })

        self.assertEqual(self.controller._players['player_1']['player'].get_player_obj(), {
            "user": "player_1",
            "seatnumber": 2,
            "status": const.STATUS_ACTIVE,
            "last_action": "",
            "stack": 500,
            "bet": 0
        })

        self.assertEqual(self.controller._players['player_2']['player'].get_player_obj(), {
            "user": "player_2",
            "seatnumber": 3,
            "status": const.STATUS_ACTIVE,
            "last_action": "",
            "stack": 100,
            "bet": 0
        })

        self.assertEqual(self.controller._players['player_3']['player'].get_player_obj(), {
            "user": "player_3",
            "seatnumber": 5,
            "status": const.STATUS_ACTIVE,
            "last_action": "",
            "stack": 200,
            "bet": 0
        })

        self.assertEqual(self.controller._players['player_4']['player'].get_player_obj(), {
            "user": "player_4",
            "seatnumber": 7,
            "status": const.STATUS_ACTIVE,
            "last_action": "",
            "stack": 300,
            "bet": 0
        })

        self.table = Table.objects.get(pk=self.table.id)

        self.assertEqual(self.table.dealer_seat, 5)
        self.assertEqual(self.table.sb_seat, 7)
        self.assertEqual(self.table.bb_seat, 2)
        self.assertEqual(self.table.status, Table.ACTIVE)

    def test_setup_table_running_three(self):
        """Tests setting up a table with four playing players"""

        self.table.dealer_seat = 8
        self.table.sb_seat = 9
        self.table.bb_seat = 2
        self.table.save()

        # SETUP
        self.controller.add_player.__wrapped__(self.controller, 'player_1', 500, 2, 1)
        self.controller.add_player.__wrapped__(self.controller, 'player_2', 100, 4, 2)
        self.controller.add_player.__wrapped__(self.controller, 'player_3', 200, 6, 3)

        # EXECUTION
        self.controller.setup_table.__wrapped__(self.controller)

        # ASSERTS
        self.assertEqual(self.controller._game_state, {
            "stage": const.PREFLOP,
            "dealer_seat": 2,
            "sb_seat": 4,
            "bb_seat": 6,
            "small_blind": 10,
            "big_blind": 20,
            "community_cards": [],
            "pot": 0,
            "action_on_seat": 2
        })

        self.assertEqual(self.controller._players['player_1']['player'].get_player_obj(), {
            "user": "player_1",
            "seatnumber": 2,
            "status": const.STATUS_ACTIVE,
            "last_action": "",
            "stack": 500,
            "bet": 0
        })

        self.assertEqual(self.controller._players['player_2']['player'].get_player_obj(), {
            "user": "player_2",
            "seatnumber": 4,
            "status": const.STATUS_ACTIVE,
            "last_action": "",
            "stack": 100,
            "bet": 0
        })

        self.assertEqual(self.controller._players['player_3']['player'].get_player_obj(), {
            "user": "player_3",
            "seatnumber": 6,
            "status": const.STATUS_ACTIVE,
            "last_action": "",
            "stack": 200,
            "bet": 0
        })

        self.table = Table.objects.get(pk=self.table.id)

        self.assertEqual(self.table.dealer_seat, 2)
        self.assertEqual(self.table.sb_seat, 4)
        self.assertEqual(self.table.bb_seat, 6)
        self.assertEqual(self.table.status, Table.ACTIVE)

    def test_add_player(self):
        self.controller.add_player.__wrapped__(self.controller, 'Bensi', 100, 1, 1)
        self.assertIn('Bensi',  self.controller._players)
        self.assertEqual(self.controller._players['Bensi']['player'].stack, 100)

    def test_add_observer(self):
        self.controller.add_observer.__wrapped__(self.controller, 'Bensi', 1)
        self.assertIn('Bensi',  self.controller._observers)
