from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    A Linked List as the underlying data storage mechanism, implement both a Stack and a Queue
    """

    def __init__(self):
        self.top = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, element):
        self.top = Node(element, self.top)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection.")
        result = self.top.value
        self.top = self.top.next
        self.size -= 1
        return result

    def peek(self):
        # method body here
        if self.is_empty():
            raise InvalidOperationError("Method now allowed on empty collection.")
        return self.top.value

class Node:
    def __init__(self, element, next_):
        self.value = element
        self.next = next_
