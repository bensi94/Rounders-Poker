from django.test import TestCase
from gameConnections.table_gateway_consumer import TableGatewayConsumer
from GameEngine.game_controller import GameController


class TestTableGatewayConsumer(TestCase):
    """Test Table Gateway Consumer"""

    def setUp(self):
        scope = None
        self.consumer = TableGatewayConsumer(scope)

    def test_tables_empty_start(self):
        """Tests that tables are empty when consumer is created"""
        assert self.consumer.tables == {}

    def test_table_is_added(self):
        """Tests that a table is created and instance made of GameController"""
        event = {
            'channel': 'table_1',
            'player': 'player_1',
            'buy_in': 100
        }
        self.consumer.player_new(event)

        assert len(self.consumer.tables) == 1
        assert isinstance(self.consumer.tables['table_1'], GameController)

    def tearDown(self):
        for _, table in self.consumer.tables.items():
            table.stop_thread()
