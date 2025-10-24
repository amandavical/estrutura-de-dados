class Queue(object):
    def __init__(self, limit=5):
        self.que=[None]*limit
        self.limit = limit
        self.front = 0
        self.rear = 0
        self.size = 0
    def isEmpty(self):
        return self.size <= 0

    def enQueue(self,item):
        if self.size == self.limit:
            return
        else:
            self.que[int(self.rear)] = item
            self.rear = (self.rear+1)%self.limit
            self.size += 1

    def deQueue(self):
        if self.size == 0:
            return
        else:
            item = self.que[int(self.front)]
            self.front = (self.front+1)%self.limit
            self.size -= 1
            return item

    def queueRear(self):
        if self.size > 0:
            return self.que[int(self.rear)]
        else:
            raise IndexError
    def queueFront(self):
        if self.size > 0:
            return self.que[int(self.front)]
        else:
            raise IndexError

    def size(self):
        return self.size