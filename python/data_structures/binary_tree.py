class BinaryTree:
    """
    Construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way. 
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return values

    def in_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            values.append(root.value)
            walk(root.right)

        walk(self.root)
        return values

    def post_order(self):
        values = []

        def walk(root):
            if root is None:
                return
            walk(root.left)
            walk(root.right)
            values.append(root.value)

        walk(self.root)
        return values

class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
