from channels.generic.websocket import AsyncWebsocketConsumer

class DashboardConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(self.groupname,self.channel_name)
        await self.accept()
    
    async def disconnect(self,close):
        pass
    
    async def recieve(self,data):
        pass