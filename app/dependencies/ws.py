from functools import lru_cache

from services import WebSocketManager


@lru_cache
def get_websocket_manager() -> WebSocketManager:
    return WebSocketManager()
