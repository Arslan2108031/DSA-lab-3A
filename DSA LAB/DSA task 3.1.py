class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for _ in range(position - 1):
            if not temp:
                print("Position out of bounds")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_by_value(self, value):
        temp = self.head
        if temp and temp.data == value:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Value not found")
            return
        prev.next = temp.next
        temp = None

    def search_by_value(self, value):
        temp = self.head
        position = 0
        while temp:
            if temp.data == value:
                return position
            position += 1
            temp = temp.next
        return -1 

    def display(self):
        temp = self.head
        if not temp:
            print("Linked list is empty.")
            return
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_beginning(1)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(3)
    print("After inserting at beginning:")
    sll.display()
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    print("After inserting at end:")
    sll.display()
    sll.insert_at_position(6, 2)
    print("After inserting 6 at position 2:")
    sll.display()
    sll.delete_by_value(3)
    print("After deleting node with value 3:")
    sll.display()
    position = sll.search_by_value(4)
    if position != -1:
        print(f"Found value 4 at position {position}.")
    else:
        print("Value 4 not found.")

    position = sll.search_by_value(10)
    if position != -1:
        print(f"Found value 10 at position {position}.")
    else:
        print("Value 10 not found.")
