from data_structures.queue import Queue

class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, pet):
        if pet.type == 'dog':
            self.dogs.enqueue(pet)
        elif pet.type == 'cat':
            self.cats.enqueue(pet)

    def dequeue(self, picked):
        if picked == "dog" and self.dogs:
            return self.dogs.dequeue()
        if picked == "cat" and self.cats:
            return self.cats.dequeue()

class Dog:
    def __init__(self):
        self.type = 'dog'


class Cat:
    def __init__(self):
        self.type = 'cat'
