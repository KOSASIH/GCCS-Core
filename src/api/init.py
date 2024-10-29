# api/__init__.py

from .rest_api import app as rest_api_app
from .websocket_api import websocket_app

__all__ = ['rest_api_app', 'websocket_app']
