class Graph:
    def __init__(self):
        self.adj_list = {}
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    def add_edge(self, v1, v2):
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)  
    def bfs(self, start_vertex):
        visited = []
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)  
            if vertex not in visited:
                visited.append(vertex)
                for neighbor in self.adj_list.get(vertex, []):
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
        return visited
    def dfs_recursive(self, start_vertex, visited=None):
        if visited is None:
            visited = []

        visited.append(start_vertex)

        for neighbor in self.adj_list.get(start_vertex, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

        return visited
    def dfs_stack(self, start_vertex):
        visited = []
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()  
            if vertex not in visited:
                visited.append(vertex)
                for neighbor in reversed(self.adj_list.get(vertex, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return visited
def test_traversals():
    print("\n--- Testing BFS and DFS Traversals ---")
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'F')
    g.add_edge('E', 'F')

    print("Adjacency List:")
    for vertex in g.adj_list:
        print(vertex, ":", g.adj_list[vertex])

    print("\nBFS Traversal:", g.bfs('A'))
    print("DFS Recursive Traversal:", g.dfs_recursive('A'))
    print("DFS Stack Traversal:", g.dfs_stack('A'))

test_traversals()
