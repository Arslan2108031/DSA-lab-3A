class Heap:
    def __init__(self, is_min_heap=True):
        self.heap = []
        self.is_min_heap = is_min_heap  

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _compare(self, child, parent):
        if self.is_min_heap:
            return child < parent
        else:
            return child > parent

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index):
        while index > 0 and self._compare(self.heap[index], self.heap[self._parent(index)]):
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract_root(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return root

    def _sift_down(self, index):
        size = len(self.heap)
        while self._left_child(index) < size:
            smallest_or_largest = self._left_child(index)
            right = self._right_child(index)
            if right < size and self._compare(self.heap[right], self.heap[smallest_or_largest]):
                smallest_or_largest = right
            if self._compare(self.heap[smallest_or_largest], self.heap[index]):
                self.heap[index], self.heap[smallest_or_largest] = self.heap[smallest_or_largest], self.heap[index]
                index = smallest_or_largest
            else:
                break

    def heapify(self, array):
        self.heap = array[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)

    def display(self):
        print(self.heap)

def test_heap():
    print("Testing Min-Heap:")
    min_heap = Heap(is_min_heap=True)
    elements = [5, 3, 8, 1, 6]
    for el in elements:
        min_heap.insert(el)
    min_heap.display()
    print("Peek:", min_heap.peek())  
    print("Extract Root:", min_heap.extract_root())  
    min_heap.display()

    print("\nTesting Max-Heap:")
    max_heap = Heap(is_min_heap=False)
    for el in elements:
        max_heap.insert(el)
    max_heap.display()
    print("Peek:", max_heap.peek()) 
    print("Extract Root:", max_heap.extract_root())  
    max_heap.display()

    print("\nTesting Heapify:")
    array = [9, 4, 7, 1, -2, 6, 5]
    min_heap2 = Heap(is_min_heap=True)
    min_heap2.heapify(array)
    min_heap2.display() 

if __name__ == "__main__":
    test_heap()
