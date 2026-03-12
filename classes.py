import datetime

class Booking():
    def __init__(self, date_time : datetime):
        self.date_time = date_time

class Path: #straight line between 2 points, start and end order does not matter
    def __init__(self,start : tuple,end : tuple, weight : float):
        self.point_1 = start 
        self.point_2 = end 
        self.weight = weight #travel time

def bin_search(item, arr, delete : bool):
    pass

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
        

class Event_Index:
    def __init__(self):
        pass
    # do this later for bonus marks if time permits
    #For full marks on the bonus, implement a self-balancing index for the booking system that
    # guarantees O(log n) insert and lookup at all times, even under adversarial insertion patterns (e.g.,
    # all bookings inserted in chronological order)


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

    

    