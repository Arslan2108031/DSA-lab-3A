class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def dijkstra(self, start):
        distances = {}
        for vertex in self.adj_list:
            distances[vertex] = float('inf')
        distances[start] = 0

        visited = []
        heap = [(0, start)]  

        while heap:
            min_index = 0
            for i in range(1, len(heap)):
                if heap[i][0] < heap[min_index][0]:
                    min_index = i
            current_distance, current_vertex = heap.pop(min_index)

            if current_vertex in visited:
                continue
            visited.append(current_vertex)

            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heap.append((distance, neighbor))

        return distances
def test_dijkstra():
    print("\n--- Testing Dijkstra's Algorithm ---")
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 3)
    g.add_edge('E', 'D', 4)
    g.add_edge('D', 'F', 11)

    print("Adjacency List with Weights:")
    for vertex in g.adj_list:
        print(vertex, ":", g.adj_list[vertex])

    distances = g.dijkstra('A')
    print("\nShortest distances from A:")
    for vertex in distances:
        print(f"A -> {vertex} : {distances[vertex]}")

test_dijkstra()
