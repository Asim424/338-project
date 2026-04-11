from campus import CampusGraph
from history import History
from ui_functions import *
import sys

if __name__ == "__main__":
    # Initialize campus with buildings (no rooms)
    campus = CampusGraph()
    with open("campus_graph.txt") as campus_file:
        campus.import_from_file(campus_file)

    # Initialize history
    history = History()

    while True:
        # Main menu
        choice = prompt_menu(["View buildings", "View route history", "View bookings", "Make service request", "Exit"])
        match choice:
            case 1:
                view_buildings(campus, history)
            case 2:
                view_route_history()
            case 3: 
                view_bookings()
            case 4:
                make_service_request()
            case 5:
                sys.exit()

