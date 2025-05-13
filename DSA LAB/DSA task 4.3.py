class CircularQueue:
    def __init__(self, size):
        self.size = size  
        self.queue = [None] * size  
        self.front = -1  
        self.rear = -1   

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full!")
        else:
            if self.front == -1:  
                self.front = 0
            self.rear = (self.rear + 1) % self.size  
            self.queue[self.rear] = element
            print(f"Enqueued: {element}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            removed_element = self.queue[self.front]
            if self.front == self.rear:  
                self.front = self.rear = -1  
            else:
                self.front = (self.front + 1) % self.size  
            print(f"Dequeued: {removed_element}")

    def front_element(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.queue[self.front]

    def rear_element(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.queue[self.rear]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            elements = []
            i = self.front
            while i != self.rear:
                elements.append(self.queue[i])
                i = (i + 1) % self.size
            elements.append(self.queue[self.rear])
            print("Queue:", elements)
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.dequeue()
cq.enqueue(60)
print("Front:", cq.front_element())  
print("Rear:", cq.rear_element())    
cq.display()
