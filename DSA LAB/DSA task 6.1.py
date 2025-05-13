class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current, value):
        if current is None:
            return None

        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            successor = self._min_value_node(current.right)
            current.value = successor.value
            current.right = self._delete_recursive(current.right, successor.value)

        return current

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, current):
        if current:
            self._inorder_recursive(current.left)
            print(current.value, end=" ")
            self._inorder_recursive(current.right)

def test_bst():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("Inorder Traversal after insertions:")
    bst.inorder_traversal()  

    print("Search 40:", bst.search(40))  
    print("Search 90:", bst.search(90)) 

    bst.delete(20) 
    print("After deleting 20:")
    bst.inorder_traversal() 

    bst.delete(30)  
    print("After deleting 30:")
    bst.inorder_traversal()  

    bst.delete(50)  
    print("After deleting 50:")
    bst.inorder_traversal()

if __name__ == "__main__":
    test_bst()
