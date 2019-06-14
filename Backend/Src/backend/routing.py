from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from backend.token_auth import TokenAuthMiddleware
from gameConnections.tableConsumer import TableConsumer
from channels.security.websocket import OriginValidator
import os


websocket_urlpatterns = [
    re_path(r'^ws/(?P<table_id>[^/]+)/$', TableConsumer)
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
})
