from table import Table
import pytest

# Tests that table is made with two empty seats
# Also test that blind init 
def test_init_two_players():
    # Blinds are set to 10 and 20
    table = Table(2, (10,20))
    
    assert table._small_blind == 10
    assert table._big_blind == 20
    assert len(table._seats) == 2
    assert table._seats[1] == None
    assert table._seats[2] == None

# Player should be able to sit in empty seat
def test_sit_at_table_empty_seat():
    table = Table(2, (10,20))

    # MOCK PLAYER - will be player object
    player = 'MOCK PLAYER'
    seat = 1
    return_msg = table.sit_at_table(player, seat)

    assert table._seats[seat] == 'MOCK PLAYER'
    assert 'Player seated at seat: ' + str(seat) == return_msg

# Player should not be able to sit in occupied seat
def test_sit_at_table_occupied():
    table = Table(2, (10, 20))

    # MOCK PLAYERS - will be player objects
    player_1 = 'MOCK PLAYER 1'
    player_2 = 'MOCK PLAYER 2'
    seat = 1
    table.sit_at_table(player_1, seat)
    return_msg = table.sit_at_table(player_2, seat)

    assert table._seats[seat] != player_2
    assert 'Seat occupied, player not seated' == return_msg

# Player should not be able to sit at seat that does not exist  
def test_sit_at_table_not_exist():
    table = Table(2, (10, 20))

    # MOCK PLAYER - will be player object
    player = 'MOCK PLAYER'
    seat = 5 # Random number that does not exist
    return_msg = table.sit_at_table(player, seat)
    
    # Checks if player is seated at seat 5 (should be KeyError)
    with pytest.raises(KeyError):
        assert table._seats[seat] != player
    assert return_msg == 'Invalid seat, player not seated'

# If one player sits down the game should be pending
def test_sit_at_table_pending():
    table = Table(2, (10, 20))

    # MOCK PLAYER - will be player object
    player = 'MOCK PLAYER'
    seat = 1
    table.sit_at_table(player, seat)

    assert table._state == 'PENDING'


# If one player sits down the game should be running
def test_sit_at_table_running():
    table = Table(2, (10, 20))

    # MOCK PLAYER - will be player object
    player1 = 'MOCK PLAYER 1'
    player2 = 'MOCK PLAYER 2'

    table.sit_at_table(player1, 1)
    table.sit_at_table(player2, 2)

    assert table._state == 'RUNNING'
    assert table._button == 1 or table._button == 2


def test_empty_seat():
    table = Table(2, (10, 20))

    # MOCK PLAYER - will be player object
    player1 = 'MOCK PLAYER 1'
    player2 = 'MOCK PLAYER 2'

    table.sit_at_table(player1, 1)
    table.sit_at_table(player2, 2)

    table.empty_seat(1)
    assert table._state == 'PENDING'
    assert table._seats[1] == None

def test_move_button():
    table = Table(9, (10,20))

    # MOCK PLAYER - will be player object
    player1 = 'MOCK PLAYER 1'
    player2 = 'MOCK PLAYER 2'

    table.sit_at_table(player1, 3)
    table.sit_at_table(player1, 7)

    table._button = 3
    table.move_button()
    assert table._button == 7

def test_move_button_high():
    table = Table(9, (10, 20))

    # MOCK PLAYER - will be player object
    player1 = 'MOCK PLAYER 1'
    player2 = 'MOCK PLAYER 2'

    table.sit_at_table(player1, 3)
    table.sit_at_table(player1, 9)

    table._button = 9
    table.move_button()
    assert table._button == 3
