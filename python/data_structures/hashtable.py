from data_structures.linked_list import LinkedList

class Hashtable:

    def __init__(self, size=1024):
        self.buckets = [None] * size
        self.size = size

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            bucket = LinkedList()
            self.buckets[index] = bucket

        drop = (key, value)
        bucket.insert(drop)

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            return None

        current = bucket.head
        while current:
            key_value_pair = current.value
            if key_value_pair[0] == key:
                return key_value_pair[1]
            current = current.next

        return None

    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            return False

        current = bucket.head
        while current:
            key_value_pair = current.value
            if key_value_pair[0] == key:
                return True
            current = current.next

        return False

    def keys(self):
        gathered_keys = []
        for bucket in self.buckets:
            if bucket:
                current = bucket.head
                while current:
                    key_value_pair = current.value
                    gathered_keys.append(key_value_pair[0])
                    current = current.next

        return gathered_keys

    def hash(self, key):
        ascii_values = [ord(char) for char in key]
        ascii_sum = sum(ascii_values)
        primed = ascii_sum * 420
        index = primed % self.size
        return index
