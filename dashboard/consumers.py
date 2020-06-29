from channels.generic.websocket import AsyncWebsocketConsumer

class DashboardConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.groupname = 'dashboard'
        print("Connected")
        await self.channel_layer.group_add(self.groupname,self.channel_name)
        await self.accept()
    
    async def disconnect(self,close_code):
        print("Disconnected")
        await self.channel_layer.group_discard(self.groupname,self.channel_name)
    
    async def receive(self,text_data):
        print("Got: ",text_data)
        await self.channel_layer.group_send(self.groupname,{
            'type': 'process',
            'data': text_data
        })
    
    async def process(self,event):
        data = event['data']
        await self.send(text_data=data)