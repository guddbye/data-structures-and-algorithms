from data_structures.linked_list import LinkedList
Linked = LinkedList

def zip_lists(a, b):
    """
    Given two linked lists, zip them together into one list.
    """
    
    if a is None or b is None:
        return None
    else:
        a_node = a.head
        b_node = b.head
        new_list = Linked()
        while a_node is not None and b_node is not None:
            new_list.append(a_node.data)
            new_list.append(b_node.data)
            a_node = a_node.next
            b_node = b_node.next
        return new_list
