import geopandas as gpd
#import folium
import matplotlib.pyplot as plt


infile = './A16-15_07_GML/A16-15_07_DID.shp'
gdf = gpd.read_file(infile)
print(f'shape file is loaded: {infile}')
print(gdf.head())

f = plt.figure(figsize=(6, 6))
a = f.gca()
a.plot(*gdf.iloc[0].geometry.exterior.xy)
plt.show()
f.savefig('out_gpd')
