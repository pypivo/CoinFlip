
from fastapi import WebSocket, WebSocketException
from fastapi.routing import APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession

from .game_manager import manager
from ..services import _get_user_by_id

async def create_ws_connect(websocket: WebSocket, user_id: int, game_name: str, session: AsyncSession):
    user = await _get_user_by_id(user_id, session)
    await manager.connect(game_name=game_name, websocket=websocket, user_id=user_id)
    if user is None:
        raise WebSocketException(code=404)