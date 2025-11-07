import geopandas as gpd


data_dir = "../../data/"
out_dir = "../../out/"
rivers_lakes = gpd.read_file(data_dir + "ne_50m_rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.shp")
fig = rivers_lakes.plot().get_figure()
fig.savefig(out_dir + "rivers_lakes.png")

