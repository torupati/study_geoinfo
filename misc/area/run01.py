from scipy.spatial import ConvexHull
import numpy as np

points_en = np.array([
    (35.6895, 139.6917),  # Tokyo Station
    (35.6585, 139.7454),  # Tsukiji Market
    (35.6305, 139.7663),  # Toyosu Market
    (35.6750, 139.7151),  # Imperial Palace
    (35.7000, 139.7000),  # New point
    (35.6400, 139.7500)   # Another new point
])

hull = ConvexHull(points_en)
print("Indices of Convex Hull Vertices:", hull.vertices)
print("Coordinates of Convex Hull Vertices:")
for index in hull.vertices:
    print(points_en[index])

    """
    Looking at these coordinates:

(35.6895, 139.6917) - Tokyo Station
(35.7000, 139.7000) - New point (slightly north of Tokyo Station)
(35.6585, 139.7454) - Tsukiji Market (east of Tokyo Station)
(35.6305, 139.7663) - Toyosu Market (further east and slightly south)
(35.6400, 139.7500) - Another new point (between Tsukiji and Toyosu, slightly south)
These points seem to form a reasonable convex hull encompassing the original set of points in the Tokyo area. The order of the vertices [0, 4, 1, 2, 5] indicates the sequence in which they are connected to form the polygon.
    """