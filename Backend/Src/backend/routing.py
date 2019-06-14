from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from backend.token_auth import TokenAuthMiddleware
from gameConnections.tableConsumer import TableConsumer

websocket_urlpatterns = [
    re_path(r'^ws/(?P<table_id>[^/]+)/$', TableConsumer)
]

application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddleware(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
