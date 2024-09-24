import pytest
from n_queens_puzzle import get_n_queens_puzzle_solutions

def test_get_n_queens_puzzle_solutions():
    assert len(get_n_queens_puzzle_solutions(1)) == 1
    assert len(get_n_queens_puzzle_solutions(2)) == 0
    assert len(get_n_queens_puzzle_solutions(3)) == 0
    assert len(get_n_queens_puzzle_solutions(4)) == 2
    assert len(get_n_queens_puzzle_solutions(5)) == 10
    assert len(get_n_queens_puzzle_solutions(6)) == 4
    assert len(get_n_queens_puzzle_solutions(7)) == 40
    assert len(get_n_queens_puzzle_solutions(8)) == 92
    assert len(get_n_queens_puzzle_solutions(9)) == 352
    assert len(get_n_queens_puzzle_solutions(10)) == 724
