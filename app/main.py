from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import select, asc
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.exc import DBAPIError, OperationalError, SQLAlchemyError
from .db.db import database, get_n_queens_puzzle_stored_solutions, solutions_table
from .utils.n_queens_puzzle import get_n_queens_puzzle_solutions

app = FastAPI(
    title="N-Queens Puzzle Solver",
    description="API to solve the N-Queens Puzzle using FastAPI.",
    version="1.0.0",
)


@app.get("/")
async def get_solutions():
    """
    Retrieve all stored N-Queens solutions from the database.

    Returns:
        message: response message
        solutions: list of all N-Queens solutions.
    """
    try:
        query = select(solutions_table).order_by(solutions_table.c.n_queens)
        results = await database.fetch_all(query)
        return {"message": "All solutions retrieved", "solutions": results}
    except OperationalError as e:
        raise HTTPException(
            status_code=503, detail="Database is not available: " + str(e)
        )
    except DBAPIError as e:
        raise HTTPException(status_code=500, detail="Database error: " + str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="SQLAlchemy error: " + str(e))


@app.get("/puzzle")
async def get_puzzle_solutions(
    n: int = Query(1, description="The size of the N-Queens board")
):
    """
    Get solution for a specific N-Queens board size.

    Args:
        n: The size of the N-Queens board.

    Returns:
        message: response message
        n: board size
        solutions: list of all N-Queens solutions.
    """
    solutions = await get_n_queens_puzzle_stored_solutions(n)
    if solutions:
        return {"message": "Solutions retrieved", "n": n, "solutions": solutions}

    solutions = get_n_queens_puzzle_solutions(n)
    try:
        query = pg_insert(solutions_table).values(n_queens=n, solutions=solutions)
        query = query.on_conflict_do_nothing(index_elements=["n_queens"])
        await database.execute(query)
    except OperationalError as e:
        raise HTTPException(
            status_code=503, detail="Database is not available: " + str(e)
        )
    except DBAPIError as e:
        raise HTTPException(status_code=500, detail="Database error: " + str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="SQLAlchemy error: " + str(e))

    return {"message": "Solutions retrieved", "n": n, "solutions": solutions}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
