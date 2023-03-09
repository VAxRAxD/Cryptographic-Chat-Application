import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user=self.scope['user']
        self.room_group_name=self.scope['url_route']['kwargs']['room_name']
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chatMessage',
                'message':message,
                'user':self.user.username
            }
        )

    def chatMessage(self,event):
        message=event['message']
        user=event['user']
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'user':user
        }))