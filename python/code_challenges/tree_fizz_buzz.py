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

    clone = tree.clone()
    breadth_first = Queue()
    breadth_first.enqueue(clone.root)

    while not breadth_first.is_empty():
        front = breadth_first.dequeue()
        # print(front.value)
        front.value = fizz_buzz(front.value)
        # print(front.value)
        print(front.children)
        for child in front.children:
            breadth_first.enqueue(child)

    return
