from datetime import datetime
from data_structures import Event_Index

class Booking:
    def __init__(self, event_name: str, start_time: datetime, end_time: datetime):
        self.event_name = event_name
        self.start_time = start_time 
        self.end_time = end_time

class Room: 
    def __init__(self, room_id: str, capacity: int, room_type: str):
        self.room_id = room_id
        self.capacity = capacity
        self.room_type = room_type
        self.calendar = Event_Index()  # Now correctly imported
        self.bookings = [] 

    def add_booking(self, event_name, start, end):
        new_booking = Booking(event_name, start, end)
        self.calendar.add_event(start, new_booking)
        
        # Manual Insertion Sort (to satisfy the "no built-in functions" rule)
        inserted = False
        for i in range(len(self.bookings)):
            if new_booking.start_time < self.bookings[i].start_time:
                self.bookings.insert(i, new_booking)
                inserted = True
                break
        if not inserted:
            self.bookings.append(new_booking)

    def events_in_range(self, start_time: datetime, end_time: datetime):
        output = []
        if self.calendar.root:
            self.calendar.get_range(self.calendar.root, start_time, end_time, output)
        return output

    def next_event(self, current_time: datetime):
        for booking in self.bookings:
            if booking.start_time > current_time:
                return booking
        return None