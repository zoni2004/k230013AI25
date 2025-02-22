import heapq

# Graph representation: Adjacency list (city: [(neighbor, cost), ...])
romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# Heuristic values (straight-line distance to Bucharest) for Greedy Best-First Search
heuristics = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Timisoara': 329, 'Lugoj': 244,
    'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160, 'Rimnicu Vilcea': 193, 'Fagaras': 178,
    'Pitesti': 98, 'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80, 'Hirsova': 151, 'Eforie': 161,
    'Vaslui': 199, 'Iasi': 226, 'Neamt': 234
}

# Breadth-First Search (BFS)
def bfs(start, goal):
    queue = [(start, [start])]  # (current node, path)
    visited = set()
    
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path, len(path) - 1  # Path and path cost
        
        if node not in visited:
            visited.add(node)
            for neighbor, _ in romania_map.get(node, []):
                queue.append((neighbor, path + [neighbor]))

    return None, float('inf')

# Uniform Cost Search (UCS)
def ucs(start, goal):
    pq = [(0, start, [start])]  # (cost, current node, path)
    visited = set()
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            for neighbor, step_cost in romania_map.get(node, []):
                heapq.heappush(pq, (cost + step_cost, neighbor, path + [neighbor]))

    return None, float('inf')

# Greedy Best-First Search (GBFS)
def greedy_best_first(start, goal):
    pq = [(heuristics[start], start, [start])]  # (heuristic, node, path)
    visited = set()
    
    while pq:
        _, node, path = heapq.heappop(pq)
        if node == goal:
            return path, len(path) - 1  # Path and step count
        
        if node not in visited:
            visited.add(node)
            for neighbor, _ in romania_map.get(node, []):
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [neighbor]))

    return None, float('inf')

# Iterative Deepening Depth-First Search (IDDFS)
def dls(node, goal, depth, path, visited):
    if depth < 0:
        return None
    if node == goal:
        return path
    visited.add(node)
    for neighbor, _ in romania_map.get(node, []):
        if neighbor not in visited:
            new_path = dls(neighbor, goal, depth - 1, path + [neighbor], visited)
            if new_path:
                return new_path
    return None

def iddfs(start, goal):
    depth = 0
    while True:
        visited = set()
        result = dls(start, goal, depth, [start], visited)
        if result:
            return result, len(result) - 1
        depth += 1

# Main Execution and Comparison
def main():
    start = input("Enter start city: ").strip()
    goal = input("Enter goal city: ").strip()
    
    if start not in romania_map or goal not in romania_map:
        print("Invalid cities. Please enter valid names from the Romania map.")
        return
    
    print("\nRunning Algorithms...\n")
    
    bfs_path, bfs_cost = bfs(start, goal)
    ucs_path, ucs_cost = ucs(start, goal)
    gbfs_path, gbfs_cost = greedy_best_first(start, goal)
    iddfs_path, iddfs_cost = iddfs(start, goal)
    
    results = [
        ("BFS", bfs_path, bfs_cost),
        ("UCS", ucs_path, ucs_cost),
        ("GBFS", gbfs_path, gbfs_cost),
        ("IDDFS", iddfs_path, iddfs_cost)
    ]

    results.sort(key=lambda x: x[2])  # Sort by path cost
    
    for algo, path, cost in results:
        print(f"{algo}: Path: {' -> '.join(path)}, Cost: {cost}")

if __name__ == "__main__":
    main()
