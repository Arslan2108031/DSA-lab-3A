class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size
        self.collisions = 0
    def custom_hash(self, key):
        hash_value = 0
        prime = 31  
        for char in key:
            hash_value = (hash_value * prime + ord(char)) % self.size
        return hash_value
    def insert_custom(self, key):
        index = self.custom_hash(key)
        if self.table[index] is not None:
            self.collisions += 1
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key)
        else:
            self.table[index] = Node(key)
    def insert_builtin(self, key):
        index = hash(key) % self.size
        if self.table[index] is not None:
            self.collisions += 1
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key)
        else:
            self.table[index] = Node(key)
    def reset(self):
        self.table = [None] * self.size
        self.collisions = 0

    def display(self):
        for i in range(self.size):
            print(f"Bucket {i}: ", end="")
            current = self.table[i]
            while current:
                print(f"{current.key} -> ", end="")
                current = current.next
            print("None")
    def histogram(self):
        bucket_sizes = []
        for bucket in self.table:
            count = 0
            current = bucket
            while current:
                count += 1
                current = current.next
            bucket_sizes.append(count)
        max_count = max(bucket_sizes)
        for level in range(max_count, 0, -1):
            for count in bucket_sizes:
                if count >= level:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()
        print("-" * (self.size * 3))
        for i in range(self.size):
            print(f"{i%10}  ", end="")
        print()
def test_hash_functions():
    keys = []
    for i in range(300):
        keys.append("key" + str(i))
    print("\n--- Using Custom Hash Function ---")
    ht_custom = HashTable(size=50)
    for key in keys:
        ht_custom.insert_custom(key)
    print("Total Collisions (Custom Hash):", ht_custom.collisions)
    ht_custom.histogram()
    print("\n--- Using Built-in hash() Function ---")
    ht_builtin = HashTable(size=50)
    for key in keys:
        ht_builtin.insert_builtin(key)
    print("Total Collisions (Built-in Hash):", ht_builtin.collisions)
    ht_builtin.histogram()

test_hash_functions()
