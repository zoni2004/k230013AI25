#Enhanced Maze Navigation with Multiple Goals
#● Description: Modify the given Best-First Search to find a path through a maze with multiple goal points. The algorithm should visit all goal points and return the shortest path covering all goals.
#● Challenge: The maze will have several dead ends and multiple goal points at different locations.

from queue import PriorityQueue

class Node:
  def __init__(self, position, parent = None):
    


