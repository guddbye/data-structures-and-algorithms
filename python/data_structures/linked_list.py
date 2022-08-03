class Node:
    """
    Create new node object for linked list to use
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Create a linked list that:
Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list
    """

    def __init__(self):
        # initialization here
        self.head = None

    def insert(self, value):
        # method body here
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        # method body here
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        text = ""
        current = self.head
        while current is not None:
            text += "{ " + str(current.value) + " } -> "
            current = current.next
        return text + "NULL"

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
        if current.value == idx:
            new_node = Node(new)
            new_node.next = self.head
            self.head = new_node
            return f"Successfully created {new}!"

        while current and current.next is not None:
            if current.next.value == idx:
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
            if current.value == idx:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                return f"Successfully created {new}!"
            current = current.next
        raise TargetError


class TargetError:
    pass
