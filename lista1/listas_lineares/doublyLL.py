class Node:
    """
    A classe Node deve conter os atributos data, next e prev, que armazenam, respectivamente, o valor
    do nó, a referência para o próximo nó e a referência para o nó anterior.
    """

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def hasNext(self):
        return self.next != None

    def hasPrev(self):
        return self.prev != None


class DoublyLL:
    """
    A classe DoublyLL mantém referências para o primeiro nó (head) e para o último nó (tail), além
    de conter os métodos de inserção, remoção e utilitários da lista.
    """

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def insertAtGivenPosition(self, pos, data):
        if self.head == None or pos == 0:
            self.insertAtBeginning(data)
        elif pos == self.length:
            self.insertAtEnd(data)
        elif pos < self.length:
            curr = self.head
            count = 0
            while curr != None and count < pos:
                curr = curr.next
                count += 1
            newNode = Node(data)
            newNode.next = curr.next
            newNode.prev = curr
            curr.next = newNode
            self.length += 1

    def insertAtBeginning(self, data):
        newNode = Node(data, None, None)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.length += 1

    def insertAtEnd(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            newNode = Node(data)
            newNode.prev = current
            newNode.next = None
            current.next = newNode
            self.length += 1

    def print(self):
        if self.length != 0:
            pos = 0
            current = self.head
            while current is not None:
                print("Node %d has value %s" % (pos, current.data))
                pos += 1
                current = current.next


list = DoublyLL()
list.insertAtBeginning(10)
list.insertAtBeginning(20)
list.insertAtBeginning(30)
list.insertAtGivenPosition(1, 40)
list.insertAtEnd(50)
list.print()
