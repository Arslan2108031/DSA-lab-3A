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

    def find_lca(self, n1, n2):
        return self._find_lca_recursive(self.root, n1, n2)

    def _find_lca_recursive(self, current, n1, n2):
        if current is None:
            return None

        if n1 < current.value and n2 < current.value:
            return self._find_lca_recursive(current.left, n1, n2)

        if n1 > current.value and n2 > current.value:
            return self._find_lca_recursive(current.right, n1, n2)

        return current

    def inorder_traversal(self):
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, current):
        if current:
            self._inorder_recursive(current.left)
            print(current.value, end=" ")
            self._inorder_recursive(current.right)

def test_lca():
    bst = BinarySearchTree()
    nodes = [20, 10, 30, 5, 15, 25, 35]
    for node in nodes:
        bst.insert(node)

    print("Inorder Traversal of BST:")
    bst.inorder_traversal()

    lca = bst.find_lca(5, 15)
    print(f"LCA of 5 and 15: {lca.value}")  

    lca = bst.find_lca(5, 25)
    print(f"LCA of 5 and 25: {lca.value}")  

    lca = bst.find_lca(25, 35)
    print(f"LCA of 25 and 35: {lca.value}")  

if __name__ == "__main__":
    test_lca()
