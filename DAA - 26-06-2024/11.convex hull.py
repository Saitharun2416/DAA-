import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def convex(points):
    start = min(points, key=lambda p: (p[1], p[0]))
    points.pop(points.index(start))
    points.sort(key=lambda p: (math.atan2(p[1] - start[1], p[0] - start[0]), (p[0] - start[0]) ** 2 + (p[1] - start[1]) ** 2))
    hull = [start]

    for i in points:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], i) != 2:
            hull.pop()
        hull.append(i)
    return hull
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
hull = convex(points)
print("The points in the convex hull are:", hull)
