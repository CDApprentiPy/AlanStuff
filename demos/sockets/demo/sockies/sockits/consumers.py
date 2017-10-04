from channels import Group
import json


def ws_connect(message):
    """ Handles a client joining!"""
    # Accepts the connection
    message.reply_channel.send({"accept": True})
    # adds connected person to current counter group
    Group("counter").add(message.reply_channel)
    # should go on to tell them current counter value
    try:
        message.channel_session['count'] = message.channel_session['count'] + 1
    except:
        message.channel_session['count'] = 0
    message.reply_channel.send({
        'text': json.dumps({
            'count': message.channel_session['count'],
        })
    })


def ws_increment(message):
    """This should handle a user clicking on the button"""
    count = message.channel_session['count'] + 1
    message.channel_session['count'] = count
    Group("counter").send({
        "text": json.dumps({
            "count": message.channel_session['count'],
        }) ,
    })