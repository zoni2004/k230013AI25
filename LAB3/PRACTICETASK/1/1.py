#Modify the graph to add more nodes and test how the algorithm behaves.
from queue import PriorityQueue

graph = {
    'A' : [('B', 5), ('C', 8)],
    'B' : [('C', 5),('D', 10)],
    'C' : [('E', 3)],
    'D' : [('F', 7), ('G', 6)],
    'E' : [('F', 2), ('G', 10)],
    'F' : [],
    'G' : []
}

def best_first_search(graph, start, goal):
  visited = set()
  pq = PriorityQueue()
  pq.put((0, start))

  while not pq.empty():
    cost, node = pq.get()
    if node not in visited:
      print(node, end=' ')
      visited.add(node)
      if node == goal:
        print("\nGoal reached\n")
        return True

      for neighbor, weight in graph[node]:
        pq.put((weight,neighbor))
  print("Goal not reached\n")
  return False

print("BFS path\n")
best_first_search(graph, 'A', 'F')
