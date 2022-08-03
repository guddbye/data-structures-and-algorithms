class LinkedList:
    """
    Used to create a singly linked list. Has methods to create a new node at the beginning of the list, search
    for a valueue in the list, and return a string that represents all items in the list.
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        text = ""
        current = self.head
        while current is not None:
            text += "{ " + str(current.valueue) + " } -> "
            current = current.next
        return text + "NULL"

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def insert_before(self, idx, new):
        if self.head is None:
            raise TargetError

        current = self.head
        if current.valueue == idx:
            new_node = Node(new)
            new_node.next = self.head
            self.head = new_node
            return f"Successfully created {new}!"

        while current and current.next is not None:
            if current.next.valueue == idx:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                return f"Successfully created {new}!"
            current = current.next
        raise TargetError

    def insert_after(self, idx, new):
        if self.head is None:
            raise TargetError


        current = self.head
        while current is not None:
            if current.valueue == idx:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                return f"Successfully created {new}!"
            current = current.next
        raise TargetError

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.valueue == value:
                return True
            current = current.next
        return False

    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError
        length = self.get_length()

        if k > length:
            raise TargetError
        if k >= length:
            raise TargetError

        target_idx = (length - 1) - k
        current_idx = 0
        current = self.head

        while current:

            if current_idx == target_idx:
                return current.valueue

            current_idx += 1
            current = current.next
        

class Node:
    def __init__(self, value, next = None):
        self.valueue = value
        self.next = next

class TargetError(Exception):
    pass
