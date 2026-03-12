import datetime
class Room:
    def __init__(self, room_id: str, capacity: int, room_type: str):

        self.room_id = room_id   # e.g. "ICT-121"

        self.capacity = capacity    # max occupancy

        self.room_type = room_type  # "lecture", "lab", "office"

        self.bookings = []  # list of Booking objects
    
    def events_in_range(self, start_time : datetime, end_time : datetime):
        output = []
        for booking in self.bookings:
            if booking.date_time - start_time >= 0 and booking.date_time - end_time <= 0:
                output.append(booking)

class Building:

    def __init__(self, building_id: str, name: str, location: tuple):

        self.building_id = building_id  # e.g. "ICT"

        self.name = name    # "Information and Comm. Tech."

        self.location = location    # (lat, lon) or grid coords

        self.rooms = {} # room_id -> Room  

class Campus:

    def __init__(self):

        self.buildings = {} # building_id -> Building
        self.pathways   = []    # array of paths

    def find_path(self, source : Building, dest : Building):
        pass
        # brute force to find shortest, move only such that the lat,long becomes closer


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
        return IndexError()


class History:
    def __init__(self):
        self.nav = Stack()
    def add(self,start : Building, end : Building, along : list, total : float):
        #starting point, end  point, buildings passed on the way in order, total time spent
        self.nav.push([start,end,along,total])
    def remove(self):
        return self.nav.pop()


class Booking():
    def __init__(self, date_time : datetime):
        self.date_time = date_time
    

class Path: #straight line between 2 points, start and end order does not matter
    def __init__(self,start : tuple,end : tuple, weight : float):
        self.point_1 = start 
        self.point_2 = end 
        self.weight = weight #travel time
    