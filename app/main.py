from fastapi import FastAPI, HTTPException
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.exc import SQLAlchemyError
from db.db import database, solutions_table
from utils.n_queens_puzzle import get_n_queens_puzzle_solutions

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/puzzle")
async def get_puzzle_solutions(n: int = 1):
    solutions = get_n_queens_puzzle_solutions(n)
    try:
        query = pg_insert(solutions_table).values(n_queens = n, solutions = solutions)
        query = query.on_conflict_do_nothing(index_elements=['n_queens'])
        await database.execute(query)
    except SQLAlchemyError as e:
        raise HTTPException(Status_code=500, detail=str(e))

    return {"message": "Solutions retrieved", "n": n, "solutions": solutions}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
