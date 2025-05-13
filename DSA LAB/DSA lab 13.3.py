class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False

def kruskal(edges, num_nodes):
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            if edges[i][2] > edges[j][2]:
                edges[i], edges[j] = edges[j], edges[i]
    
    ds = DisjointSet(num_nodes)
    mst = []
    total_weight = 0
    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w

    print("Total Weight of MST:", total_weight)
    return mst
