from typing import List,Dict
from fastapi import WebSocket
class ConnectionManager:
    def __init__(self):
        self.active_connections:Dict[str,List[WebSocket]] ={} #  dictionary of type Str str

    def createChatID(self,send:str,receive:str):
        users = [send,receive]
        users.sort()
        return users[0] + "-" + users[1]
    
    async def connect(self,webSocket:WebSocket,send:str,receive:str):
        # if socket connection is already there then don't add it
        id:str = self.createChatID(send,receive)
        if id not in self.active_connections:
            await webSocket.accept()  
                    
            self.active_connections[id] = [webSocket]
            return webSocket
        else:
            await webSocket.accept()
            self.active_connections[id].append(webSocket)
            return webSocket
    
    def disconnect(self,id):
        self.active_connections.pop(id)
    
    async def send_message(self,id: str,message:str):
        await self.active_connections[id].send_text(message)
        