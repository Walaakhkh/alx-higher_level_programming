#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row, solutions):
    """Solve N-Queens problem using backtracking."""
    if row >= len(board):
        solution = []
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == 1:
                    solution.append([r, c])
        solutions.append(solution)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1, solutions)
            board[row][col] = 0

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
