from game_engine.game_controller import GameController
from django.test import TestCase
from unittest.mock import Mock

from core.models.table import Table


class TestGameController(TestCase):

    def setUp(self):
        table = Table.objects.create(
            name='Table1',
            small_blind=10,
            big_blind=20,
        )
        self.controller = GameController(table.id)
        self.controller.broadcast_state = Mock()

    # def test_setup_table(self):
    #     self.controller._players = {
    #         'Bensi': {
    #             'seatnumber': 1,

    #         }
    #     }

    # def test_get_button_ordered_players(self):
    #     self.controller._players[5] = 'Bensi'
    #     self.controller._players[3] = 'Iza'
    #     self.controller._players[7] = 'Eythor'
    #     self.controller._players[2] = 'Sveinn'

    #     # Check all buttons for these players, works like multiple tests in one
    #     self.controller._table._button = 7
    #     assert self.controller.get_button_ordered_players() == \
    #         ['Sveinn', 'Iza', 'Bensi', 'Eythor']
    #     self.controller._table._button = 5
    #     assert self.controller.get_button_ordered_players() == \
    #         ['Eythor', 'Sveinn', 'Iza', 'Bensi']
    #     self.controller._table._button = 3
    #     assert self.controller.get_button_ordered_players() == \
    #         ['Bensi', 'Eythor', 'Sveinn', 'Iza']
    #     self.controller._table._button = 2
    #     assert self.controller.get_button_ordered_players() == \
    #         ['Iza', 'Bensi', 'Eythor', 'Sveinn']

    # def test_get_button_ordered_players_two(self):
    #     """Tests for two players"""
    #     self.controller._players[5] = 'Bensi'
    #     self.controller._players[3] = 'Iza'

    #     self.controller._table._button = 5
    #     assert self.controller.get_button_ordered_players() == ['Iza', 'Bensi']
    #     self.controller._table._button = 3
    #     assert self.controller.get_button_ordered_players() == ['Bensi', 'Iza']

    def test_add_player(self):
        self.controller.add_player.__wrapped__(self.controller, 'Bensi', 100, 1, 1)
        assert 'Bensi' in self.controller._players
        assert self.controller._players['Bensi']['player']._stack == 100

    def test_add_observer(self):
        self.controller.add_observer.__wrapped__(self.controller, 'Bensi', 1)
        assert 'Bensi' in self.controller._observers
