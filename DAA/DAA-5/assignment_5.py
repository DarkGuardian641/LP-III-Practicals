# 8-Queens Problem using Backtracking
# One Queen is already placed at position (0, 0)

N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print("\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False

    return True

def solve(board, row=1):
    # Base case: all queens placed
    if row == N:
        print("Final 8-Queens Solution:\n")
        print_board(board)
        return True

    # Try placing queen in each column for the current row
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0  # Backtrack

    return False

# Initialize board with all 0s
board = [[0] * N for _ in range(N)]

# Pre-place first Queen
board[0][0] = 1

print("Starting with first Queen at (0, 0):\n")
print_board(board)

# Solve for remaining Queens
if not solve(board):
    print("No solution found!")