from data_structures.stack import Stack


class PseudoQueue:
    """
    Utilizes two separate Stacks to create a Queue.
    Has methods to both enqueue and dequeue a node.
    """

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        self.stack_1.push(value)

    def dequeue(self):
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()

    def is_empty(self):
        return self.stack_1.is_empty() and self.stack_2.is_empty()

    def __str__(self):
        return f"PseudoQueue: {self.stack_1} {self.stack_2}"


