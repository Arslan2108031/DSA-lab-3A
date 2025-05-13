class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.vertices = []
        self.adj_list = {}
        self.adj_matrix = []
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.adj_list[vertex] = []
            size = len(self.vertices)
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0] * size)
    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)

        self.adj_list[v1].append(v2)
        self.adj_matrix[self.vertices.index(v1)][self.vertices.index(v2)] = 1

        if not self.directed:
            self.adj_list[v2].append(v1)
            self.adj_matrix[self.vertices.index(v2)][self.vertices.index(v1)] = 1
    def display(self):
        print("\nAdjacency List:")
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(row)
def test_graph():
    print("\n--- Testing Undirected Graph ---")
    g1 = Graph(directed=False)
    g1.add_vertex('A')
    g1.add_vertex('B')
    g1.add_edge('A', 'B')
    g1.add_edge('A', 'C')
    g1.add_edge('B', 'C')
    g1.display()

    print("\n--- Testing Directed Graph ---")
    g2 = Graph(directed=True)
    g2.add_edge('X', 'Y')
    g2.add_edge('Y', 'Z')
    g2.add_edge('Z', 'X')
    g2.display()

test_graph()
