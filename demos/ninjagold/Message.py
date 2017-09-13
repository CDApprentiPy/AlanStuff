import datetime

class Message(object):
    def __init__(self, what, moneys):
        self.activity = what
        self.amount = moneys
        self.style = 'green' if moneys >= 0 else 'red'
        self.time = datetime.datetime.now()
    
    def to_message(self):
        return "You went to the {}  and earned {} at {}".format(self.activity, self.amount, self.time)


if __name__ == '__main__':
    bob = Message('mine', -15)
    print(bob.time)