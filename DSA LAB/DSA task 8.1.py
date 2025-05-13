class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}  
        self.adj_matrix = [] 

    def add_edge(self, v1, v2):

        if v1 not in self.adj_list:
            self.adj_list[v1] = []
        if v2 not in self.adj_list:
            self.adj_list[v2] = []
        
        self.adj_list[v1].append(v2)

        if not self.directed:
            self.adj_list[v2].append(v1)

        self._update_adj_matrix(v1, v2)

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
        
        if not self.directed:
            if v2 in self.adj_list and v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
        self._update_adj_matrix(v1, v2, remove=True)

    def _update_adj_matrix(self, v1, v2, remove=False):
        vertices = sorted(self.adj_list.keys())
        if len(self.adj_matrix) == 0:
            size = len(vertices)
            self.adj_matrix = [[0] * size for _ in range(size)]
        
        v1_index = vertices.index(v1)
        v2_index = vertices.index(v2)
        
        if remove:
            self.adj_matrix[v1_index][v2_index] = 0
            if not self.directed:
                self.adj_matrix[v2_index][v1_index] = 0
        else:
            self.adj_matrix[v1_index][v2_index] = 1
            if not self.directed:
                self.adj_matrix[v2_index][v1_index] = 1

    def display(self):
        print("Adjacency List:")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")
        
        print("\nAdjacency Matrix:")
        vertices = sorted(self.adj_list.keys())
        for row in self.adj_matrix:
            print(row)

if __name__ == "__main__":
    g = Graph(directed=True)

    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_edge(1, 4)

    g.display()

    g.remove_edge(1, 2)

    print("\nAfter removing edge 1 -> 2:")
    g.display()

    g2 = Graph(directed=False)

    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 1)

    print("\nUndirected Graph:")
    g2.display()
