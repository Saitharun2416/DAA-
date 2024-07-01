import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair_of_points(points):
    min_distance = float('inf')
    closest_pair = None
    n = len(points)
    
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    
    return closest_pair, min_distance

def is_left_turn(p1, p2, p):
    return (p2[0] - p1[0]) * (p[1] - p1[1]) - (p2[1] - p1[1]) * (p[0] - p1[0])

def is_collinear(p1, p2, p3):
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) == (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex_hull_with_collinear(points):
    n = len(points)
    hull = []
    
    for i in range(n):
        for j in range(i + 1, n):
            left_turns = right_turns = 0
            collinear_points = []
            for k in range(n):
                if k != i and k != j:
                    turn = is_left_turn(points[i], points[j], points[k])
                    if turn > 0:
                        left_turns += 1
                    elif turn < 0:
                        right_turns += 1
                    elif is_collinear(points[i], points[j], points[k]):
                        collinear_points.append(points[k])
            if left_turns == 0 or right_turns == 0:
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])
                for p in collinear_points:
                    if p not in hull:
                        hull.append(p)
    
    return hull
points = [(10,0), (11,5), (5, 3), (9, 3.5), (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)]
closest_pair, min_distance = closest_pair_of_points(points)
print("Closest pair of points:", closest_pair)
print("Minimum distance:", min_distance)
hull_points_with_collinear = convex_hull_with_collinear(points)
print("Convex hull points with collinear points:", hull_points_with_collinear)
