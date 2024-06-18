import heapq

def d(graph, start):
    p= [(0, start)]  
    dist= {vertex: float('infinity') for vertex in graph}
    dist[start] = 0
    visited = set()
    
    while p:
        cd,cv = heapq.heappop(p)
        if cv in visited:
            continue
        visited.add(cv)
        for i, j in graph[cv].items():
            distance = cd + j
            if distance < dist[i]:
                dist[i] = distance
                heapq.heappush(p, (distance, i))
    
    return dist


graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1aD': {'B': 5, 'C': 1}
    }
s = 'A'
distances = d(graph, s)
print("shortest path:",distances)
x=distances.values()
print("minimum cost:",sum(x))
