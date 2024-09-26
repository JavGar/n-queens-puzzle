import os
import sqlalchemy
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL", "")
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

solutions_table = sqlalchemy.Table(
    "pussle_solutions", metadata, autoload_with=sqlalchemy.create_engine(DATABASE_URL)
)


async def get_n_queens_puzzle_stored_solutions(n):
    try:
        query = sqlalchemy.select(solutions_table).where(solutions_table.c.n_queens == n)
        row = await database.fetch_one(query)
        if row:
            result = dict(row)
            return result
    except Exception as e:
        print(e)
