from django.urls import re_path

from .import consumers

websocket_urlpatterns = [
    # .as_asgi()  get an ASGI application to handle the client websocket connection request.
    re_path(r"ws/sillyme/(?P<room_name>\w+)/$", consumers.chatConsumer.as_asgi()),
]