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
        while self.stack_2.top:
            self.stack_1.push(self.stack_2.pop())
        self.stack_1.push(value)

    def dequeue(self):
        while self.stack_1.top:
            self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()

    # def is_empty(self):
    #     return self.stack_1.is_empty() and self.stack_2.is_empty()


class DuckDuckGoose():
    """ Write a function called DuckDuckGoose() that accepts some strings and an int K. Use a enqueue and dequeue.
    """

    def __init__(self, strings, k):
        self.strings = strings
        self.k = k
        self.queue = PseudoQueue()
        for string in strings:
            self.queue.enqueue(string)

    def play(self):
        for _ in range(self.k):
            self.queue.dequeue()
        return self.queue.dequeue()
