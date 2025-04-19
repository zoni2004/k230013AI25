import math

class CardNode:
  def __init__(self, cards, is_max_turn = True):
    self.cards = cards
    self.is_max_turn = is_max_turn
    self.best_move = None
    self.minmax_value = None

class MinMaxAgent:
  def __init__(self, depth):
    self.depth = depth

  def formulate_goal(self, node):
    return "Goal reached" if not node.cards else "Continue Playing"

  def act(self, node, environment):
    goal_status = self.formulate_goal(node)
    if goal_status == "Goal reached":
      return f"Minmax value for root node is {node.minmax_value}"
    else:
      return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, node.is_max_turn)

class Environment:
  def __init__(self):
    self.computed_nodes = []

  def get_percept(self, node):
    return node

  def alpha_beta_search(self, node, depth, alpha, beta, maxmizing):
    self.computed_nodes.append(node)

    if depth == 0 or len(node.cards) == 0:
      node.minmax_value = 0
      return 0

    if node.is_max_turn:
      value = -math.inf
      left_value = node.cards[0] + self.alpha_beta_search(CardNode(node.cards[1:], False), depth-1, alpha, beta, False)
      right_value = node.cards[-1] + self.alpha_beta_search(CardNode(node.cards[:-1], False), depth-1, alpha, beta, False)
      value = max(left_value, right_value)
      alpha = max(alpha, value)
      node.best_move = 'left' if left_value >= right_value else 'right'
      node.minmax_value = value
      return value
    else:
      value = math.inf
      left_value = node.cards[0] + self.alpha_beta_search(CardNode(node.cards[1:], False), depth-1, alpha, beta, False)
      right_value = node.cards[-1] + self.alpha_beta_search(CardNode(node.cards[:-1], False), depth-1, alpha, beta, False)
      value = min(left_value, right_value)
      beta = min(beta, value)
      node.best_move = 'left' if left_value <= right_value else 'right'
      node.minmax_value = value
      return value

def simulate_game(cards):
    root = CardNode(cards)
    agent = MinMaxAgent(depth=4)
    environment = Environment()

    current_node = root
    max_score = 0
    min_score = 0
    
    print(f"Initial cards: {cards}")

    while current_node.cards:
        agent.act(current_node, environment)
        
        if current_node.is_max_turn:
          move = current_node.best_move
          if move == 'left':
                picked = current_node.cards[0]
                current_node = CardNode(current_node.cards[1:], False)
          else:
                picked = current_node.cards[-1]
                current_node = CardNode(current_node.cards[:-1], False)
          max_score += picked
          print(f"Max picks {picked} from {move}. Score: {max_score}. Remaining: {current_node.cards}")
        else:
          move = current_node.best_move
          if move == 'left':
                picked = current_node.cards[0]
                current_node = CardNode(current_node.cards[1:], True)
          else:
                picked = current_node.cards[-1]
                current_node = CardNode(current_node.cards[:-1], True)
          min_score += picked
          print(f"Min picks {picked} from {move}. Score: {min_score}. Remaining: {current_node.cards}")
    
    print("\nFinal scores:")
    print(f"Max: {max_score}")
    print(f"Min: {min_score}")
    print(f"Winner: {'Max' if max_score > min_score else 'Min' if min_score > max_score else 'Tie'}")

    print("\nComputed nodes during search:", environment.computed_nodes)
    return max_score, min_score

cards = [4, 10, 6, 2, 9, 5]
simulate_game(cards)
    
