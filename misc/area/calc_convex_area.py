from scipy.spatial import ConvexHull
from geopy.distance import geodesic
import math

def convex_hull_area_geodesic_en(points):
    """
    Calculates the area of the convex hull enclosing a given set of latitude and longitude points using geodesic distances.

    Args:
        points: A list of latitude and longitude points. Each point should be a tuple or list
                in the format (latitude, longitude). Duplicate points are acceptable.

    Returns:
        The area of the convex hull in square meters.
        Returns 0.0 if there are fewer than 3 points.
    """
    if len(points) < 3:
        return 0.0

    # Calculate the convex hull
    hull = ConvexHull(points)

    # Get the indices of the vertices of the convex hull
    hull_points_indices = hull.vertices

    # Get the coordinates of the convex hull vertices in order
    hull_coordinates = [points[i] for i in hull_points_indices]

    # Close the polygon by adding the first point to the end if it's not already there
    if hull_coordinates[0] != hull_coordinates[-1]:
        hull_coordinates = hull_coordinates + [hull_coordinates[0]]

    area = 0.0
    for i in range(len(hull_coordinates) - 1):
        point1 = hull_coordinates[i]
        point2 = hull_coordinates[i + 1]
        # Calculate the geodesic distance (in meters) between the two points
        distance = geodesic(point1, point2).meters
        # Approximate latitude of the midpoint
        mid_latitude_rad = (point1[0] + point2[0]) / 2 * (math.pi / 180.0)
        # Average Earth radius
        earth_radius = 6371000  # meters
        # Approximate radians per meter in the latitude direction
        lat_to_rad = (point1[0] - point2[0]) / distance if distance > 0 else 0
        # Approximate longitudinal distance
        lon_distance = (point1[1] - point2[1]) * earth_radius * math.cos(mid_latitude_rad)

        # Calculate the contribution to the area (simple triangle approximation)
        area += (lon_distance * distance) / 2

    return abs(area)

# Example
points_en = [
    (35.6895, 139.6917),  # Tokyo Station
    (35.6585, 139.7454),  # Tsukiji Market
    (35.6305, 139.7663),  # Toyosu Market
    (35.6750, 139.7151),  # Imperial Palace
    (35.7000, 139.7000),  # New point
    (35.6400, 139.7500)   # Another new point
]

area_convex_hull_en = convex_hull_area_geodesic_en(points_en)
print(f"Convex Hull Area (Geodesic): {area_convex_hull_en:.2f} square meters")
