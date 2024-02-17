import time


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, node):
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def pop_head(self):
        if self.head:
            ret = self.head
            self.head = self.head.next
            return ret
        return None

    def size(self):
        cur = self.head
        size = 0
        while cur:
            size += 1
            cur = cur.next
        return size


class Animal:
    def __init__(self, name):
        self.timestamp = time.time()
        self.name = name


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class AnimalShelter(LinkedList):
    def enqueue(self, animal):
        animal_node = Node(animal)
        self.insert(animal_node)

    def dequeue_any(self):
        return super().pop_head()

    def dequeue_cat(self):
        prev = None
        cur = self.head
        while cur:
            if isinstance(cur.data, Cat):
                prev.next = cur.next
                return cur.data
            prev = cur
            cur = cur.next
        return None

    def dequeue_dog(self):
        prev = None
        cur = self.head
        while cur:
            if isinstance(cur.data, Dog):
                prev.next = cur.next
                return cur.data
            prev = cur
            cur = cur.next
        return None


def test_enqueue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("c1"))
    animal_shelter.enqueue(Dog("d1"))
    animal_shelter.enqueue(Cat("c2"))
    assert animal_shelter.size() == 3

    animal_shelter.enqueue(Cat("c3"))
    animal_shelter.enqueue(Dog("d2"))
    animal_shelter.enqueue(Cat("c4"))

    assert animal_shelter.dequeue_any().data.name == "c1"
    assert animal_shelter.dequeue_cat().name == "c2"
    assert animal_shelter.dequeue_any().data.name == "d1"
    assert animal_shelter.dequeue_dog().name == "d2"


if __name__ == "__main__":
    test_enqueue()
