class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, node, dist):
        self.heap.append((dist, node))
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)
        min_node = self.heap.pop()
        self._heapify_down(0)
        return min_node

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent][0] <= self.heap[index][0]:
                break
            self._swap(index, parent)
            index = parent

    def _heapify_down(self, index):
        size = len(self.heap)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index
            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            if smallest == index:
                break
            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    min_heap = MinHeap()
    min_heap.insert(start, 0)

    while not min_heap.is_empty():
        current_distance, current_node = min_heap.extract_min()
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                min_heap.insert(neighbor, distance)
    
    return distances

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)],
    }
    
    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    print(f"Shortest distances from {start_node}:")
    for node, distance in shortest_distances.items():
        print(f"Distance to {node}: {distance}")
