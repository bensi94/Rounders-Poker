from game_controller import GameController

def test_get_button_ordered_players():
    controller = GameController()
    controller._players[5] = 'Bensi'
    controller._players[3] = 'Iza'
    controller._players[7] = 'Eythor'
    controller._players[2] = 'Sveinn'

    # Check all buttons for these players, works like multiple tests in one
    controller._table._button = 7
    assert controller.get_button_ordered_players() == ['Sveinn', 'Iza', 'Bensi', 'Eythor']
    controller._table._button = 5
    assert controller.get_button_ordered_players() == ['Eythor', 'Sveinn', 'Iza', 'Bensi']
    controller._table._button = 3
    assert controller.get_button_ordered_players() == ['Bensi', 'Eythor', 'Sveinn', 'Iza']
    controller._table._button = 2
    assert controller.get_button_ordered_players() == ['Iza', 'Bensi', 'Eythor', 'Sveinn']

# Tests for two players
def test_get_button_ordered_players_two():
    controller = GameController()
    controller._players[5] = 'Bensi'
    controller._players[3] = 'Iza'

    controller._table._button = 5
    assert controller.get_button_ordered_players() == ['Iza', 'Bensi']
    controller._table._button = 3
    assert controller.get_button_ordered_players() == ['Bensi', 'Iza']

