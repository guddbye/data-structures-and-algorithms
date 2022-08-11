from data_structures.kary_tree import KaryTree
from data_structures.queue import Queue


def fizz_buzz_tree(tree):

    def fizz_buzz(num):
        if num % 15 == 0:
            return "FizzBuzz"

        elif num % 3 == 0:
            return "Fizz"

        elif num % 5 == 0:
            return "Buzz"

        else:
            return str(num)

    if tree.root is None:
        return None

    breadth = Queue()
    breadth.enqueue(tree.root)
    clone = tree.clone()


    while not breadth.is_empty():
        front = breadth.dequeue()
        front.value = fizz_buzz(front.value)
        print(front.children)
        for child in front.children:
            breadth.enqueue(child)

    return clone
