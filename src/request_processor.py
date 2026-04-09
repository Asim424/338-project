from data_structures import Queue

class RequestQueue:
    def __init__(self):
        self.body = Queue()
    def enqueue(self,item):
        # item should be [request, request_type]
        self.body.enqueue(item)
    def dequeue(self):
        return self.body.dequeue()
    def peek(self):
        return self.body.peek()
