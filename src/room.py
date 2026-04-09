import datetime

class Booking():
    def __init__(self, date_time: datetime):
        self.date_time = date_time

class Room: 
    def __init__(self, room_id: str, capacity: int, room_type: str):
        self.room_id = room_id      # e.g. "ICT-121"
        self.capacity = capacity    # max occupancy
        self.room_type = room_type  # "lecture", "lab", "office"
        self.bookings = []          # list of Booking objects

class EventNode:
    def __init__(self, key, event):
        self.body = []

class Event_Index:
    # node is an array such that [key, event, left, right, height]
    def __init__(self):
        self.root = None


    # Height helper
    def height(self, node):
        if not node:
            return 0
        return node.body[4]


    # Balance factor
    def balance(self, node):
        return self.height(node.body[2]) - self.height(node.body[3])


    # Right rotation
    def rotate_right(self, y):
        x = y.body[2]
        t2 = x.body[3]

        x.body[3] = y
        y.body[2] = t2

        y.body[4] = 1 + max(self.height(y.body[2]), self.height(y.body[3]))
        x.body[4] = 1 + max(self.height(x.body[2]), self.height(x.body[3]))

        return x


    # Left rotation
    def rotate_left(self, x):
        y = x.body[3]
        t2 = y.body[2]

        y.body[2] = x
        x.body[3] = t2

        x.body[4] = 1 + max(self.height(x.body[2]), self.height(x.body[3]))
        y.body[4] = 1 + max(self.height(y.body[2]), self.height(y.body[3]))

        return y


    def insert(self, node, key, event):
        if not node:
            return EventNode(key, event)

        if key < node.body[0]:
            node.body[2] = self.insert(node.body[2], key, event)
        elif key > node.body[0]:
            node.body[3] = self.insert(node.body[3], key, event)
        else:
            return node

        node.body[4] = 1 + max(self.height(node.body[2]), self.height(node.body[3]))

        balance = self.balance(node)

        # Left Left
        if balance > 1 and key < node.body[2].body[0]:
            return self.rotate_right(node)

        # Right Right
        if balance < -1 and key > node.body[3].body[0]:
            return self.rotate_left(node)

        # Left Right
        if balance > 1 and key > node.body[2].body[0]:
            node.body[2] = self.rotate_left(node.body[2])
            return self.rotate_right(node)

        # Right Left
        if balance < -1 and key < node.body[3].body[0]:
            node.body[3] = self.rotate_right(node.body[3])
            return self.rotate_left(node)

        return node


    def add_event(self, key, event):
        self.root = self.insert(self.root, key, event)


    def search(self, node, key):
        if not node or node.body[0] == key:
            return node

        if key < node.body[0]:
            return self.search(node.body[2], key)
        else:
            return self.search(node.body[3], key)
