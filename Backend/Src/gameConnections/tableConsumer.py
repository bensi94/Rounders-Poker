from channels.generic.websocket import AsyncWebsocketConsumer


class TableConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')

        await self.accept()

    async def receive(self):
        print('receive')

    async def disconnect(self, event):
        print('disconnected')
