from room import *
from table_format import format_row

class Building:
    def __init__(self, building_id: str, name: str, location: tuple):
        self.building_id = building_id  # e.g. "ICT"
        self.name = name                # "Information and Comm. Tech."
        self.location = location        # (lat, lon) or grid coords
        self.rooms = {}                 # room_id -> Room

    def insert_room(self, room: Room):
        self.rooms[room.room_id] = room

    def remove_room(self, room_id: str):
        if room_id not in self.rooms:
            raise KeyError(f"Room {room_id} not found")

        del self.rooms[room_id]            

    def lookup_room(self, room_id: str):
        if room_id not in self.rooms:
            return None

        return self.rooms[room_id]

    def print_room_table(self):
        headers = ["ID", "Capacity", "Room Type"]
        cell_width = 24

        # Header
        header_row = format_row(headers, cell_width)
        print(header_row)
        print("-" * len(header_row))

        # Building rows
        for room in self.rooms.values():
            print(format_row([room.room_id, room.capacity, room.room_type], cell_width))
