# Interfaz/routing.py
from django.urls import re_path
from django.urls import path
#from channels.routing import route
from Interfaz.consumers import HomeConsumer

from . import consumers

websocket_urlpatterns = [
    path('ws/interfaz/', consumers.HomeConsumer),
    #route('websocket.home',HomeConsumer),
    #re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]
