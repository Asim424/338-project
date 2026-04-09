class PriorityQueue:
    def __init__(self):
        self.body = []

    def enqueue(self, item, priority):
        inserted = False

        for i in range(len(self.body)):
            if priority < self.body[i][0]:  # smaller = higher priority
                self.body.insert(i, [priority, item])
                inserted = True
                break

        if not inserted:
            self.body.append([priority, item])

    def dequeue(self):
        if not self.body:
            return None
        return self.body.pop(0)  # returns [priority, item]
