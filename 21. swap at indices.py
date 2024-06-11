from typing import List
import collections

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px

def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    dsu = DSU(len(s))
    for a, b in pairs:
        dsu.union(a, b)
    groups = collections.defaultdict(list)
    for i in range(len(s)):
        groups[dsu.find(i)].append(s[i])

    for key in groups:
        groups[key].sort(reverse=True)

    result = []
    for i in range(len(s)):
        group = dsu.find(i)
        result.append(groups[group].pop())
    
    return ''.join(result)
s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
print(smallestStringWithSwaps(s, pairs))  # Output: "bacd"

#Time complexity:0(n logn)
#Space complexity:o(n)
