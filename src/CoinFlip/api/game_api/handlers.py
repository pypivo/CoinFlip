import json

from fastapi import WebSocket, WebSocketDisconnect, Depends, WebSocketException
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.CoinFlip.db.engine import get_db
from .game_manager import manager
from .ws_connection import create_ws_connect

game_router = APIRouter()

@game_router.websocket("/ws/connect-to-game/{user_id}/{game_name}")
async def ws_connect_to_game(websocket: WebSocket, user_id: int, game_name: str, db: AsyncSession = Depends(get_db)):
    try:
        await create_ws_connect(websocket, user_id, game_name, db)
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            await manager.guess_coin_side(game_name, data["coin_side"], user_id)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
    except WebSocketException:
        await manager.send_personal_message(f"User with id {user_id} is not found.", websocket)
        manager.disconnect(websocket)
