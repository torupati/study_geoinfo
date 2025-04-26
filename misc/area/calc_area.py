from geopy.distance import geodesic
import math

def polygon_area_geodesic_en(coordinates):
    """
    Calculates the area of a polygon defined by latitude and longitude points using geodesic distances.

    Args:
        coordinates: A list of latitude and longitude points. Each point should be a tuple or list
                     in the format (latitude, longitude). The first and last points do not need to be the same.

    Returns:
        The area of the polygon in square meters.
    """
    if len(coordinates) < 3:
        return 0.0  # A polygon needs at least 3 points

    # Close the polygon by adding the first point to the end if it's not already there
    if coordinates[0] != coordinates[-1]:
        coordinates = coordinates + [coordinates[0]]

    area = 0.0
    for i in range(len(coordinates) - 1):
        point1 = coordinates[i]
        point2 = coordinates[i + 1]
        # Calculate the distance (in meters) between the two points using geodesic
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
coordinates_en = [
    (35.6895, 139.6917),  # Tokyo Station
    (35.6585, 139.7454),  # Tsukiji Market
    (35.6305, 139.7663),  # Toyosu Market
    (35.6750, 139.7151),  # Imperial Palace
    (35.6895, 139.6917)   # Back to the first point (optional)
]

area_en = polygon_area_geodesic_en(coordinates_en)
print(f"Polygon Area (Geodesic): {area_en:.2f} square meters")
