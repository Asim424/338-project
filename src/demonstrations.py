from campus import CampusGraph
from building import Building
from room import Room
from ui_functions import prompt_menu

import sys
from random import randint
from timeit import timeit
from matplotlib import pyplot as plt

def building_lookup_demonstration():
    num_buildings = 1000

    campus = CampusGraph()

    ids = [str(i) for i in range(num_buildings)]

    insert_time_data = {}
    lookup_time_data = {}

    i = 1
    for id in ids:
        building = Building(id, f"Name{id}", (0, 0))

        time = timeit(lambda : campus.insert_building(building), number=100) / 100 * 1_000_000_000
        insert_time_data[i] = time

        rand_id = ids[randint(0, i)]

        time = timeit(lambda : campus.lookup_building(rand_id), number=100) / 100 * 1_000_000_000
        lookup_time_data[i] = time

        i += 1

    # Plot
    plt.figure()

    x = [iter for iter in insert_time_data.keys()];
    y = [insert_time_data[iter] for iter in x]
    plt.plot(x, y)

    x = [iter for iter in lookup_time_data.keys()];
    y = [lookup_time_data[iter] for iter in x]
    plt.plot(x, y)

    plt.title("Operation Time Based on Campus Size")
    plt.xlabel("Number of Buildings")
    plt.ylabel("Time (ns)")
    plt.grid(color="grey", linestyle='-', linewidth=1, alpha=0.5)
    plt.legend(["Insert", "Lookup"])

    plt.show()

def room_lookup_demonstration():
    num_rooms = 1000

    building = Building("ID", "Name", (0, 0))

    ids = [str(i) for i in range(num_rooms)]

    time_data = {}

    i = 1
    for id in ids:
        building.insert_room(Room(id, 0, f"Type{id}"))
        rand_id = ids[randint(0, i)]

        time = timeit(lambda : building.lookup_room(rand_id), number=100) / 100 * 1_000_000_000
        time_data[i] = time

        i += 1

    # Plot
    plt.figure()
    x = [iter for iter in time_data.keys()];
    y = [time_data[iter] for iter in x]
    plt.plot(x, y)

    plt.title("Room Lookup Time Based on Building Size")
    plt.xlabel("Number of Rooms")
    plt.ylabel("Time (ns)")
    plt.grid(color="grey", linestyle='-', linewidth=1, alpha=0.5)

    plt.show()

if __name__ == "__main__":
    while True:
        # Main menu
        choice = prompt_menu(["Building lookup demo", "Room lookup demo", "Exit"])
        match choice:
            case 1:
                building_lookup_demonstration()
            case 2:
                room_lookup_demonstration()
            case 3:
                sys.exit()
