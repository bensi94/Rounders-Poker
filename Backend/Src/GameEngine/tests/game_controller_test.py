from GameEngine.game_controller import GameController
from django.test import TestCase


class TestGameController(TestCase):

    def setUp(self):
        self.controller = GameController('table_1')

    def test_get_button_ordered_players(self):
        self.controller._players[5] = 'Bensi'
        self.controller._players[3] = 'Iza'
        self.controller._players[7] = 'Eythor'
        self.controller._players[2] = 'Sveinn'

        # Check all buttons for these players, works like multiple tests in one
        self.controller._table._button = 7
        assert self.controller.get_button_ordered_players() == \
            ['Sveinn', 'Iza', 'Bensi', 'Eythor']
        self.controller._table._button = 5
        assert self.controller.get_button_ordered_players() == \
            ['Eythor', 'Sveinn', 'Iza', 'Bensi']
        self.controller._table._button = 3
        assert self.controller.get_button_ordered_players() == \
            ['Bensi', 'Eythor', 'Sveinn', 'Iza']
        self.controller._table._button = 2
        assert self.controller.get_button_ordered_players() == \
            ['Iza', 'Bensi', 'Eythor', 'Sveinn']

    def test_get_button_ordered_players_two(self):
        """Tests for two players"""
        self.controller._players[5] = 'Bensi'
        self.controller._players[3] = 'Iza'

        self.controller._table._button = 5
        assert self.controller.get_button_ordered_players() == ['Iza', 'Bensi']
        self.controller._table._button = 3
        assert self.controller.get_button_ordered_players() == ['Bensi', 'Iza']

    def test_add_player(self):
        self.controller.add_player.__wrapped__(self.controller, 'Bensi', 100)
        assert 'Bensi' in self.controller._players
        assert self.controller._players['Bensi']._stack == 100
