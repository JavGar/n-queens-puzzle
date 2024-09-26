import os
import sqlalchemy
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL", "")
database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

solutions_table = sqlalchemy.Table(
    "pussle_solutions", metadata, autoload_with=sqlalchemy.create_engine(DATABASE_URL)
)
