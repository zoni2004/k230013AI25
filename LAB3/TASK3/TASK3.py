#Delivery Route Optimization with Time Windows
#● Description: Using the Greedy Best-First Search, optimize delivery routes for a set of delivery points. Each delivery point has a specific time window for delivery, and the algorithm must prioritize those with stricter deadlines.
#● Challenge: Ensure that the algorithm handles time constraints efficiently while minimizing total travel distance.

import heapq

class DeliveryNode:
    def __init__(self, location, deadline, distance=0):
        self.location = location
        self.deadline = deadline 
        self.distance = distance  

    def __lt__(self, other):
        return self.deadline < other.deadline  

graph = {
    'Warehouse': {'A': 5, 'B': 10},
    'A': {'C': 6, 'D': 8},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 7},
    'D': {'F': 5, 'G': 9},
    'E': {'G': 4},
    'F': {'Destination': 6},
    'G': {'Destination': 3},
    'Destination': {}
}

# lower means higher priority
time_windows = {
    'Warehouse': 20,  
    'A': 8,
    'B': 12,
    'C': 7,
    'D': 9,
    'E': 10,
    'F': 6,
    'G': 11,
    'Destination': 15
}

def greedy_best_first_search(graph, time_windows, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, DeliveryNode(start, time_windows[start]))

    visited = set()
    path = []

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.location in visited:
            continue

        path.append(current_node.location)
        visited.add(current_node.location)

        if current_node.location == goal:
            print(f"Optimized Route: {path}")
            return

        for neighbor, distance in graph[current_node.location].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, DeliveryNode(neighbor, time_windows[neighbor], distance))

    print("No valid route found.")

print("Optimized Delivery Route with Time Windows:\n")
greedy_best_first_search(graph, time_windows, 'Warehouse', 'Destination')

