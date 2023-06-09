import json
from random import choice
from typing import List, Optional
from collections import defaultdict

from fastapi import WebSocket

class GameManager:
    def __init__(self):
        self.active_connections: defaultdict = defaultdict(lambda: defaultdict(Optional[WebSocket]))
        self.game = defaultdict(lambda: defaultdict(Optional[int]))

    async def connect(self, game_name: str, websocket: WebSocket, user_id: int):
        if len(self.active_connections[game_name]) == 2:
            await websocket.accept()
            await websocket.close(4000)
        else:
            await websocket.accept()
            self.active_connections[game_name][user_id] = websocket
            self.game[game_name][user_id] = None

    async def guess_coin_side(self, game_name: str, coin_side: int, user_id: int):
        if self.game[game_name][user_id] is None:
            self.game[game_name][user_id] = coin_side
        for user in self.game[game_name]:
            if self.game[game_name][user] is None:
                break
        else:
            right_coin_side = choice((0, 1))
            for user in self.game[game_name]:
                if self.game[game_name][user] == right_coin_side:
                    await GameManager.send_victory_message(websocket=self.active_connections[game_name][user],
                                                           coin_side=right_coin_side)
                else:
                    await GameManager.send_lose_message(websocket=self.active_connections[game_name][user],
                                                        coin_side=right_coin_side)
                self.game[game_name][user] = None

    def disconnect(self, websocket: WebSocket):
        self.active_connections[websocket].remove(websocket)

    @staticmethod
    async def send_victory_message(websocket: WebSocket, coin_side: int):
        await websocket.send_text(f"Правильная сторона {coin_side}.\nПоздравляю, вы угадали!")

    @staticmethod
    async def send_lose_message(websocket: WebSocket, coin_side: int):
        await websocket.send_text(f"Правильная сторона {coin_side}.\nК сожалению, вы проиграли.")

    async def send_to_game_message(self, message: str, game_name: str):
        await self.active_connections[game_name][0].send_text(message)
        await self.active_connections[game_name][1].send_text(message)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = GameManager()