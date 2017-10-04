"""
A Demo of how sockets work
"""
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

# def http_consumer(message):
#     response = HttpResponse("Hello world! You asked for it %s" % message.content['path'])
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)

# def ws_consumer(message):
#     """This is the web socket message consuming function"""
#     message.reply_channel.send({
#         "text": message.content['text'],
#     })

# connect this to websocket.connect
def ws_add(message):
    """when somebody sockets, add them to a chat group"""
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)

# connect this to websocket.disconnect
def ws_disconnect(message):
    """when somebody unsockets remove them from a chat group"""
    Group("chat").discard(message.repl_channel)

# connect this to websocket.receive
def ws_message(message):
    """This handles receving a socket-based message for teh chatters"""
    Group("chat").send({
        # what is [user] ?
        "text": "[user] %s" % message.content['text'],
    })
