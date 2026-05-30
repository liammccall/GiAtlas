from pathlib import Path

import geopandas as gpd
from sqlalchemy import create_engine

import src.python.db.util as util

PROJECT_ROOT = Path(__file__).resolve().parents[3]

data_dir = PROJECT_ROOT / "data"
engine = create_engine("postgresql://username:password@db:5432/gidb")

def natural_earth_url(
    name: str,
    resolution: str = "10m",
    category: str = "physical",
):
    return (
        f"https://naturalearth.s3.amazonaws.com/"
        f"{resolution}_{category}/"
        f"ne_{resolution}_{name}.zip"
    )

def save_natural_earth(from_name : str, to_name: str):
    data = gpd.read_file(natural_earth_url(from_name))
    # data.to_postgis(to_name, engine, if_exists='replace')
    util.save_gis(data, from_name, "hey")
    
def save_file(from_name : str, to_name: str):
    data = gpd.read_file(data_dir / f"ne_50m_{from_name}/ne_50m_{from_name}.shp")
    data.to_postgis(to_name, engine, if_exists='replace')
    
def retrieve_file(name : str):
    data = gpd.read_postgis(f"SELECT geometry FROM public.{name}", engine, geom_col="geometry")
    return data