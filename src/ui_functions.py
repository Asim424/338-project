from request_processor import RequestQueue
from service_tickets import TicketQueue
from building import Building
from room import Room

def print_separator():
    print(f"\n{'-' * 79}\n")

def get_int(string = "", minimum = None, maximum = None):
    if (minimum != None) and (maximum != None):
        check_range = True
    else:
        check_range = False

    # Loops until a valid integer within the input range is selected.
    while True:
        try:
            user_input = int(input(f"{string}: "))

            # Prevents invalid inputs from being entered.
            if check_range and (user_input < minimum or user_input > maximum):
                raise RuntimeError
            
            # Breaks to the return statement if the input is valid.
            break
        except RuntimeError:
            print(f"You must enter a number from {minimum} to {maximum}. Please try again.")
        except ValueError:
            print(f"You must enter your choice as an integer, such as \"1\". Please try again.")

    return user_input

def get_float(string = "", minimum = None, maximum = None):
    if (minimum != None) and (maximum != None):
        check_range = True
    else:
        check_range = False

    # Loops until a valid float within the input range is selected.
    while True:
        try:
            user_input = float(input(f"{string}: "))

            # Prevents invalid inputs from being entered.
            if check_range and (user_input < minimum or user_input > maximum):
                raise RuntimeError
            
            # Breaks to the return statement if the input is valid.
            break
        except RuntimeError:
            print(f"You must enter a number from {minimum} to {maximum}. Please try again.")
        except ValueError:
            print(f"You must enter your choice as an floating point number, such as \"3.5\". Please try again.")

    return user_input

def prompt_menu(options):
    print_separator(); 

    print("Choose one of the following operations:"); 

    for i, opt in enumerate(options):
      print(f"\t{i + 1}. {opt}");
    

    choice = get_int("Enter your choice by number", 1, len(options))

    return choice

def view_buildings(campus, history):
    while True:
        print_separator()
        campus.print_table()
        
        choice = prompt_menu(["Find shortest route between buildings", "Lookup building by id", "Add building", "Exit"])

        print()
        match choice:
            # Find shortest route
            case 1:
                while True:
                    id1 = input("Enter the id of the starting point: ").upper()

                    if campus.lookup_building(id1) is None:
                        print("Invalid building id. Please try again.")
                        continue

                    break

                while True:
                    id2 = input("Enter the id of the end point: ").upper()

                    if campus.lookup_building(id2) is None:
                        print("Invalid building id. Please try again.")
                        continue

                    break

                route, dist = campus.find_shortest_path(id1, id2)
                history.add(campus.lookup_building(id1), campus.lookup_building(id2), route, dist)

                print(f"\nThe shortest route, with a total walking time of {round(dist, 2)} minutes is: ")
                while not route.is_empty():
                    building = route.pop()
                    
                    if route.is_empty():
                        end = "\n"
                    else:
                        end = " -> "

                    print(f"{building.building_id} ({building.name})", end=end)

                input("\nPress enter to continue.")
            
            # Building lookup
            case 2:
                id = input("Enter the id of the building: ").upper()
                building = campus.lookup_building(id)
                
                if building is None:
                    print(f"\nNo building found with id {id}")
                    
                else:
                    select_building(campus, building)

                input("\nPress enter to continue.")
                
            # Add building
            case 3:
                id = input("Enter the building id: ").upper()
                name = input("Enter the building name: ")
                latitude = get_float("Enter the latitude", -90, 90)
                longitude = get_float("Enter the longitude", -180, 180)

                campus.insert_building(Building(id, name, (latitude, longitude)))

                print("\nBuilding added.")

                input ("\nPress enter to continue.")


            # Exit
            case 4:
               return 


def select_building(campus, building):
    print_separator()
        
    choice = prompt_menu(["View rooms", "Add pathway" ,f"Remove building {building.building_id}", "Exit"])

    print()
    match choice:
        # View rooms
        case 1:
            view_rooms(building)

        # Add pathway
        case 2:
            print_separator()
            campus.print_table()

            id = input("\nEnter the id of the connecting building: ").upper()
            weight = get_float("Enter the pathway walking time, in minutes", 0, 20)

            if campus.lookup_building(id) is None:
                print(f"\nNo building found with id {id}")

            else:
                campus.add_pathway(building.building_id, id, weight) 
                print("\nPathway added.")


        # Remove building
        case 3:
            campus.remove_building(building.building_id) 
            
            print(f"Building removed.")

        # Exit
        case 4:
            return

def view_rooms(building):
    while True:
        print_separator()
        building.print_room_table()
        
        choice = prompt_menu(["Lookup room by id", "Add room", "Exit"])

        print()
        match choice:
            # Room lookup
            case 1:
                id = input("Enter the id of the room: ").upper()
                room = building.lookup_room(id)
                
                if room is None:
                    print(f"\nNo room found with id {id}")
                    
                else:
                    select_room(building, room)

                input("\nPress enter to continue.")
                
            # Add room
            case 2:
                id = input("Enter the room id: ").upper()
                capacity = get_int("Enter the room capacity")
                room_type = input("Enter the room type: ")

                building.insert_room(Room(id, capacity, room_type))

                print("\nRoom added.")

                input ("\nPress enter to continue.")

            # Exit
            case 3:
               return

def select_room(building, room):
    print_separator()
        
    choice = prompt_menu([f"Remove room {room.room_id}", "Exit"])

    print()
    match choice:
        # Remove room
        case 1:
            building.remove_room(room.room_id) 
            
            print(f"Room removed.")

        # Exit
        case 2:
            return

def view_route_history(history):
    while True:
        print_separator()
        if history.is_empty():
            print("Navigation history is empty. No previous routes available.")
            input("\nPress enter to return to the main menu.")
            return

        current = history.peek()
        print(f"Current System State: Last navigated to {current.destination.building_id} from {current.origin.building_id}.")
        print(f"Stored History States: {len(history._stack)}")
        
        choice = prompt_menu(["Undo last route", "Exit"])

        print()
        match choice:
            case 1:
                removed = history.undo()
                print(f"Action: Reverted navigation query from {removed.origin.building_id} to {removed.destination.building_id}.")
                
                if not history.is_empty():
                    new_top = history.peek()
                    print(f"System State Restored. Previous destination: {new_top.destination.building_id}")
                else:
                    print("System State Restored. History is now empty.")
                
                input("\nPress enter to continue.")
            case 2:
                return

def view_bookings():
    pass

def make_service_request(requests:RequestQueue):
    priority_levels = ["Emergency", "Standard", "Low"]

    while True:
        print_separator()
        choice = prompt_menu(["Create new request", "Get next Request", "Exit"])

        print()

        match choice:
            case 1:
                request = input("Enter request: ")
                if not request.strip():
                    print("No request was given. Exiting create request.")
                    break

                print_separator()
                print("Select request priority:")
                for idx, priority in enumerate(priority_levels, start=1):
                    print(f"\t{idx}. {priority}")
                priority_choice = get_int("Enter priority by number", 1, len(priority_levels))
                priority_label = priority_levels[priority_choice - 1]

                requests.enqueue(request, priority_label)
                print(f"Request queued with {priority_label} priority.")
                input("\nPress enter to continue.")

            case 2:
                request = requests.dequeue()
                if request is None:
                    print("There are no requests in the queue")
                else:
                    print("Now serving the highest-priority request:")
                    print(f"Priority: {request['priority']}")
                    print(f"Request: {request['description']}")

                input("\nPress enter to continue.")

            case 3:
                return
                
def view_request_queue(requests:RequestQueue):
    ## displays requests and their urgency levels in the queue, from most to least urgent
    print_separator()
    if requests.is_empty():
        print("The request queue is empty. No requests to display.")
    else:
        print("Current Request Queue (from most to least urgent):")
        for i, request in enumerate(requests.get_all_requests(), start=1):
            print(f"{i}. [{request['priority']}] {request['description']}")

            
def make_service_ticket(tickets:TicketQueue):
    while (True):
        print_separator()
        
        choice = prompt_menu([f"Queue new ticket", "Dequeue ticket", "Exit"])

        print()
        match choice:
            # Remove room
            case 1:
                ticket = input("Enter ticket: ")
                if not ticket.strip():
                    print("No ticket was given. Exiting queue ticket.")
                    break

                tickets.enqueue(ticket)
                
                print(f"Ticket \"{ticket}\" queued.")

            case 2:
                ticket = tickets.dequeue()
                if ticket is None:
                    print("There are no tickets in the queue")

                else:
                    print(f"Ticket: \"{ticket}\"")

                input("\nPress enter to continue.")

            # Exit
            case 3:
                return
    