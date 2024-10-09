def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or row - i == abs(col - board[i]):
            return False
    return True


def solve_n_queens_(board, row):
    if row == len(board):
        yield list(board)
    else:
        for col in range(len(board)):
            if is_valid(board, row, col):
                board[row] = col
                yield from solve_n_queens_(board, row + 1)
                board[row] = -1


def get_n_queens_puzzle_solutions(n):
    board = [-1] * n
    yield from solve_n_queens_(board, 0)
