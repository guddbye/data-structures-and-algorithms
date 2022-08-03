from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Data structure that stores values in linked nodes.
    Uses Last In First Out (LIFO) to access the nodes in the stack.
    """

    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection.")
        result = self.top.value
        self.top = self.top.next
        self.size -= 1
        return result

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method now allowed on empty collection.")
        return self.top.value

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
class Node:
    def __init__(self, element, next_=None):
        self.value = element
        self.next = next_
