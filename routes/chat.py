from fastapi import APIRouter, WebSocket
import asyncio
from services import connection_manager as Manger
from typing import List


router = APIRouter(prefix="/chat",tags=["chat"])


connections = Manger.ConnectionManager()

@router.websocket("/{sendId}")
async def chat(newsocket: WebSocket,sendId:str,receiverid:str):
    websocket:WebSocket = await connections.connect(webSocket= newsocket,send=sendId,receive=receiverid)
    try:
        while True:
            data = await websocket.receive_text()
            conns:List[WebSocket] =  connections.active_connections[connections.createChatID(receive=receiverid,send=sendId)]
            for item in conns:
                await item.send_text(f"Message - {data}")

    except:
        conns:List[WebSocket] = connections.active_connections[connections.createChatID(receive=receiverid,send=sendId)]
        conns.remove(websocket)
        print("disconnecting - ")


@router.get("/health")
async def health():
    return "Health is ok for chat"


