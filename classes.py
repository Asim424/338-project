import datetime

class Booking():
    def __init__(self, date_time : datetime):
        self.date_time = date_time

class Path: #straight line between 2 points, start and end order does not matter
    def __init__(self,start : tuple, end : tuple, weight : float):
        self.point_1 = start 
        self.point_2 = end 
        self.weight = weight #travel time

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

class Queue:
    def __init__(self):
        self.body = []
    def enqueue(self,item):
        if self.body is not None:
            self.body.append(item)
        else:
            self.body = [item]

    def dequeue(self):
        if self.body is not None:
            return self.body.pop(0)
        return IndexError("queue is empty")

    def peek(self):
        if self.body is not None:
            return self.body[0]
        return IndexError("queue is empty")
        


class Node:
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
            return Node(key, event)

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
        

class Requests:
    def __init__(self):
        self.body = Queue()
    def enqueue(self,item):
        # item should be [request, request_type]
        self.body.enqueue(item)
    def dequeue(self):
        return self.body.dequeue()
    def peek(self):
        return self.body.peek()
    

class Room:
    def __init__(self, room_id: str, capacity: int, room_type: str):

        self.room_id = room_id   # e.g. "ICT-121"

        self.capacity = capacity    # max occupancy

        self.room_type = room_type  # "lecture", "lab", "office"

        self.bookings = []  # list of Booking objects
    
    def events_in_range(self, start_time : datetime, end_time : datetime):
        output = []
        # for events in a given day have the start_time be the 12am of that day and end_time be 11:59 pm of that day
        for booking in self.bookings:
            if end_time >= booking.date_time >= start_time:
                output.append(booking)
    
    def next_event(self, curr_event : Booking):
        for booking in range(len(self.bookings)):
            if self.bookings[booking] == curr_event:
                return self.bookings[booking+1]
            
class priorityQ:
    def __init__(self):
        self.body = []
    def enqueue(self,item, priority : int):
        for i in range(len(self.body)):
            if(priority >= self.body[i][0]):
                if self.body is not None:
                    self.body.insert(i, [priority,item])
                else:
                    self.body =[[priority,item]]
    def dequeue(self):
        output = self.body.pop(0)
        return output

class priority_service:
    def __init__(self):
        self.body = priorityQ()
    def new_request(self,request, priority:int):
        self.body.enqueue(request,priority)
    def serve_request(self):
        return self.body.dequeue()
    
class Building:

    def __init__(self, building_id: str, name: str, location: tuple):

        self.building_id = building_id  # e.g. "ICT"

        self.name = name    # "Information and Comm. Tech."

        self.location = location    # (lat, lon) or grid coords

        self.rooms = priorityQ() # room_id -> Room  
    
    def add_room(self, item: Room, id : str):
        self.rooms.enqueue(item, id) #guarantees that rooms are sorted by id, to make lookup quicker


class Campus:

    def __init__(self):

        self.buildings = priorityQ() # building_id -> Building
        self.pathways   = []    # array of paths

    def find_path(self, source : Building, dest : Building):
        pass
        # brute force to find shortest, move only such that the lat,long becomes closer
    
    def add_building(self,item,id):
        self.buildings.enqueue(item,id)


class Stack:
    def __init__(self):
        self.body = []
    def push(self,item):
        if self.body is not None:
            self.body.append(item)
        else:
            self.body = [item]
    def pop(self):
        if self.body is not None:
            return self.body.pop()
        return IndexError("stack is empty")


class History:
    def __init__(self):
        self.nav = Stack()
    def add(self,start : Building, end : Building, along : list, total : float):
        #starting point, end  point, buildings passed on the way in order, total time spent
        self.nav.push([start,end,along,total])
    def remove(self):
        return self.nav.pop()

    

    