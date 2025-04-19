import math

class GameState:
    def __init__(self, board, is_white_turn):
        self.board = board
        self.is_white_turn = is_white_turn
        self.children = []
        self.minimax_value = None
        self.move = None 

    def get_possible_moves(self):
        return self.children

    def is_terminal(self):
        return len(self.children) == 0

    def evaluate(self):
        white_count = sum(row.count('W') for row in self.board)
        black_count = sum(row.count('B') for row in self.board)
        return white_count - black_count if self.is_white_turn else black_count - white_count

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, state):
        return state.minimax_value is not None

    def act(self, state, environment):
        if self.formulate_goal(state):
            return f"Goal already reached: {state.minimax_value}"
        else:
            best_value, best_move = environment.alpha_beta(state, self.depth, -math.inf, math.inf, state.is_white_turn)
            state.minimax_value = best_value
            return f"Minimax value of root: {best_value}"

class Environment:
    def __init__(self):
        self.computed_states = []
        self.pruned_states = []

    def alpha_beta(self, state, depth, alpha, beta, maximizing):
        self.computed_states.append(state)

        if depth == 0 or state.is_terminal():
            value = state.evaluate()
            state.minimax_value = value
            return value, state.move

        best_move = None

        if maximizing:
            value = -math.inf
            for child in state.get_possible_moves():
                val, _ = self.alpha_beta(child, depth - 1, alpha, beta, False)
                if val > value:
                    value = val
                    best_move = child.move
                alpha = max(alpha, value)
                if beta <= alpha:
                    self.pruned_states.append(child)
                    break
        else:
            value = math.inf
            for child in state.get_possible_moves():
                val, _ = self.alpha_beta(child, depth - 1, alpha, beta, True)
                if val < value:
                    value = val
                    best_move = child.move
                beta = min(beta, value)
                if beta <= alpha:
                    self.pruned_states.append(child)
                    break

        state.minimax_value = value
        return value, best_move

def create_sample_board():
    return [
        ['.', 'B', '.', 'B', '.', 'B', '.', 'B'],
        ['B', '.', 'B', '.', 'B', '.', 'B', '.'],
        ['.', 'B', '.', 'B', '.', 'B', '.', 'B'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['W', '.', 'W', '.', 'W', '.', 'W', '.'],
        ['.', 'W', '.', 'W', '.', 'W', '.', 'W'],
        ['W', '.', 'W', '.', 'W', '.', 'W', '.'],
    ]

def run_checkers_minimax():
    board = create_sample_board()
    root_state = GameState(board, is_white_turn=False)

    move_descriptions = [
        ((5, 6), (4, 5), False),  
        ((2, 3), (3, 4), False),  
        ((6, 7), (5, 6), False), 
        ((3, 4), (5, 6), True),  
    ]

    for i, (src, dst, is_capture) in enumerate(move_descriptions):
        child = GameState(create_sample_board(), is_white_turn=(i % 2 == 0))
        child.move = (src, dst, is_capture)
        root_state.children.append(child)

    env = Environment()
    agent = MinimaxAgent(depth=2)

    result = agent.act(root_state, env)
    print(result)
    print("States computed:", len(env.computed_states))
    print("States pruned:", len(env.pruned_states))
    print("Minimax Value:", root_state.minimax_value)

    print("\nMove History:")
    for idx, child in enumerate(root_state.children):
        player = "AI" if idx % 2 == 0 else "Player"
        src, dst, is_capture = child.move
        move_str = f"{player} moves: {src} → {dst}"
        if is_capture:
            move_str += " [Capture!]"
        print(move_str)

run_checkers_minimax()
