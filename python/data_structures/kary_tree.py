from data_structures.queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root


    def breadth_first(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()


            if node.value % 2 == 1:
                node.value *= 2
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []
