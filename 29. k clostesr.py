import heapq

def kClosest(points, k):
    
    def distance(point):
        return point[0]**2 + point[1]**2
 
    heap = [(distance(point), point) for point in points[:k]]
    heapq.heapify(heap)
  
    for point in points[k:]:
        heapq.heappushpop(heap, (distance(point), point))
 
    return [point for _, point in heap]

points = [[1, 3], [-2, 2]]
k = 1
print(kClosest(points, k))  # Output: [[-2, 2]]

#Time complexity:O(nlogk)
#Space complexity:O(k)
