import heapq

def p(graph, start):
    mst = []
    visited = set()
    m= [(0, start, None)]
    while m:
        cost, c, p = heapq.heappop(m)
        if c in visited:
            continue
        
        visited.add(c)
        if p is not None:
            mst.append((p, c, cost))
        
        for i, j in graph[c].items():
            if i not in visited:
                heapq.heappush(m, (j, i, c))
    
    return mst

graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 6},
        'C': {'A': 4, 'B': 2, 'D': 3},
        'D': {'B': 6, 'C': 3}
    }
a = 'A'
mst = p(graph,a)
print("Minimum Spanning Tree:",mst)
