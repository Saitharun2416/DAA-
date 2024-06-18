import heapq

def p(graph, start):
    mst = []  
    visited = set()  
    min_heap = [(0, start, None)]  
    
    while min_heap:
        cost, current_node, previous_node = heapq.heappop(min_heap)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if previous_node is not None:
            mst.append((previous_node, current_node, cost))
        
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor, current_node))
    
    return mst

graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 6},
        'C': {'A': 4, 'B': 2, 'D': 3},
        'D': {'B': 6, 'C': 3}
    }
start_node = 'A' 
mst = p(graph, start_node)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
