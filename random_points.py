import numpy as np
from shapely.geometry import Point
import geopandas as gpd

# Create random points between a defined lat/long range. Size = number of points
y_vals = np.random.uniform(low=37.0, high=38.0, size=(50))
x_vals = np.random.uniform(low=-121.0, high=-120.0, size=(50))

x_vals_list = list(x_vals)
y_vals_list = list(y_vals)
# Turn the list into Poings
geom = [Point(xy) for xy in zip(x_vals_list, y_vals_list)]
crs = {'init': 'epsg:4326'}

geo_df = GeoDataFrame(crs=crs, geometry=geom)
geo_df.plot()

geo_df.to_file(driver='ESRI Shapefile', filename=("random_points.shp"))
