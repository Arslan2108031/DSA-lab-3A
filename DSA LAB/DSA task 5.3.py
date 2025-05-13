class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return None

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add(new_node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    def display(self):
        print("Cache state:", end=" ")
        current = self.head.next
        result = {}
        while current != self.tail:
            result[current.key] = current.value
            current = current.next
        print(result)

def test_lru_cache():
    cache = LRUCache(5)
    cache.put(1, "A")
    cache.put(2, "B")
    cache.put(3, "C")
    cache.put(4, "D")
    cache.put(5, "E")
    cache.display()

    cache.get(2) 
    cache.put(6, "F")  
    cache.display()

    cache.get(4) 
    cache.put(7, "G")  
    cache.display()

    cache.get(5) 
    cache.put(8, "H")
    cache.display()

if __name__ == "__main__":
    test_lru_cache()
