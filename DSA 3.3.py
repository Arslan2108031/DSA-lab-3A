class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None
            return
        count = 0
        while temp:
            if count == position:
                break
            temp = temp.next
            count += 1
        if temp is None:
            print("Position out of bounds.")
            return
        temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        temp = None

    def traverse_forward(self):
        temp = self.head
        if temp is None:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

    def traverse_reverse(self):
        temp = self.head
        if temp is None:
            print("List is empty.")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ← ")
            temp = temp.prev
        print("None")

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_at_beginning(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(5)

    print("Linked List (Forward):")
    dll.traverse_forward()

    print("Linked List (Reverse):")
    dll.traverse_reverse()

    dll.delete_at_position(2)

    print("\nAfter Deleting Node at Position 2:")
    dll.traverse_forward()

    print("After Deleting Node at Position 2 (Reverse):")
    dll.traverse_reverse()
