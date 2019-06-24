from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from backend.token_auth import TokenAuthMiddleware
from channels.security.websocket import OriginValidator
import os

from gameConnections.player_consumer import PlayerConsumer
from gameConnections.table_gateway_consumer import TableGatewayConsumer

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
