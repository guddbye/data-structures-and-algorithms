from data_structures.stack import Stack


def multi_bracket_validation(string):
    """
    Given a string of brackets, return True if the brackets are balanced and False otherwise.
    """
    open_stack = Stack()
    openers = ["{","[","("]
    closers = ["}","]",")"]
    pairs = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for char in string:
        if char in openers:
            open_stack.push(char)

        elif char in closers:

            if open_stack.is_empty():

                return False

            else:
                if pairs[char] != open_stack.pop():
                    return False

    return True

