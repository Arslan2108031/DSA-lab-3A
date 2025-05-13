class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0 

    def enqueue(self, value, priority):
        self.heap.append((priority, self.counter, value))
        self.counter += 1
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty priority queue")

        root_value = self.heap[0][2]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if not self.is_empty():
            self._heapify_down(0)
        
        return root_value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self.heap[0][2]

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][0] < self.heap[parent_index][0]:  
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while index * 2 + 1 < len(self.heap):
            left_child = index * 2 + 1
            right_child = index * 2 + 2
            smallest = index

            if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
                smallest = left_child
            if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
                smallest = right_child

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

if __name__ == "__main__":
    pq = PriorityQueue()

    pq.enqueue("Task 1", 3)  
    pq.enqueue("Task 2", 1)
    pq.enqueue("Task 3", 2)

    print("Highest priority task:", pq.peek()) 

    print("Dequeued task:", pq.dequeue())  
    print("Dequeued task:", pq.dequeue())  
    print("Dequeued task:", pq.dequeue())  

    try:
        pq.dequeue()
    except IndexError as e:
        print(e)
