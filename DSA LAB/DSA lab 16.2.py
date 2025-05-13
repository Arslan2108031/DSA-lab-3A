def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    nodes_to_process = list(graph.keys())  
    while nodes_to_process:
        min_node = None
        for node in nodes_to_process:
            if min_node is None or distances[node] < distances[min_node]:
                min_node = node
        nodes_to_process.remove(min_node)
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance   
    return distances
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
source_node = 'A'
shortest_paths = dijkstra(graph, source_node)
print(f"Shortest paths from '{source_node}':")
for node, distance in shortest_paths.items():
    print(f"Distance from {source_node} to {node}: {distance}")

