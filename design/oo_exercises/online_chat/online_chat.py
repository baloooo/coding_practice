from abc import ABCMeta
# https://code.facebook.com/posts/820258981365363/building-mobile-first-infrastructure-for-messenger/
"""
Todo: Add more details, next time around.

Possibly use observer pattern to notify users in GroupChats about messages sent.
Supplementary material:
cassandra vs hbase: https://stackoverflow.com/questions/14950728/why-hbase-is-a-better-choice-than-cassandra-with-hadoop
https://github.com/miguelalba-old/hfdp-python/blob/master/factory/pizzas.py
https://github.com/miguelalba-old/hfdp-python/blob/master/singleton/chocolateboiler.py
http://highscalability.com/blog/2014/2/26/the-whatsapp-architecture-facebook-bought-for-19-billion.html

"""

class Messenger(object):
    '''
    Messenger is a singleton class
    One possible strategy could be to have sort of mailboxes for each users on the server, and when one
    user sends some message directly to other it can sit in users mailbox along with other messages for 
    group chat and others. When user opens up the mobile application and asks for the delta of messages
    since the last syn from the server they can push the mailbox down to user mobile and then mobile app
    can sort the messages in to one-one messages and group messages and render them in app for reading.
    https://www.safaribooksonline.com/library/view/designing-data-intensive-applications/9781491903063/ch01.html
    '''
    _instance = None
    _lock = thread.allocate_lock()

    def __new__(cls):
        cls._lock_acquire()
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        cls._lock_release()
        return cls.__instance

    @staticmethod
    def get_uuid()
        '''
        Utility method which returns UUIDs which can be used for user_id or chat_ids.
        '''
        pass


class UserService(object):

    def __init__(self):
        self.users_by_id = {}  # key: user id, value: User

    def add_user(self, user_id, name, pass_hash):  # ...
    def remove_user(self, user_id):  # ...
    def add_friend_request(self, from_user_id, to_user_id):  # ...
    def approve_friend_request(self, from_user_id, to_user_id):  # ...
    def reject_friend_request(self, from_user_id, to_user_id):  # ...


class User(object):

    def __init__(self, user_id, name, pass_hash):
        self.user_id = user_id
        self.name = name
        self.pass_hash = pass_hash
        self.friends_by_id = {}  # key: friend id, value: User
        self.friend_ids_to_private_chats = {}  # key: friend id, value: private chats
        self.group_chats_by_id = {}  # key: chat id, value: GroupChat
        self.received_friend_requests_by_friend_id = {}  # key: friend id, value: AddRequest
        self.sent_friend_requests_by_friend_id = {}  # key: friend id, value: AddRequest

    def message_user(self, friend_id, message):  # ...
    def message_group(self, group_id, message):  # ...
    def send_friend_request(self, friend_id):  # ...
    def receive_friend_request(self, friend_id):  # ...
    def approve_friend_request(self, friend_id):  # ...
    def reject_friend_request(self, friend_id):  # ...
    def fetch_recent_mesages(self):
        # Messenger will be a singleton class, which creates an instance of the backend
        # Messenger class which has UserService and other classes
        messenger = Messenger()
        # last_synced_timestamp would help messenger backend to only send the messages we have
        # not received since last sync and prevent unnecessary bandwidth usage
        new_messages = messenger.get_recent_messages(user_id, self.last_synced_timestamp)
        # this method would distribute these new messages to each of the chats
        self.serve_messages(new_messages)


class Chat(metaclass=ABCMeta):

    def __init__(self):
        self.chat_id = self.get_uuid()
        self.users = []
        '''
        This will be a ordered queue
        we can have two pointers within here, one points to the point untill
        where messages have been synced to DB and the other till where user
        has seen messages.
        '''
        self.messages = []

class PrivateChat(Chat):

    def __init__(self, first_user, second_user):
        super(PrivateChat, self).__init__()
        self.users.append(first_user)
        self.users.append(second_user)
        self.registerObserver(self.chat_id, [first_user, second_user])

class GroupChat(Chat):
    def __init__(self, users):
        super(GroupChat, self).__init__(users)

    def drop_message(self, user, message_text):
        # gets unique message id from a service
        message_id = self.get_message_id()
        message = Message(message_id, message_text, user)
        # stored in message history of group
        self.messages.append(message) # Every group chat will have it's own message queue
        self.notifyObserver(message) # Notifies(drops message in inboxes for) all group chat participants

    def registerObserver(self, user):
        '''
        add_user and registerObserver can be same
        '''
        pass

    def notifyObserver(self, message):
        for user in self.users:
            if user != message.user:
                # don't send notification to user who generated the message
                user.receive_message(message)

    def add_user(self, user):  # ...
    def remove_user(self, user):  # ... 


class Message(object):

    def __init__(self, message_id, message, user):
        # user who generated the message
        self.user = user
        self.message_id = message_id
        self.message = message
        self.timestamp = datetime.now()
        self.status = Status.UNREAD


class AddRequest(object):

    def __init__(self, from_user_id, to_user_id, request_status, timestamp):
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.timestamp = timestamp


class MessageStatus(Enum):
    UNREAD = 0 READ = 1

class RequestStatus(Enum):

    UNREAD = 0
    READ = 1
    ACCEPTED = 2
    REJECTED = 3
