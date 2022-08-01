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
        pass

    def insert(self, value):
        # method body here
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        pass

    def includes(self, value):
        # method body here
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
        pass

    def __str__(self):
        # method body here
        current = self.head
        string = ""
        while current:
            string += str(current.value) + " -> "
            current = current.next
        return string[:-4]
        pass


class TargetError:
    pass
