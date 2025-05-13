class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        temp = self.head
        if not temp:
            print("Linked list is empty.")
            return
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

    def detect_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    def find_start_of_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  
                break
        else:
            return None  

        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    def remove_loop(self):
        loop_start = self.find_start_of_loop()

        if loop_start is None:
            print("No loop detected.")
            return

        temp = loop_start
        while temp.next != loop_start:
            temp = temp.next

        temp.next = None

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    loop_node = sll.head
    while loop_node.next:
        loop_node = loop_node.next
    loop_node.next = sll.head.next.next 
    print("Before removing loop:")
    sll.display()

    if sll.detect_loop():
        print("Loop detected.")
        loop_start = sll.find_start_of_loop()
        print(f"Loop starts at node with value: {loop_start.data}")
        sll.remove_loop()
        print("Loop removed.")
    else:
        print("No loop detected.")

    print("After removing loop:")
    sll.display()
