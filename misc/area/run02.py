from pyproj import Geod
from scipy.spatial import ConvexHull
import numpy as np

def convex_hull_area_geod_direct(points):
    if len(points) < 3:
        return 0.0
    hull = ConvexHull(points)
    hull_coords = [points[i] for i in hull.vertices]

    # Define a Geod object for accurate geodesic calculations (using WGS84 ellipsoid)
    geod = Geod(ellps='WGS84')

    # Separate longitudes and latitudes
    lons = [coord[1] for coord in hull_coords]
    lats = [coord[0] for coord in hull_coords]

    # Ensure the polygon is closed by adding the first point at the end
    if lons[0] != lons[-1] or lats[0] != lats[-1]:
        lons.append(lons[0])
        lats.append(lats[0])

    if len(lons) < 3:
        return 0.0

    # Calculate the area directly using geod.polygon_area_perimeter
    area, perimeter = geod.polygon_area_perimeter(lons, lats)
    return abs(area)

points_en = np.array([
    (35.6895, 139.6917),  # Tokyo Station
    (35.6585, 139.7454),  # Tsukiji Market
    (35.6305, 139.7663),  # Toyosu Market
    (35.6750, 139.7151),  # Imperial Palace
    (35.6750, 139.7251),  # new point
    (35.7000, 139.7000),  # New point
    (35.6400, 139.7500)   # Another new point
])
#area_geod_direct = convex_hull_area_geod_direct(points_en)

points_west_en = np.array([
    (34.0522, -118.2437),  # Los Angeles
    (37.7749, -122.4194),  # San Francisco
    (33.7075, -117.9157),  # Anaheim
    (38.5816, -121.4944)   # Sacramento
])

area_geod_direct = convex_hull_area_geod_direct(points_west_en)
print(f"Convex Hull Area (Geod Direct): {area_geod_direct:.2f} square meters")

