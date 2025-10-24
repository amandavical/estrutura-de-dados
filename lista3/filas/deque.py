class Deque:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def add_first(self, item):
        if self.isFull():
            print("Deque cheio")
            return
        self.front = (self.front - 1) % self.capacity
        self.items[self.front] = item
        self.size += 1

    def add_last(self, item):
        if self.isFull():
            print("Deque cheio")
            return
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def delete_first(self):
        if self.isEmpty():
            print("Deque vazio")
            return None
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def delete_last(self):
        if self.isEmpty():
            print("Deque vazio")
            return None
        self.rear = (self.rear - 1) % self.capacity
        item = self.items[self.rear]
        self.size -= 1
        return item

    def first(self):
        if self.isEmpty():
            print("Deque vazio")
            return None
        return self.items[self.front]

    def last(self):
        if self.isEmpty():
            print("Deque vazio")
            return None
        return self.items[(self.rear - 1) % self.capacity]

    def back(self):  # sinônimo de last()
        return self.last()

    def __str__(self):
        if self.isEmpty():
            return "Deque vazio"
        result = []
        current = self.front
        for _ in range(self.size):
            result.append(self.items[current])
            current = (current + 1) % self.capacity
        return "Deque: " + str(result)