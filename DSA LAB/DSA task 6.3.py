class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def is_balanced(self):
        def check_balance(node):
            if node is None:
                return 0, True 

            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)

            current_height = max(left_height, right_height) + 1

            if abs(left_height - right_height) <= 1 and left_balanced and right_balanced:
                return current_height, True
            else:
                return current_height, False

        _, balanced = check_balance(self.root)
        return balanced

def test_is_balanced():
    tree1 = BinaryTree()
    tree1.root = Node(10)
    tree1.root.left = Node(5)
    tree1.root.right = Node(20)
    tree1.root.left.left = Node(3)
    tree1.root.left.right = Node(7)
    tree1.root.right.left = Node(15)
    tree1.root.right.right = Node(25)

    print("Tree 1 is balanced:", tree1.is_balanced()) 

    tree2 = BinaryTree()
    tree2.root = Node(10)
    tree2.root.left = Node(5)
    tree2.root.left.left = Node(3)
    tree2.root.left.left.left = Node(1)

    print("Tree 2 is balanced:", tree2.is_balanced())  

    tree3 = BinaryTree()
    print("Tree 3 is balanced:", tree3.is_balanced()) 

    tree4 = BinaryTree()
    tree4.root = Node(42)
    print("Tree 4 is balanced:", tree4.is_balanced())  

if __name__ == "__main__":
    test_is_balanced()
