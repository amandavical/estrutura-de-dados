class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = Node(data, self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError("Stack Underflow")
        temp = self.head.data
        self.head = self.head.next
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError("Stack is Empty")
        return self.head.data

    def isEmpty(self):
        return self.head is None