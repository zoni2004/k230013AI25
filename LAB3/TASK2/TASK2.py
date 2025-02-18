import heapq
import random
import time
import threading

# Graph with initial edge costs
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

# Heuristic values (Manhattan or straight-line distance)
heuristic = {
    'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 7,
    'F': 3, 'G': 6, 'H': 2, 'I': 0
}

# Lock for thread-safe updates
graph_lock = threading.Lock()

def random_cost_updates():
    """Dynamically updates edge costs at random intervals."""
    while True:
        with graph_lock:
            node = random.choice(list(graph.keys()))
            if graph[node]:  # Ensure the node has neighbors
                neighbor = random.choice(list(graph[node].keys()))
                new_cost = random.randint(1, 10)  # Assign a new random cost
                graph[node][neighbor] = new_cost
                print(f"\n[Edge Update] Cost from {node} to {neighbor} updated to {new_cost}")
        time.sleep(random.randint(2, 5))  # Update interval

def a_star_dynamic(graph, start, goal):
    """A* Search that dynamically adjusts to edge cost changes."""
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], 0, start, None))  # (f-cost, g-cost, node, parent)
    
    g_costs = {start: 0}
    came_from = {start: None}
    
    visited = set()

    while priority_queue:
        _, current_g, current_node, parent = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        came_from[current_node] = parent

        print(current_node, end=" ")  # Print the traversal order

        if current_node == goal:
            # Reconstruct path
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nPath found: {path}")
            return

        with graph_lock:
            for neighbor, cost in graph[current_node].items():
                new_g = current_g + cost
                f_cost = new_g + heuristic[neighbor]

                if neighbor not in g_costs or new_g < g_costs[neighbor]:
                    g_costs[neighbor] = new_g
                    heapq.heappush(priority_queue, (f_cost, new_g, neighbor, current_node))

    print("\nNo path found")

# Start random cost updates in a separate thread
threading.Thread(target=random_cost_updates, daemon=True).start()

# Run the dynamic A* search
print("A* path with dynamic edge costs:\n")
a_star_dynamic(graph, 'A', 'I')
