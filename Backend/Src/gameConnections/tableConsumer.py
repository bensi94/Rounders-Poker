import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TableConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if 'user' in self.scope and not self.scope['user'].is_anonymous:
            self.table_id = self.scope['url_route']['kwargs']['table_id']

            # Join the table
            await self.channel_layer.group_add(
                self.table_id,
                self.channel_name
            )

            await self.accept()
        else:
            await self.close()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)

    async def disconnect(self, event):
        # Leave the table
        await self.channel_layer.group_discard(
            self.table_id,
            self.channel_name
        )
