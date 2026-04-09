class Room: 
    def __init__(self, room_id: str, capacity: int, room_type: str):
        self.room_id = room_id      # e.g. "ICT-121"
        self.capacity = capacity    # max occupancy
        self.room_type = room_type  # "lecture", "lab", "office"
        self.bookings = []          # list of Booking objects

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
