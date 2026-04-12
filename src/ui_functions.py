from request_processor import RequestQueue

def print_separator():
    print(f"\n{"-" * 79}\n")

def format_cell(text, width):
    text = str(text)
    if len(text) > width:
        text = text[:width - 3] + "..."
    return f"{text:<{width+3}}"

def format_row(items, width):
    row = ""

    for item in items:
        row += format_cell(item, width)
    
    return row

def get_int(string = "", minimum = None, maximum = None):
    # Sets the input range to between minimum and maximum values, inclusive of both. Only runs if applicable.
    if (minimum != None) and (maximum != None):
        input_range = list(range(minimum, maximum + 1))
    else:
        input_range = None
    
    # Loops until a valid integer within the input range is selected.
    while True:
        try:
            # Case for if the user wants a range of numbers.
            if input_range is not None:
                # The user is asked to enter a choice from a menu.
                user_input = int(input(f"{string}: "))

                # Prevents invalid inputs from being entered.
                if user_input not in input_range:
                    raise RuntimeError
            
            else:
                user_input = int(input(f"{string}"))

            # Breaks to the return statement if the input is valid.
            break
        except RuntimeError:
            print(f"You must enter a number from {minimum} to {maximum}. Please try again.")
        except ValueError:
            print(f"You must enter your choice as an integer, such as \"1\". Please try again.")

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
        
        choice = prompt_menu(["Find shortest route between buildings", "Lookup room by id", "Exit"])

        print()
        match choice:
            case 1:
                while True:
                    id1 = input("Enter the id of the starting point: ")

                    if campus.lookup_building(id1) is None:
                        print("Invalid building id. Please try again.")
                        continue

                    break

                while True:
                    id2 = input("Enter the id of the end point: ")

                    if campus.lookup_building(id2) is None:
                        print("Invalid building id. Please try again.")
                        continue

                    break

                route, dist = campus.find_shortest_path(id1, id2)
                history.add(campus.lookup_building(id1), campus.lookup_building(id2), route, dist)

                print(f"\nThe shortest route, with a total walking time of {dist} minutes is: ")
                while not route.is_empty():
                    building = route.pop()
                    
                    if route.is_empty():
                        end = "\n"
                    else:
                        end = " -> "

                    print(f"{building.building_id} ({building.name})", end=end)

                input("\nPress enter to continue.")
                    
            case 2:
                pass

            case 3:
                return

def view_route_history():
    pass

def view_bookings():
    pass

def make_service_request(requests:RequestQueue):
    while True:
        print_separator()
        choice = prompt_menu(["Create new request", "Get next Request", "exit"])

        print()

        match choice:
            case 1:
                request = input("Enter request: ")
                if not request.strip():
                    print("No request was given. Exiting create request.")
                    break
                else:
                    requests.enqueue(request)
                    print("Request is now queued")

                    input("\nPress enter to continue.")
            case 2:
                request = requests.dequeue()
                if isinstance(request, IndexError):
                    print("There are no requests in the queue")
                else:
                    print("The request is:")
                    print(f'"{request}"')

                input("\nPress enter to continue.")

            case 3:
                return
                


            

