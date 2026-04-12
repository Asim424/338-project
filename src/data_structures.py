class PriorityQueue:
    def __init__(self):
        self.data = []

    def print_data(self):
        for i in range(len(self.data)):
            print(f"{self.data[i].get_value()}", end=", ")

    def enqueue(self, item, priority):
        # Insert at the end, and then heapify upward
        self.data.append((priority, item))
        self.heapify_up(len(self.data) - 1)

    def dequeue(self):
        # Highest priorty is index zero, so we pop that
        if len(self.data) == 0:
            return None
        ret = self.data[0]

        # Move the last element to index zero, and heapify downward
        last = self.data.pop()

        if len(self.data) > 0:
            self.data[0] = last
            self.heapify_down(0)

        return ret

    def heapify_up(self, i):
        if i <= 0:
            return
            
        parent = (i - 1) // 2

        if parent >= 0:
            if self.data[i][0] < self.data[parent][0]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                self.heapify_up(parent)

    def heapify_down(self, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < len(self.data) and self.data[left][0] < self.data[largest][0]:
            largest = left

        if right < len(self.data) and self.data[right][0] < self.data[largest][0]:
            largest = right

        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify_down(largest)

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
