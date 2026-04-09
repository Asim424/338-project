import datetime

class Booking:
    def __init__(self, event_name: str, start_time: datetime, end_time: datetime):
        self.event_name = event_name
        self.start_time = start_time  # This replaces date_time
        self.end_time = end_time

    # This helper allows to compare bookings directly by time
    def __lt__(self, other):
        return self.start_time < other.start_time

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
        self.room_id = room_id
        self.capacity = capacity
        self.room_type = room_type
        
        # We will use the AVL Tree (Event_Index) for high-performance lookups
        self.calendar = Event_Index() 
        # Keep the list for simple sequential access if needed
        self.bookings = []
    
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

        self.vertices = Queue()  
    
    def add_room(self, item: Room, id : str):
        self.rooms.enqueue(item, id) #guarantees that rooms are sorted by id, to make lookup quicker

    def add_vertix(self, vertix:vertix):
        self.vertices.enqueue(vertix)

class vertix:
    def __init__(self):
        self.buildings = [0]*2
        self.weight = 0
    
    def make_connection(self, build1:Building, build2:Building, time:int):
        self.buildings = [build1,build2]
        self.weight = time
    
    def get_other(self, building:Building):
        if self.buildings[0] is building:
            return self.buildings[1]
        return self.buildings[0]
        

class Campus:

    def __init__(self):
        self.buildings = priorityQ() # building_id -> Building

    def find_path(self, source, dest):
        pq = priorityQ()
        pq.enqueue((source, [source]), 0)  # (current, path), priority = cost

        visited = set()

        while pq.body:
            priority, (current, path) = pq.dequeue()

            if current in visited:
                continue
            visited.add(current)

            if current == dest:
                return path, priority

            for vert in current.vertices.body:
                neighbor = vert.get_other(current)

                if neighbor not in visited:
                    pq.enqueue(
                        (neighbor, path + [neighbor]),
                        priority + vert.weight
                    )

        return None, float("inf")

        # path = []
        # temp_path = []
        # temp_weight = [10000000000,-1]
        # buildings = self.buildings.body.copy()
        # buildings.remove(source)
        # curr_building = source
        # vertices = curr_building.vertices.body.copy()
        # vertix = vertices[0]
        # vertices.pop(0)
        
        # while True:
        #     if vertix.buildings.contains(dest):
        #         if temp_weight[0] > temp_weight[1]:
        #             path = temp_path
        #             path.append(vertix)
        #             temp_weight[0] = temp_weight[1]
            
        #     else:
        #         curr_building = vertix.get_other
        #         temp_weight[1] += vertix.weight
        #         temp_path += vertix
        #         vertices = curr_building.vertices.body.copy()
        #         vertix = vertices[0]
        #         vertices.pop(0)
        #         buildings.remove(curr_building)
            

                
    
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


if __name__ == "__main__":
    from math import floor
    import random

    def names_from_list(list,building):
        out = []
        for item in list:
            out.append(item.get_other(building).building_id)
        return out

    def weights_from_list(list):
        out = []
        for item in list:
            out.append(item.weight)
        return out
    campus = Campus()
    buildings = [Building]*10

    for i in range(len(buildings)):
        buildings[i] = Building(f"{i}",f"{i}",(i,i))

    for i in range(len(buildings)):
        for j in range(len(buildings)):
            if i == j:
                break

            if random.random() <= 0.5:
                temp = vertix()
                temp.make_connection(buildings[i],buildings[j],floor(random.random()*10))
                buildings[i].add_vertix(temp)
                buildings[j].add_vertix(temp)   
    build1 = floor(random.random()*10)  
    build2 = floor(random.random()*10)
    path = campus.find_path(buildings[build1],buildings[build2])
    for building in buildings:
        print(building.building_id,"connects to",names_from_list(building.vertices.body,building),"with weights",weights_from_list(building.vertices.body))

    print(f"path from {buildings[build1].building_id} to {buildings[build2].building_id}:")

    for building in path[0]:
        print(building.building_id)