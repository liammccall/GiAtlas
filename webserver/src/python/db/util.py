import geopandas as gpd
from sqlalchemy import create_engine

import src.python.db.stored_proc.indexing as indexing

engine = create_engine("postgresql://username:password@db:5432/gidb")

def run_query(query : str) -> gpd.GeoDataFrame:
    data = gpd.read_postgis(query, engine, geom_col="geometry")
    return data
    

def save_gis(data: gpd.GeoDataFrame, to_name: str, desc: str = ""):
    data.to_postgis(to_name, engine, if_exists='replace')
    indexing.update_shape_index(engine, to_name, desc)
    print(indexing.get_shape_index())