from channels.consumer import SyncConsumer
from game_engine.game_controller import GameController
from asgiref.sync import async_to_sync

from core.models.table import Table


class TableGatewayConsumer(SyncConsumer):
    """The Table Gateway Consumer controls the Game Engine for each table"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tables = {}

    def player_new(self, event):
        try:
            table_id = event['table']
            table = Table.objects.get(pk=table_id)
            if table_id not in self.tables:
                self.tables[table_id] = GameController(table)
                self.tables[table_id].start()

            self.tables[table_id].add_player(event['player'], event['buy_in'])
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
