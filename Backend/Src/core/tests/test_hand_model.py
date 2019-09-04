from django.test import TestCase
from django.core.exceptions import ValidationError
from unittest import mock
import pytz
import datetime
import pytest

from core.models.table import Table
from core.models.hand import Hand
from core.tests.constants import valid_history_example,\
    invalid_history_invalid_stage


class HandModelTests(TestCase):

    def test_createing_valid_hand(self):
        """Test creating a valid hand"""

        mocked_time = datetime.datetime(2019, 1, 1, tzinfo=pytz.utc)

        with mock.patch(
            'django.utils.timezone.now', mock.Mock(return_value=mocked_time)
        ):
            table = Table.objects.create(
                name='Table1',
                small_blind=10,
                big_blind=20,
            )

            hand = Hand.objects.create(
                table=table,
                history=valid_history_example
            )

            self.assertEqual(hand.history, valid_history_example)

    @pytest.mark.focus
    def test_creating_invalid_hand(self):
        """Test creating hand with invalid json"""

        mocked_time = datetime.datetime(2019, 1, 1, tzinfo=pytz.utc)

        with mock.patch(
            'django.utils.timezone.now', mock.Mock(return_value=mocked_time)
        ):
            table = Table.objects.create(
                name='Table1',
                small_blind=10,
                big_blind=20,
            )

            hand = Hand(
                table=table,
                history=invalid_history_invalid_stage
            )

        expected_msg = \
            '["Error validating JSON: \'HELLO\' is not one of'\
            ' [\'PREFLOP\', \'FLOP\', \'TURN\', \'RIVER\']"]'

        with self.assertRaisesMessage(ValidationError, expected_msg):
            hand.full_clean()
