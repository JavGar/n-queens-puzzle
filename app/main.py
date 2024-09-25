from fastapi import FastAPI
from utils.n_queens_puzzle import get_n_queens_puzzle_solutions

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/puzzle")
async def get_puzzle_solutions(n: int = 1):
    return {"message": "Solutions retrieved", "n": n, "solutions": get_n_queens_puzzle_solutions(n)}
