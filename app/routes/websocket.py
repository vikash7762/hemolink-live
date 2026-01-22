from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List, Dict

router = APIRouter()

# ---------------------------------------------
# 1. Connection Manager
# This class keeps track of who is online.
# ---------------------------------------------
class ConnectionManager:
    def __init__(self):
        # Dictionary to store active connections: {user_id: WebSocket}
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections[user_id] = websocket
        print(f"✅ User {user_id} connected via WebSocket")

    def disconnect(self, user_id: str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]
            print(f"❌ User {user_id} disconnected")

    async def send_personal_message(self, message: str, user_id: str):
        if user_id in self.active_connections:
            await self.active_connections[user_id].send_text(message)

# Create a global manager instance
manager = ConnectionManager()

# ---------------------------------------------
# 2. The WebSocket Endpoint
# Users connect here to "listen" for alerts.
# ---------------------------------------------
@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(websocket, user_id)
    try:
        while True:
            # Keep the connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(user_id)