from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if animal == "dog":
            self.dogs.enqueue(animal)
        elif animal == "cat":
            self.cats.enqueue(animal)
        else:
            raise InvalidOperationError("Invalid animal type.")

    def dequeue(self, pref):
        if pref == "dog":
            while not self.dogs.is_empty():
                self.cats.enqueue(self.dogs.dequeue())
            return self.dogs.dequeue()
        elif pref == "cat":
            while not self.cats.is_empty():
                self.dogs.enqueue(self.cats.dequeue())
            return self.cats.dequeue()
        else:
            raise InvalidOperationError("Invalid animal type.")

class Dog:
    def __init__(self):
        self.type = "dog"

class Cat:
    def __init__(self):
        self.type = "cat"
