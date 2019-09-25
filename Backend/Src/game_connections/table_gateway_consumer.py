from channels.consumer import SyncConsumer
from game_engine.game_controller import GameController
from asgiref.sync import async_to_sync

from core.models.table import Table


class TableGatewayConsumer(SyncConsumer):
    """The Table Gateway Consumer controls the Game Engine for each table"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tables = {}

    # By default this function will not start a new table if it does not exist
    # But by passing start as True the table will be started
    def check_table(self, event, start=False):
        table = None
        try:
            table_id = event['table']
            table = Table.objects.get(pk=table_id)

            if table.status == Table.CLOSED:
                async_to_sync(self.channel_layer.send)(
                    event['channel'],
                    {
                        'type': 'individual_update',
                        'error': {
                            'type': 'Table.Closed'
                        }
                    }
                )
                return None

            if start:
                table_id = event['table']
                if table_id not in self.tables:
                    self.tables[table_id] = GameController(table.id)
                    self.tables[table_id].start()

        except Table.DoesNotExist:
            async_to_sync(self.channel_layer.send)(
                event['channel'],
                {
                    'type': 'individual_update',
                    'error': {
                        'type': 'Table.DoesNotExist'
                    }
                }
            )

        return table

    def player_new(self, event):
        table = self.check_table(event, start=True)
        if table:
            self.tables[event['table']].add_player(
                event['user'],
                event['buy_in'],
                event['seat_number'],
                event['channel']
            )

    def observer_new(self, event):
        table = self.check_table(event, start=True)

        if table:
            self.tables[event['table']].add_observer(event['user'], event['channel'])
