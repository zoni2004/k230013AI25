# A rescue robot is deployed in a grid-based environment to locate and rescue a lost individual. The terrain consists of different types of obstacles:

#'O' → Open paths (traversable).
#'X' → Obstacles (cannot be crossed).
#'P' → Starting position of the robot.
#'T' → Target location where the lost individual is located.
#The robot can move in four directions: Up, Down, Left, and Right.

#Grid Representation:
#O	O	X	O	T
#O	X	O	O	X
#P	O	O	X	O
#X	X	O	O	O
#O	O	O	X	O
#We will implement Breadth-First Search (BFS) to find the shortest path from 'P' to 'T'.

import queue

maze = [
    ['O', 'O', 'X', 'O', 'T'],
    ['O', 'X', 'O', 'O', 'X'],
    ['P', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'X', 'O']
]

directions = [(1,0), (0,-1), (0,1), (-1,0)]

def create_maze(maze):
  graph = {}
  row = len(maze)
  col = len(maze[0])
  player_pos = None
  target_pos = None

  for r in range(row):
    for c in range(col):
      if maze[r][c] in ['O', 'P', 'T'] :
        neighbors = []
        for dr, dc in directions:
          nr = r + dr
          nc = c + dc
          if 0 <= nr < row and 0 <= nc < col and maze[nr][nc] in ['O', 'P', 'T']:
              neighbors.append((nr,nc))
        graph[(r,c)] = neighbors
      if maze[r][c] == 'P':
        player_pos = (r, c)
      if maze[r][c] == 'T':
        target_pos = (r, c)

  return graph, player_pos, target_pos

graph, player_pos, target_pos = create_maze(maze)

print("Graph:", graph)
print("Player Position:", player_pos)
print("Target Position:", target_pos)

class GoalBasedAgent:
  def __init__(self, goal):
    self.goal = goal

  def formulate_goal(self, percept):
    if percept == self.goal:
      return "Goal Reached"
    else:
      return "Searching"

  def act(self, percept, environment):
    goal_status = self.formulate_goal(percept)
    if(goal_status == "Goal Reached"):
      return f"Goal {self.goal} found"
    else:
      return environment.bfs(percept, self.goal)

class Environment:
  def __init__(self, graph):
    self.graph = graph

  def get_percept(self, node):
    return node

  def bfs(self, start, goal):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
      node = queue.pop(0)
      print(f"Visiting {node}")
      if node == goal:
        return f"Goal {goal} found"
      else:
        for neighbor in self.graph[node]:
          if neighbor not in visited:
            visited.append(neighbor)
            queue.append(neighbor)
    return "Goal not found"

def run_agent(agent, environment, start):
  percept = environment.get_percept(start)
  action = agent.act(percept, environment)
  print(action)

start = player_pos
goal = target_pos
agent = GoalBasedAgent(goal)
environment = Environment(graph)
run_agent(agent, environment, start)
