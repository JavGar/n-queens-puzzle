from itertools import permutations
from sqlalchemy import select
from db.db import database, solutions_table


def get_n_queens_puzzle_solutions(n):
    solutions = list()
    cols = range(n)
    for vec in permutations(cols):
        if (
            n
            == len(set(vec[i] + i for i in cols))
            == len(set(vec[i] - i for i in cols))
        ):
            solutions.append(vec)

    return solutions


async def get_n_queens_puzzle_stored_solutions(n):
    try:
        query = select(solutions_table).where(solutions_table.c.n_queens == n)
        row = await database.fetch_one(query)
        if row:
            result = dict(row)
            return result
    except Exception as e:
        print(e)
