from math import inf
from building import *
from data_structures import PriorityQueue, Stack
from ui_functions import format_row


class PathwayEdge:
    def __init__(self, dest: Building, weight: int):
        self.dest = dest
        self.weight = weight
        self.next = None

class BuildingNode:
    def __init__(self, data: Building):
        self.data = data
        self.edges_head = None

    def add_pathway(self, node, weight):
        edge = PathwayEdge(node, weight)
        edge.next = self.edges_head
        self.edges_head = edge

    def remove_pathway(self, node):
        if self.edges_head is None:
            return
        if self.edges_head.dest is node:
            tmp = self.edges_head
            self.edges_head = self.edges_head.next
            tmp.next = None
            return

        prev = self.edges_head
        cur = self.edges_head.next
        while cur is not None:
            if cur.dest is node:
                prev.next = cur.next
                cur.next = None
                return
            prev = cur
            cur = cur.next

class CampusGraph:
    def __init__(self):
        self.building_nodes = {}

    def insert_building(self, building: Building):
        node = BuildingNode(building)
        self.building_nodes[building.building_id] = node
        return node

    def remove_building(self, building_id: str):
        if building_id not in self.building_nodes:
            raise KeyError(f"Building {building_id} not found")

        node = self.building_nodes[building_id]
        for n in self.building_nodes.values():
            if n is not node:
                n.remove_pathway(node)
        del self.building_nodes[node.data.building_id]

    def add_pathway(self, id1: str, id2: str, weight: int):
        if id1 not in self.building_nodes:
            raise KeyError(f"Building {id1} not found")
        if id2 not in self.building_nodes:
            raise KeyError(f"Building {id2} not found")

        n1 = self.building_nodes[id1]
        n2 = self.building_nodes[id2]

        n1.add_pathway(n2, weight)
        n2.add_pathway(n1, weight)

    def remove_pathway(self, id1: str, id2: str):
        if id1 not in self.building_nodes:
            raise KeyError(f"Building {id1} not found")
        if id2 not in self.building_nodes:
            raise KeyError(f"Building {id2} not found")

        n1 = self.building_nodes[id1]
        n2 = self.building_nodes[id2]

        n1.remove_pathway(n2)
        n2.remove_pathway(n1)

    def lookup_building(self, building_id: str):
        if building_id not in self.building_nodes:
            return None

        return self.building_nodes[building_id].data

    def find_shortest_path(self, from_id: str, to_id: str):
        if from_id not in self.building_nodes:
            raise KeyError(f"Building {from_id} not found")
        if to_id not in self.building_nodes:
            raise KeyError(f"Building {to_id} not found")

        from_node = self.building_nodes[from_id]
        to_node = self.building_nodes[to_id]

        cur_dist = {}
        pred = {}
        visited = set()

        # Set initial state
        for node in self.building_nodes.values():
            cur_dist[node] = inf
            pred[node] = None
        cur_dist[from_node] = 0

        min_heap = PriorityQueue()
        # Create priority queue
        for node in self.building_nodes.values():
            min_heap.enqueue(node, cur_dist[node])
            
        # Main loop
        while len(visited) < len(self.building_nodes):
            dist, n = min_heap.dequeue()
            if dist > cur_dist[n]:
                continue;
            visited.add(n)
            
            edge = n.edges_head
            while edge is not None:
                temp_dist = cur_dist[n] + edge.weight
                if temp_dist < cur_dist[edge.dest]:
                    cur_dist[edge.dest] = temp_dist
                    pred[edge.dest] = n
                    min_heap.enqueue(edge.dest, temp_dist)

                edge = edge.next

        # Create a route stack object from the pred dictionary
        route = Stack()
        cur = self.building_nodes[to_id]
        while cur is not None:
            route.push(cur.data)
            cur = pred[cur]

        return route, cur_dist[self.building_nodes[to_id]]

    def import_from_file(self, file):
        self.building_nodes = {}

        lines = file.readlines()

        # Nodes
        while lines: 
            line = lines.pop(0).strip()
            if len(line) == 0:
                break
            if line == "===":
                break

            tokens = line.split("--")

            id = tokens[0]
            if id in self.building_nodes:
                raise RuntimeError(f"Cannot create two buildings with the same id: {line}")

            name = tokens[1]

            try:
                location = (float(tokens[2]), float(tokens[3]))
            except:
                raise ValueError(f"Building location attributes must be floating-point numbers: {line}")
            
            self.insert_building(Building(id, name, location))

        # Edges
        while lines:
            line = lines.pop(0).strip()

            tokens = line.split("--")

            id1 = tokens[0]
            if id1 not in self.building_nodes:
                raise RuntimeError(f"{id1} not found in buildings: {line}")

            id2 = tokens[1]
            if id2 not in self.building_nodes:
                raise RuntimeError(f"{id2} not found in buildings: {line}")
            
            try:
                weight = int(tokens[2])
            except:
                raise ValueError(f"Weight parameter must be an integer: {line}")

            self.add_pathway(id1, id2, weight)

    def print_table(self):
        headers = ["ID", "Name", "Latitude", "Longitude"]
        cell_width = 16

        # Header
        header_row = format_row(headers, cell_width)
        print(header_row)
        print("-" * len(header_row))

        # Building rows
        for node in self.building_nodes.values():
            building = node.data
            print(format_row([building.building_id, building.name, building.location[0], building.location[1]], cell_width))
            





if __name__ == "__main__":
    campus = CampusGraph()
    with open("campus_graph.txt") as file:
        campus.import_from_file(file)

    route, dist = campus.find_shortest_path("Id1", "Id4")
    print(route)







