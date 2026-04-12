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

class Stack:
    def __init__(self):
        self.body = []
    def push(self,item):
        if self.body is not None:
            self.body.append(item)
        else:
            self.body = [item]
    def pop(self):
        if self.body is not None and self.body != []:
            return self.body.pop()
        return IndexError("stack is empty")
    def is_empty(self):
        if len(self.body) == 0:
            return True
        return False

class Queue:
    def __init__(self):
        self.body = []
    def enqueue(self,item):
        if self.body is not None:
            self.body.append(item)
        else:
            self.body = [item]

    def dequeue(self):
        if self.body is not None and self.body != []:
            return self.body.pop(0)
        return IndexError("queue is empty")

    def peek(self):
        if self.body is not None and self.body != []:
            return self.body[0]
        return IndexError("queue is empty")

def arr_bin_search(item, arr, delete : bool):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == item:
            if delete:
                item = arr.pop(mid)
            return mid
        
        if arr[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    return ValueError("Value not found")
