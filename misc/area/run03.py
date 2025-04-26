from pyproj import Geod
from scipy.spatial import ConvexHull
import numpy as np

def convex_hull_area_geod_direct_debug(points):
    if len(points) < 3:
        return 0.0
    hull = ConvexHull(points)
    hull_coords = [points[i] for i in hull.vertices]

    geod = Geod(ellps='WGS84')

    lons = [coord[1] for coord in hull_coords]
    lats = [coord[0] for coord in hull_coords]

    if lons[0] != lons[-1] or lats[0] != lats[-1]:
        lons.append(lons[0])
        lats.append(lats[0])

    print("Lats:", lats)
    print("Lons:", lons)

    if len(lons) < 3:
        return 0.0

    area, perimeter = geod.polygon_area_perimeter(lons, lats)
    return abs(area)

points_west_en = np.array([
    (34.0522, -118.2437),  # Los Angeles
    (37.7749, -122.4194),  # San Francisco
    (33.7075, -117.9157),  # Anaheim
    (38.5816, -121.4944)   # Sacramento
])

area_west_en_debug = convex_hull_area_geod_direct_debug(points_west_en)
print(f"Convex Hull Area (Debug): {area_west_en_debug:.2f} square meters")