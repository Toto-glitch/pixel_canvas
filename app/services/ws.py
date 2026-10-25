from typing import Any

from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect


class WebSocketManager:
    def __init__(self) -> None:
        self._connections: set[WebSocket] = set()

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
        self._connections.add(ws)

    def disconnect(self, ws: WebSocket) -> None:
        self._connections.discard(ws)

    async def send_to(self, ws: WebSocket, data: dict[str, Any]) -> None:
        await ws.send_json(data)

    async def broadcast(self, data: dict[str, Any]) -> None:
        for ws in self._connections:
            try:
                await ws.send_json(data)
            except WebSocketDisconnect:
                self.disconnect(ws)
