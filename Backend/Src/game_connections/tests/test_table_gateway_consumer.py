from django.test import TestCase
from game_connections.table_gateway_consumer import TableGatewayConsumer
from game_engine.game_controller import GameController
from unittest import mock

from core.models.table import Table


class TestTableGatewayConsumer(TestCase):
    """Test Table Gateway Consumer"""

    def setUp(self):
        scope = None
        self.consumer = TableGatewayConsumer(scope)
        self.consumer.channel_layer = mock.Mock()

    def create_test_table(self):
        return Table.objects.create(
            name='Table1',
            small_blind=10,
            big_blind=20,
        )

    def test_tables_empty_start(self):
        """Tests that tables are empty when consumer is created"""
        assert self.consumer.tables == {}

    def test_table_is_added(self):
        """Tests that a table is created and instance made of GameController"""

        table = self.create_test_table()

        event = {
            'table': table.id,
            'player': 'player_1',
            'buy_in': 100
        }
        self.consumer.player_new(event)

        assert len(self.consumer.tables) == 1
        assert isinstance(self.consumer.tables[table.id], GameController)

    def test_table_is_does_not_exist(self):
        """Tests that a table that is not in the database does not exist"""
        event = {
            'table': 1,
            'player': 'player_1',
            'buy_in': 100,
            'channel': 1
        }

        mock_response = mock.Mock()
        with mock.patch(
            'game_connections.table_gateway_consumer.async_to_sync',
            return_value=mock_response
        ):

            self.consumer.player_new(event)
            mock_response.assert_called_with(
                1,
                {'type': 'individual_update', 'error': {'type': 'Table.DoesNotExist'}}
            )

    def tearDown(self):
        for _, table in self.consumer.tables.items():
            table.stop_thread()
