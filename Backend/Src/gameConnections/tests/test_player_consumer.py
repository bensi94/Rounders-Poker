from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from channels.testing import WebsocketCommunicator
from backend.routing import application
import pytest
import os


@database_sync_to_async
def create_user_and_token(**params):
    user = get_user_model().objects.create_user(**params)
    token = Token.objects.create(user=user)
    return user, token


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
async def test_connect_authorized():
    """Test that a user that exists with valid token gets connected"""
    mockUser = {
        'username': 'bensi94',
        'password': 'testpass',
        'name': 'Benedikt Oskarsson'
    }

    _, token = await create_user_and_token(**mockUser)
    path = 'ws://localhost:8000/ws/game/?Token=' + str(token)
    allowedOrigin = 'http://' + str(os.environ.get('FRONTEND_ORIGIN'))
    communicator = WebsocketCommunicator(
        application, path, headers=[
            (b'origin', bytes(allowedOrigin, encoding='utf-8'))]
    )
    connected, _ = await communicator.connect()
    assert connected


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
async def test_connect_invalid_token():
    """Test that user with invalid token will not be connected"""
    mockUser = {
        'username': 'bensi94',
        'password': 'testpass',
        'name': 'Benedikt Oskarsson'
    }

    await create_user_and_token(**mockUser)
    path = 'ws://localhost:8000/ws/game/?Token=INVALIDTOKEN'
    allowedOrigin = 'http://' + str(os.environ.get('FRONTEND_ORIGIN'))
    communicator = WebsocketCommunicator(
        application, path, headers=[
            (b'origin', bytes(allowedOrigin, encoding='utf-8'))]
    )
    connected, _ = await communicator.connect()
    assert not connected


@pytest.mark.django_db(transaction=True)
@pytest.mark.asyncio
async def test_connect_invalid_origin():
    """Test that user with from invalid origin will not connected"""
    mockUser = {
        'username': 'bensi94',
        'password': 'testpass',
        'name': 'Benedikt Oskarsson'
    }

    _, token = await create_user_and_token(**mockUser)
    path = 'ws://localhost:8000/ws/game/?Token=' + str(token)
    allowedOrigin = 'http://INVALID_ORIGIN'
    communicator = WebsocketCommunicator(
        application, path, headers=[
            (b'origin', bytes(allowedOrigin, encoding='utf-8'))]
    )
    connected, _ = await communicator.connect()
    assert not connected
