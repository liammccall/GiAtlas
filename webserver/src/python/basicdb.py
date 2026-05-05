from pathlib import Path

import geopandas as gpd
from sqlalchemy import create_engine

PROJECT_ROOT = Path(__file__).resolve().parents[2]

data_dir = PROJECT_ROOT / "data"
def save_file(name : str):
    data = gpd.read_file(data_dir / f"ne_50m_{name}/ne_50m_{name}.shp")
    engine = create_engine("postgresql://username:password@db:5432/gidb")
    data.to_postgis(name, engine)
    
    
save_file("coastline")