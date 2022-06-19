class Friend:
    def Me(self):
        print('I am Bohdan`s friend')

    def Me_now(self):
        print('Actually, I am Bohdan`s friend')


class BestFriend(Friend):
    def Me_now(self):
        print('Actually, I am Bohdan`s best friend')


class Spectator(BestFriend):
    def __init__(self):
        super().Me()
        super().Me_now()

nick = Spectator()
