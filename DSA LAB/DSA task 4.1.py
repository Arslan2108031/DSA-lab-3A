#Using Arrays
class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

print("Stack using Python list:")
stack_array = StackArray()
stack_array.push(1)
stack_array.push(2)
stack_array.push(3)
print("Top element:", stack_array.peek())  
print("Pop element:", stack_array.pop())   
print("Is stack empty?", stack_array.is_empty())  
print("Stack size:", stack_array.size())  




#Using Linked Lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        popped_element = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_element

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.size

print("\nStack using Linked List:")
stack_linked_list = StackLinkedList()
stack_linked_list.push(1)
stack_linked_list.push(2)
stack_linked_list.push(3)
print("Top element:", stack_linked_list.peek()) 
print("Pop element:", stack_linked_list.pop())
print("Is stack empty?", stack_linked_list.is_empty())  
print("Stack size:", stack_linked_list.size())  
