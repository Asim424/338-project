from math import inf
from building import *
from data_structures import PriorityQueue


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
        
        return cur_dist, pred










