class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}  
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.prev = self.head
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    def _insert_at_front(self, node):
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node
    def get(self, key):
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._insert_at_front(node)
            return node.value
        return -1
    def put(self, key, value):
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self._remove(node)
            self._insert_at_front(node)
        else:
            if len(self.hashmap) >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.hashmap[lru_node.key]
            new_node = Node(key, value)
            self._insert_at_front(new_node)
            self.hashmap[key] = new_node
    def display(self):
        current = self.head.next
        print("Cache State: ", end="")
        while current != self.tail:
            print(f"({current.key}:{current.value})", end=" -> ")
            current = current.next
        print("None")
def test_lru_cache():
    print("\n--- Testing LRU Cache ---")
    cache = LRUCache(3)
    cache.put(1, 10)
    cache.put(2, 20)
    cache.put(3, 30)
    cache.display()

    print("Get 2:", cache.get(2))  
    cache.display()

    cache.put(4, 40)  
    cache.display()

    print("Get 1:", cache.get(1))
    print("Get 3:", cache.get(3))  
    cache.display()

test_lru_cache()
