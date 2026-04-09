from data_structures import PriorityQueue

class PriorityService:
    def __init__(self):
        self.body = PriorityQueue()
    def new_request(self,request, priority:int):
        self.body.enqueue(request,priority)
    def serve_request(self):
        return self.body.dequeue()


