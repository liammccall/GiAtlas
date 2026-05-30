import geopandas as gpd
from io import BytesIO
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

data_dir = PROJECT_ROOT / "data"


def generate_map_file(name: str):
    data = gpd.read_file(data_dir / f"ne_50m_{name}/ne_50m_{name}.shp")
    return _generate_map_core(data, name)


def generate_map_df(data: gpd.GeoDataFrame, name: str = "image"):
    return _generate_map_core(data, name)


def _generate_map_core(data: gpd.GeoDataFrame, name: str = "image"):
    fig = data.plot().get_figure()

    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    return buf