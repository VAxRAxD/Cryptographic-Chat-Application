import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name=self.scope['url_route']['kwargs']['room_name']
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        user=text_data_json['user']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chatMessage',
                'message':message,
                'user':user
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

class HomeConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name='home'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    
    def receive(self, text_data):
        text_data_json=json.loads(text_data)
        type=text_data_json['type']
        sender=text_data_json['sender']
        reciever=text_data_json['reciever']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': type,
                'sender':sender,
                'reciever':reciever
            }
        )

    def Request(self,event):
        sender=event['sender']
        reciever=event['reciever']
        self.send(text_data=json.dumps({
            'type':'Request',
            'sender':sender,
            'reciever':reciever
        }))
    
    def Accept(self,event):
        sender=event['sender']
        reciever=event['reciever']
        self.send(text_data=json.dumps({
            'type':'Accept',
            'sender':sender,
            'reciever':reciever
        }))