from itertools import permutations

def get_n_queens_puzzle_solutions(n):
    solutions = list()
    cols = range(n)
    for vec in permutations(cols):        
        if n == len(set(vec[i]+i for i in cols)) \
            == len(set(vec[i]-i for i in cols)):
            solutions.append(vec)

    return solutions
