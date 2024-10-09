import pytest

from app.utils.n_queens_puzzle import get_n_queens_puzzle_solutions, is_valid


def test_diagonal_left_conflict():
    board = [1, -1, -1, -1]
    assert not is_valid(board, 1, 0)
    board = [1, 3, -1, -1, -1, -1]
    assert not is_valid(board, 2, 2)


def test_same_column_conflict():
    board = [1, -1, -1, -1]
    assert not is_valid(board, 1, 1)
    board = [1, 3, -1, -1, -1, -1]
    assert not is_valid(board, 4, 1)


def test_diagonal_rigth_conflict():
    board = [1, -1, -1, -1]
    assert not is_valid(board, 1, 2)
    board = [1, 3, -1, -1, -1, -1]
    assert not is_valid(board, 2, 3)


def test_valid_position():
    board = [1, 3, 0, -1]
    assert is_valid(board, 3, 2)


def test_get_n_queens_puzzle_solutions():
    assert len(list(get_n_queens_puzzle_solutions(1))) == 1
    assert len(list(get_n_queens_puzzle_solutions(2))) == 0
    assert len(list(get_n_queens_puzzle_solutions(3))) == 0
    assert len(list(get_n_queens_puzzle_solutions(4))) == 2
    assert len(list(get_n_queens_puzzle_solutions(5))) == 10
    assert len(list(get_n_queens_puzzle_solutions(6))) == 4
    assert len(list(get_n_queens_puzzle_solutions(7))) == 40
    assert len(list(get_n_queens_puzzle_solutions(8))) == 92
    assert len(list(get_n_queens_puzzle_solutions(9))) == 352
    assert len(list(get_n_queens_puzzle_solutions(10))) == 724
