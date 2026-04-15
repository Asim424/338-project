import os

from campus import CampusGraph
from history import History
from ui_functions import *
import sys

if __name__ == "__main__":
    # Initialize campus with buildings (no rooms)
    campus = CampusGraph()
    base_dir = os.path.dirname(__file__)
    graph_path = os.path.join(base_dir, "campus_graph.txt")

    with open(graph_path) as campus_file:
        campus.import_from_file(campus_file)

    # Initialize history
    history = History()

    #Initialize RequestQueue
    requests = RequestQueue()

    while True:
        # Main menu
        choice = prompt_menu(["View buildings", "View route history", "View bookings", "Make service request", "View request queue", "Exit"])
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
                sys.exit()

