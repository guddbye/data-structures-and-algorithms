from data_structures.stack import Stack


class PseudoQueue:
    """
    Utilizes two separate Stacks to create a Queue.
    Has methods to both enqueue and dequeue a node.
    """
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, val):
        while self.out_stack.top:
            self.in_stack.push(self.out_stack.pop())
        self.in_stack.push(val)

    def dequeue(self):
        while self.in_stack.top:
            self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()
        
class DuckDuckGoose():
    """ 
    Write a function called DuckDuckGoose() that accepts some strings and an int K. Use a enqueue and dequeue.
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

