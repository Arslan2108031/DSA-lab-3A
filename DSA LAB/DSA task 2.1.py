class DynamicArray:
    def __init__(self):
        self.capacity = 4
        self.length = 0
        self.array = self._make_array(self.capacity)

    def _make_array(self, size):
        return [None] * size  

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, value):
       
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.length] = value
        self.length += 1

    def insert(self, index, value):
       
        if index < 0 or index > self.length:
            print("Invalid index")
            return
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.length += 1

    def delete(self, index):
  
        if index < 0 or index >= self.length:
            print("Invalid index")
            return
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.length - 1] = None
        self.length -= 1

        if self.length > 0 and self.length == self.capacity // 4:
            self._resize(self.capacity // 2)

    def search(self, value):

        for i in range(self.length):
            if self.array[i] == value:
                return i
        return -1

    def display(self):
        return [self.array[i] for i in range(self.length)]

print("=== Testing Custom Dynamic Array ===")

da = DynamicArray()

da.append(10)
da.append(20)
da.append(30)
da.append(40)
print("After appending:", da.display()) 

da.insert(2, 25)
print("After inserting 25 at index 2:", da.display()) 

da.delete(1)
print("After deleting index 1:", da.display()) 
print("Index of 30:", da.search(30))  
print("Index of 99:", da.search(99))  
print("Final array:", da.display())


