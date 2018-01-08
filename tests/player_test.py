from player import Player


def test_player_name():
    player = Player('Benedikt')
    assert 'Benedikt' == player._name
