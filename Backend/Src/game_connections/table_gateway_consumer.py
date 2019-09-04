from channels.consumer import SyncConsumer
from game_engine.game_controller import GameController


class TableGatewayConsumer(SyncConsumer):
    """The Table Gateway Consumer controls the Game Engine for each table"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tables = {}

    def player_new(self, event):
        table_id = event['channel']
        if table_id not in self.tables:
            self.tables[table_id] = GameController(table_id)
            self.tables[table_id].start()

        self.tables[table_id].add_player(event['player'], event['buy_in'])
