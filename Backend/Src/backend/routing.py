from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from backend.token_auth import TokenAuthMiddleware
from channels.security.websocket import OriginValidator
import os

from game_connections.player_consumer import PlayerConsumer
from game_connections.table_gateway_consumer import TableGatewayConsumer

websocket_urlpatterns = [
    re_path(r'^ws/(?P<table_id>[^/]+)/$', PlayerConsumer)
]

application = ProtocolTypeRouter({
    'websocket': OriginValidator(
        TokenAuthMiddleware(
            URLRouter(
                websocket_urlpatterns
            )
        ),
        [os.environ.get('FRONTEND_ORIGIN')],
    ),
    'channel': ChannelNameRouter({'game_engine': TableGatewayConsumer})
})
