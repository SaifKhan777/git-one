import random

def initial_board(size):
    return [random.randint(0, size - 1) for _ in range(size)]

def conflicts(board, row, col):
    count = 0
    for i in range(len(board)):
        if i == row:
            continue
        if board[i] == col or abs(i - row) == abs(board[i] - col):
            count += 1
    return count

def min_conflicts(board, max_iterations):
    size = len(board)
    for _ in range(max_iterations):
        conflicts_count = [conflicts(board, row, col) for row, col in enumerate(board)]
        if sum(conflicts_count) == 0:
            return board
        row_to_change = random.choice([i for i, count in enumerate(conflicts_count) if count > 0])
        min_conflicts = [i for i, count in enumerate(conflicts_count) if count == conflicts_count[row_to_change]]
        board[row_to_change] = random.choice(min_conflicts)
    return None

def print_board(board):
    size = len(board)
    for row in range(size):
        line = ""
        for col in range(size):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    board_size = 8
    max_iterations = 100
    initial_state = [0, 4, 7, 5, 2, 6, 1, 3]
    # initial_state = initial_board(board_size)
    solution = min_conflicts(initial_state, max_iterations)

    if solution:
        print("Solution found:")
        print_board(solution)
    else:
        print("No solution found after {} iterations.".format(max_iterations))
