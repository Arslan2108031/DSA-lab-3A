class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return False 
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True
def detect_cycle_undirected(graph, n):
    ds = DisjointSet(n)
    
    for u in range(n):
        for v in graph[u]:
            if not ds.union(u, v):
                return True  
    return False
graph_undirected = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}
print(detect_cycle_undirected(graph_undirected, 4)) 