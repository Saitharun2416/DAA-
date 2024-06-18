class UnionFind:
    def _init_(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph, num_vertices):
    edges = sorted(graph, key=lambda edge: edge[2])
    union_find = UnionFind(num_vertices)
    mst = []

    for edge in edges:
        u, v, weight = edge
        if union_find.find(u) != union_find.find(v):
            union_find.union(u, v)
            mst.append(edge)
            if len(mst) == num_vertices - 1:
                break

    return mst

graph = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
num_vertices = 4
mst = kruskal(graph, num_vertices)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
