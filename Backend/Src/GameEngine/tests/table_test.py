from table import Table
import pytest

# Tests that table is made with two empty seats
# Also test that blind init 
def test_init_two_users():
    # Blinds are set to 10 and 20
    table = Table(2, (10,20))
    
    assert table._small_blind == 10
    assert table._big_blind == 20
    assert len(table._seats) == 2
    assert table._seats[1] == None
    assert table._seats[2] == None

# User should be able to sit in empty seat
def test_sit_at_table_empty_seat():
    table = Table(2, (10,20))

    # MOCK USER
    user = 'MOCK USER'
    seat = 1
    return_value, return_msg = table.sit_at_table(user, seat)

    assert table._seats[seat] == 'MOCK USER'
    assert 'User seated at seat: ' + str(seat) == return_msg
    assert return_value == True

# User should not be able to sit in occupied seat
def test_sit_at_table_occupied():
    table = Table(2, (10, 20))

    # MOCK USERS 
    user_1 = 'MOCK USER 1'
    user_2 = 'MOCK USER 2'
    seat = 1
    table.sit_at_table(user_1, seat)
    return_value, return_msg = table.sit_at_table(user_2, seat)

    assert table._seats[seat] != user_2
    assert 'Seat occupied, user not seated' == return_msg
    assert return_value == False

# User should not be able to sit at seat that does not exist  
def test_sit_at_table_not_exist():
    table = Table(2, (10, 20))

    # MOCK USER
    user = 'MOCK USER'
    seat = 5 # Random number that does not exist
    return_value, return_msg = table.sit_at_table(user, seat)
    
    # Checks if user is seated at seat 5 (should be KeyError)
    with pytest.raises(KeyError):
        assert table._seats[seat] != user
    assert return_msg == 'Invalid seat, user not seated'
    assert return_value == False

# If one user sits down the game should be pending
def test_sit_at_table_pending():
    table = Table(2, (10, 20))

    # MOCK USER
    user = 'MOCK USER'
    seat = 1
    table.sit_at_table(user, seat)

    assert table._state == 'PENDING'


# If one user sits down the game should be running
def test_sit_at_table_running():
    table = Table(2, (10, 20))

    # MOCK USER
    user1 = 'MOCK USER 1'
    user2 = 'MOCK USER 2'

    table.sit_at_table(user1, 1)
    table.sit_at_table(user2, 2)

    assert table._state == 'RUNNING'
    assert table._button == 1 or table._button == 2


def test_empty_seat():
    table = Table(2, (10, 20))

    # MOCK USER
    user1 = 'MOCK USER 1'
    user2 = 'MOCK USER 2'

    table.sit_at_table(user1, 1)
    table.sit_at_table(user2, 2)

    table.empty_seat(1)
    assert table._state == 'PENDING'
    assert table._seats[1] == None

def test_move_button():
    table = Table(9, (10,20))

    # MOCK USER
    user1 = 'MOCK USER 1'
    user2 = 'MOCK USER 2'

    table.sit_at_table(user1, 3)
    table.sit_at_table(user1, 7)

    table._button = 3
    table.move_button()
    assert table._button == 7

def test_move_button_high():
    table = Table(9, (10, 20))

    # MOCK USER
    user1 = 'MOCK USER 1'
    user2 = 'MOCK USER 2'

    table.sit_at_table(user1, 3)
    table.sit_at_table(user1, 9)

    table._button = 9
    table.move_button()
    assert table._button == 3

def test_get_button():
    table = Table(9, (10, 20))

    # MOCK USER
    user1 = 'MOCK USER 1'
    user2 = 'MOCK USER 2'

    table.sit_at_table(user1, 3)
    table.sit_at_table(user1, 9)

    table._button = 3
    table.move_button()
    
    assert table.get_button() == 9

def test_update_blinds_and_get_blinds():
    table = Table(9, (10, 20))

    updated_blinds = (20, 40)

    table.update_blinds(updated_blinds)

    assert table.get_blinds() == updated_blinds


