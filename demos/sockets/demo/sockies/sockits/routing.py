from channels.routing import route
from sockits.consumers import ws_connect, ws_increment
channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_increment),
]