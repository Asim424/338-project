
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TicketQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if (self.head == None):
            self.head = Node(data)
            self.tail = self.head
            return
        
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def dequeue(self):
        if self.head == None:
            return None
        next = self.head.next
        data = self.head.data
        self.head.next = None
        if self.head == self.tail:
            self.tail = None
        self.head = next
        return data

        
        