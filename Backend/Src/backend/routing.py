from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from gameConnections.tableConsumer import TableConsumer

websocket_urlpatterns = [
    re_path(r'^ws/game$', TableConsumer)
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
