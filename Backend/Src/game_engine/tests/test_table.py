from django.test import TestCase
from core.models.table import Table as Table_Object

from game_engine.table import Table


class TestTable(TestCase):
    """Test the game engine table"""

    def create_test_table(self, name='Table1', max_players=2, small_blind=10, big_blind=20):
        return Table_Object.objects.create(
            name=name,
            max_players=max_players,
            small_blind=small_blind,
            big_blind=big_blind,
        )

    # Tests that table is made with two empty seats
    # Also test that blind init
    def test_init_two_users(self):
        table = Table(self.create_test_table())

        assert table._small_blind == 10
        assert table._big_blind == 20
        assert len(table._seats) == 2
        assert table._seats[1] is None
        assert table._seats[2] is None

    # User should be able to sit in empty seat
    def test_sit_at_table_empty_seat(self):

        table = Table(self.create_test_table())

        # MOCK USER
        user = 'MOCK USER'
        seat = 1
        return_value, return_msg = table.sit_at_table(user, seat)

        assert table._seats[seat] == 'MOCK USER'
        assert 'User seated at seat: ' + str(seat) == return_msg
        assert return_value is True

    # User should not be able to sit in occupied seat
    def test_sit_at_table_occupied(self):
        table = Table(self.create_test_table())

        # MOCK USERS
        user_1 = 'MOCK USER 1'
        user_2 = 'MOCK USER 2'
        seat = 1
        table.sit_at_table(user_1, seat)
        return_value, return_msg = table.sit_at_table(user_2, seat)

        assert table._seats[seat] != user_2
        assert 'Seat occupied, user not seated' == return_msg
        assert return_value is False

    # User should not be able to sit at seat that does not exist
    def test_sit_at_table_not_exist(self):
        table = Table(self.create_test_table())

        # MOCK USER
        user = 'MOCK USER'
        seat = 5  # Random number that does not exist
        return_value, return_msg = table.sit_at_table(user, seat)

        # Checks if user is seated at seat 5 (should be KeyError)
        with self.assertRaises(KeyError):
            assert table._seats[seat] != user
        assert return_msg == 'Invalid seat, user not seated'
        assert return_value is False

    # If one user sits down the game should be pending
    def test_sit_at_table_pending(self):
        table = Table(self.create_test_table())

        # MOCK USER
        user = 'MOCK USER'
        seat = 1
        table.sit_at_table(user, seat)

        assert table._state == 'PENDING'

    # If one user sits down the game should be running
    def test_sit_at_table_running(self):
        table = Table(self.create_test_table())

        # MOCK USER
        user1 = 'MOCK USER 1'
        user2 = 'MOCK USER 2'

        table.sit_at_table(user1, 1)
        table.sit_at_table(user2, 2)

        assert table._state == 'RUNNING'
        assert table._button == 1 or table._button == 2

    def test_empty_seat(self):
        table = Table(self.create_test_table())

        # MOCK USER
        user1 = 'MOCK USER 1'
        user2 = 'MOCK USER 2'

        table.sit_at_table(user1, 1)
        table.sit_at_table(user2, 2)

        table.empty_seat(1)
        assert table._state == 'PENDING'
        assert table._seats[1] is None

    def test_move_button(self):
        table = Table(self.create_test_table(max_players=9))

        # MOCK USER
        user1 = 'MOCK USER 1'

        table.sit_at_table(user1, 3)
        table.sit_at_table(user1, 7)

        table._button = 3
        table.move_button()
        assert table._button == 7

    def test_move_button_high(self):
        table = Table(self.create_test_table(max_players=9))

        # MOCK USER
        user1 = 'MOCK USER 1'

        table.sit_at_table(user1, 3)
        table.sit_at_table(user1, 9)

        table._button = 9
        table.move_button()
        assert table._button == 3

    def test_get_button(self):
        table = Table(self.create_test_table(max_players=9))

        # MOCK USER
        user1 = 'MOCK USER 1'

        table.sit_at_table(user1, 3)
        table.sit_at_table(user1, 9)

        table._button = 3
        table.move_button()

        assert table.get_button() == 9

    def test_update_blinds_and_get_blinds(self):
        table = Table(self.create_test_table(max_players=9))

        updated_blinds = (20, 40)

        table.update_blinds(updated_blinds)

        assert table.get_blinds() == updated_blinds
