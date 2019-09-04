from django.test import TestCase
from core.models.table import Table
from unittest import mock
import pytz
import datetime


class TableModelTests(TestCase):

    def test_creating_valid_table(self):
        """Test creating a valid table"""
        mocked_time = datetime.datetime(2019, 1, 1, tzinfo=pytz.utc)

        with mock.patch(
            'django.utils.timezone.now', mock.Mock(return_value=mocked_time)
        ):
            table = Table.objects.create(
                name='Table1',
                small_blind=10,
                big_blind=20,
            )

        self.assertEqual(table.name, 'Table1')
        self.assertEqual(table.created, mocked_time)
        self.assertEqual(table.small_blind, 10)
        self.assertEqual(table.big_blind, 20)
        self.assertEqual(table.hand_count, 0)
        self.assertEqual(table.average_pot, 0.0)
        self.assertEqual(table.max_players, 9)
        self.assertEqual(table.type, 'C')
        self.assertEqual(table.status, 'W')
