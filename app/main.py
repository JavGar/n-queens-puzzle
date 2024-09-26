from fastapi import FastAPI, HTTPException
from sqlalchemy import select, asc
from sqlalchemy.dialects.postgresql import insert as pg_insert
from db.db import database, solutions_table
from utils.n_queens_puzzle import (
    get_n_queens_puzzle_solutions,
    get_n_queens_puzzle_stored_solutions,
)

app = FastAPI()


@app.get("/")
async def read_root():
    try:
        query = select(solutions_table).order_by(solutions_table.c.n_queens)
        results = await database.fetch_all(query)
        return {"message": "All solutions retrieved", "solutions": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/puzzle")
async def get_puzzle_solutions(n: int = 1):
    solutions = await get_n_queens_puzzle_stored_solutions(n)
    if solutions:
        return {"message": "Solutions retrieved", "n": n, "solutions": solutions}

    solutions = get_n_queens_puzzle_solutions(n)
    try:
        query = pg_insert(solutions_table).values(n_queens=n, solutions=solutions)
        query = query.on_conflict_do_nothing(index_elements=["n_queens"])
        await database.execute(query)
    except Exception as e:
        raise HTTPException(Status_code=500, detail=str(e))

    return {"message": "Solutions retrieved", "n": n, "solutions": solutions}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
