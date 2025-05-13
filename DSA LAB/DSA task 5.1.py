class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        new_node = Node(key, value)
        if self.table[idx] is None:
            self.table[idx] = new_node
        else:
            current = self.table[idx]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def get(self, key):
        idx = self._hash(key)
        current = self.table[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        idx = self._hash(key)
        current = self.table[idx]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[idx] = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("HashTableChaining contents:")
        for i, node in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}:{current.value}) ->", end=" ")
                current = current.next
            print("None")
        print()

class HashTableOpenAddressing:
    def __init__(self, size=20):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            k, v = self.table[idx]
            if k == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.size
            if idx == start_idx:
                print("HashTable is full!")
                return
        self.table[idx] = (key, value)

    def get(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            k, v = self.table[idx]
            if k == key:
                return v
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        return None

    def delete(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            k, v = self.table[idx]
            if k == key:
                self.table[idx] = None
                return True
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        return False

    def display(self):
        print("HashTableOpenAddressing contents:")
        for i, item in enumerate(self.table):
            if item:
                print(f"Slot {i}: ({item[0]}:{item[1]})")
            else:
                print(f"Slot {i}: Empty")
        print()

def main():
    print("--- Testing HashTableChaining ---")
    ht_chaining = HashTableChaining()
    ht_chaining.insert("apple", 1)
    ht_chaining.insert("banana", 2)
    ht_chaining.insert("orange", 3)
    ht_chaining.insert("grape", 4)
    ht_chaining.display()
    print("Get 'banana':", ht_chaining.get("banana"))
    ht_chaining.delete("banana")
    print("After deleting 'banana':")
    ht_chaining.display()

    print("--- Testing HashTableOpenAddressing ---")
    ht_open = HashTableOpenAddressing()
    ht_open.insert("apple", 1)
    ht_open.insert("banana", 2)
    ht_open.insert("orange", 3)
    ht_open.insert("grape", 4)
    ht_open.display()
    print("Get 'orange':", ht_open.get("orange"))
    ht_open.delete("orange")
    print("After deleting 'orange':")
    ht_open.display()

if __name__ == "__main__":
    main()
