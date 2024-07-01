import heapq
import math

def close(p, k):
    distances = [(math.sqrt(x**2 + y**2), [x, y]) for x, y in p]
    c = heapq.nsmallest(k, distances)
    return [point for _, point in c]

p = [[1,3],[-2,2],[5,8],[0,1]]
k = 2
print(close(p, k))  
