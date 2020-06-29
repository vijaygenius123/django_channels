from channels.generic.websocket import AsyncWebsocketConsumer

class DashboardConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.connect()
    
    async def disconnect(self,close):
        await self.disconnect()
    
    async def recieve(self,data):
        print(data)
        pass