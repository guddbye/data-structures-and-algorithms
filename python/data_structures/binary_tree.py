from data_structures.queue import Queue

class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None
        self.max = None

    def pre_order(self):
        def walk(root, data):
            if not root:
                return

            data.append(root.value)
            walk(root.left, data)
            walk(root.right, data)

        data_values = []
        walk(self.root, data_values)
        return data_values


    def in_order(self):
        def walk(root, data):
            if not root:
                return

            walk(root.left, data)
            data.append(root.value)
            walk(root.right, data)

        data_values = []
        walk(self.root, data_values)
        return data_values

    def post_order(self):
        def walk(root, data):
            if not root:
                return

            walk(root.left, data)
            walk(root.right, data)
            data.append(root.value)

        data_values = []
        walk(self.root, data_values)
        return data_values

    def find_max(self):
        def walk(root):
            if not root:
                return
            if self.max is None:
                self.max = root.value
            if root.value > self.max:
                self.max = root.value
            walk(root.left)
            walk(root.right)
        walk(self.root)
        return self.max

    def add(self, data):

        node = Node(data)

        if not self.root:
            self.root = node
            return

        breadth = Queue()

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            if not front.left:
                front.left = node
                return
            else:
                breadth.enqueue(front.left)
            if not front.right:
                front.right = node
                return
            else:
                breadth.enqueue(front.right)
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
