class PriorityQueue:
    def __init__(self, is_min_heap=True):
        self.heap = []
        self.is_min_heap = is_min_heap

    def push(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("pop from empty priority queue")
        self._swap(0, len(self.heap) - 1)
        root = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("peek from empty priority queue")
        return self.heap[0]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self._compare(self.heap[index], self.heap[parent_index]):
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest_or_largest = index

        if left_child_index < len(self.heap) and self._compare(self.heap[left_child_index], self.heap[smallest_or_largest]):
            smallest_or_largest = left_child_index

        if right_child_index < len(self.heap) and self._compare(self.heap[right_child_index], self.heap[smallest_or_largest]):
            smallest_or_largest = right_child_index

        if smallest_or_largest != index:
            self._swap(index, smallest_or_largest)
            self._heapify_down(smallest_or_largest)

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _compare(self, child, parent):
        if self.is_min_heap:
            return child < parent  
        else:
            return child > parent 

def find_k_smallest(arr, k):
    pq = PriorityQueue(is_min_heap=True)
    for num in arr:
        pq.push(num)
    
    return [pq.pop() for _ in range(k)]

def find_k_largest(arr, k):
    pq = PriorityQueue(is_min_heap=False)  
    for num in arr:
        pq.push(num)
    
    return [pq.pop() for _ in range(k)]

def find_k_smallest_sorted(arr, k):
    return sorted(arr)[:k]

def find_k_largest_sorted(arr, k):
    return sorted(arr, reverse=True)[:k]
if __name__ == "__main__":
    arr = [10, 4, 5, 8, 6, 1, 9, 7, 3, 2]
    k = 3
    print("K smallest using heap:", find_k_smallest(arr[:], k))
    print("K largest using heap:", find_k_largest(arr[:], k))
    print("K smallest using sorting:", find_k_smallest_sorted(arr[:], k))
    print("K largest using sorting:", find_k_largest_sorted(arr[:], k))
