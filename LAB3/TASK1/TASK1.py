#Enhanced Maze Navigation with Multiple Goals
#● Description: Modify the given Best-First Search to find a path through a maze with multiple goal points. The algorithm should visit all goal points and return the shortest path covering all goals.
#● Challenge: The maze will have several dead ends and multiple goal points at different locations.

from queue import PriorityQueue

class Node:
  def __init__(self, position, parent = None):
    self.position = position
    self.parent = parent
    self.g = 0
    self.h = 0
    self.f = 0

  def __lt__(self, other):
    return self.f < other.f

def heuristic(current_pos, end_pos):
  return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])

def best_first_search(maze, start, end):
  rows, cols = len(maze), len(maze[0])
  start_node = Node(start)
  frontier = PriorityQueue()
  frontier.put(start_node)
  visited = set()

  while not frontier.empty():
    current_node = frontier.get()
    current_pos = current_node.position

    if current_pos == end:
      path = []
      while current_node:
        path.append(current_node.position)
        current_node = current_node.parent
      return path[::-1]

    visited.add(current_pos)

    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
      new_pos = (current_pos[0] + dx, current_pos[1] + dy)
      if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
        new_node = Node(new_pos, current_node)
        new_node.g = current_node.g + 1
        new_node.h = heuristic(new_node.position, end)
        new_node.f = new_node.h
        frontier.put(new_node)
        visited.add(new_pos)

  return None

maze = [
    [0 ,0 ,1 ,0 ,0],
    [0 ,0 ,0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0,0)
ends = [(3,0), (4,4), (4,2)]

for end in ends:
  path = best_first_search(maze, start, end)
  if path:
    print(f"Path from {start} to {end}: {path}")
  else:
    print(f"No path found from {start} to {end}")
