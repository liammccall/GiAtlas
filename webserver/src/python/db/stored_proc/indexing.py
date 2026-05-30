from sqlalchemy import Engine, select, func
import pandas as pd
from sqlalchemy.orm import Session

from src.python.db.entities.index import ShapeIndex

def update_shape_index(engine: Engine, table_name : str, desc : str) -> bool:
    with engine.begin() as conn:
        statement = select(
            func.app_index.update_index(table_name, desc)
        )
        conn.execute(statement)
        
def get_shape_index(engine: Engine) -> pd.DataFrame:
    session = Session(engine)
    statement = select(ShapeIndex)
    return session.scalars(statement)