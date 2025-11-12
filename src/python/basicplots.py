import geopandas as gpd


data_dir = "../../data/"
out_dir = "../../out/"
rivers_lakes = gpd.read_file(data_dir + "ne_50m_rivers_lake_centerlines/ne_50m_rivers_lake_centerlines.shp")
coastline = gpd.read_file(data_dir + "ne_50m_coastline/ne_50m_coastline.shp")
lakes = gpd.read_file(data_dir + "ne_50m_lakes/ne_50m_lakes.shp")
land = gpd.read_file(data_dir + "ne_50m_land/ne_50m_land.shp")
ocean = gpd.read_file(data_dir + "ne_50m_ocean/ne_50m_ocean.shp")

fig = rivers_lakes.plot().get_figure()
fig.savefig(out_dir + "rivers_lakes.png")

ax = coastline.plot(zorder=0)
lakes.plot(ax=ax, zorder=1)
# land.plot(ax=ax, zorder=2)
# ocean.plot(ax=ax, zorder=3)
ax.get_figure().savefig(out_dir + "combined.png")

fig = coastline.plot().get_figure()
fig.savefig(out_dir + "coastline.png")

fig = lakes.plot().get_figure()
fig.savefig(out_dir + "lakes.png")

fig = land.plot().get_figure()
fig.savefig(out_dir + "land.png")

fig = ocean.plot().get_figure()
fig.savefig(out_dir + "ocean.png")
