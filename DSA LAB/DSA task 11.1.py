class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while True:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}:", end=" ")
            current = self.table[i]
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")
class HashTableOpenAddressing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.deleted = "<deleted>"

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None and self.table[index] != self.deleted:
            k, v = self.table[index]
            if k == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == start_index:
                print("Hash Table is full!")
                return
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index] != self.deleted:
                k, v = self.table[index]
                if k == key:
                    return v
            index = (index + 1) % self.size
            if index == start_index:
                break
        return None

    def delete(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index] != self.deleted:
                k, v = self.table[index]
                if k == key:
                    self.table[index] = self.deleted
                    return True
            index = (index + 1) % self.size
            if index == start_index:
                break
        return False

    def display(self):
        for i in range(self.size):
            if self.table[i] is None:
                print(f"Slot {i}: Empty")
            elif self.table[i] == self.deleted:
                print(f"Slot {i}: Deleted")
def test_hash_tables():
    print("\n--- Testing Hash Table with Chaining ---")
    htc = HashTableChaining()
    htc.insert("apple", 10)
    htc.insert("banana", 20)
    htc.insert("grape", 30)
    htc.insert("apricot", 40)  
    htc.display()
    print("Get apple:", htc.get("apple"))
    htc.delete("banana")
    htc.display()

    print("\n--- Testing Hash Table with Open Addressing (Linear Probing) ---")
    hto = HashTableOpenAddressing()
    hto.insert("apple", 10)
    hto.insert("banana", 20)
    hto.insert("grape", 30)
    hto.insert("apricot", 40)
    hto.display()
    print("Get grape:", hto.get("grape"))
    hto.delete("banana")
    hto.display()

test_hash_tables()
