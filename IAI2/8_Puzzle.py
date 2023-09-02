import random

class EightPuzzle:
    def __init__(self, size):
        self.size = size
        self.goal_state = [i for i in range(1, size*size)] + [0]
        self.state = self.shuffle_board()

    def shuffle_board(self):
        board = self.goal_state[:]
        random.shuffle(board)
        return board

    def is_goal(self):
        return self.state == self.goal_state

    def get_neighbors(self):
        neighbors = []
        empty_index = self.state.index(0)
        row, col = divmod(empty_index, self.size)

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                neighbor = self.state[:]
                neighbor[empty_index], neighbor[new_row * self.size + new_col] = (
                    neighbor[new_row * self.size + new_col],
                    neighbor[empty_index],
                )
                neighbors.append(neighbor)

        return neighbors

def heuristic(state):
    return sum(1 for i, j in zip(state, EightPuzzle(3).goal_state) if i != j)

def hill_climbing(puzzle):
    current_state = puzzle.state

    while not puzzle.is_goal():
        neighbors = puzzle.get_neighbors()
        if not neighbors:
            break

        random.shuffle(neighbors)
        current_heuristic = heuristic(current_state)
        best_neighbor = min(neighbors, key=heuristic)

        if heuristic(best_neighbor) >= current_heuristic:
            break

        current_state = best_neighbor

    return current_state

if __name__ == "__main__":
    # Initialize an 8-puzzle with a solvable initial state
    initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    puzzle = EightPuzzle(3)
    puzzle.state = initial_state

    print("Initial state:")
    print(puzzle.state)

    solution = hill_climbing(puzzle)

    if puzzle.is_goal():
        print("Goal state reached:")
        print(solution)
    else:
        print("No solution found.")
