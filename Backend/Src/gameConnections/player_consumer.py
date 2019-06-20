import json
from channels.generic.websocket import AsyncWebsocketConsumer


class PlayerConsumer(AsyncWebsocketConsumer):
    '''Handels all socket communications for each player'''

    async def connect(self):
        # User that is not authenticated (anonymous) should not be accepted
        if 'user' in self.scope and not self.scope['user'].is_anonymous:
            self.table_id = self.scope['url_route']['kwargs']['table_id']

            # Join the table
            await self.channel_layer.group_add(
                self.table_id,
                self.channel_name
            )
            self.user = str(self.scope['user'])
            await self.accept()

            await self.channel_layer.group_add(
                'table1',
                self.channel_name
            )

            await self.channel_layer.send(
                'game_engine',
                {
                    'type': 'player.new',
                    'player': self.user,
                    'channel': self.channel_name,
                    'buy_in': 6
                }
            )

        else:
            await self.close()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)

    async def state_update(self, event):
        self.send(event["state"])

    async def disconnect(self, event):
        # Leave the table
        await self.channel_layer.group_discard(
            self.table_id,
            self.channel_name
        )
