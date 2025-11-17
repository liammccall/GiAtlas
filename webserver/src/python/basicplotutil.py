import geopandas as gpd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

data_dir = PROJECT_ROOT / "data"
out_dir = PROJECT_ROOT / "out"

def generate_map(name : str):
    data = gpd.read_file(data_dir / f"ne_50m_{name}/ne_50m_{name}.shp")

    fig = data.plot().get_figure()
    save_path = out_dir / f"{name}.png"
    fig.savefig(save_path)
    
    return save_path