import os
import datetime

from campus import CampusGraph
from service_tickets import TicketQueue
from history import History
from ui_functions import *
from room import Room
import sys

if __name__ == "__main__":
    # Initialize campus with buildings (no rooms)
    campus = CampusGraph()
    base_dir = os.path.dirname(__file__)
    graph_path = os.path.join(base_dir, "campus_graph.txt")

    with open(graph_path) as campus_file:
        campus.import_from_file(campus_file)

    ict_building = campus.lookup_building("ICT")
    if ict_building:
        test_room = Room("ICT-121", 50, "Lab")
        ict_building.insert_room(test_room)
        start = datetime.datetime(2026, 4, 25, 10, 30)
        end = datetime.datetime(2026, 4, 25, 12, 0)
        test_room.add_booking("ENSF 338 Workshop", start, end)

    # Initialize history
    history = History()

    #Initialize RequestQueue
    requests = RequestQueue()

    #Initializa TicketQueue
    tickets = TicketQueue()

    while True:
        # Main menu
        choice = prompt_menu(["View buildings", "View route history", "View bookings", "Make service request", "View request queue", "Make service ticket", "Exit"])
        match choice:
            case 1:
                view_buildings(campus, history)
            case 2:
                view_route_history(history)
            case 3: 
                view_bookings(campus)
            case 4:
                make_service_request(requests)
            case 5:
                view_request_queue(requests)
            case 6:
                make_service_ticket(tickets)
            case 7:
                sys.exit()

