class Node:
    """
    Cada nó da lista será representado pela classe Node. Essa classe contem dois atributos principais: o
    dado armazenado (data) e a referencia para o próximo nó (next).
    Tambem incluimos metodos getters
    e setters para facilitar o acesso e a modificacao desses atributos
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None


class LinkedList(object):
    """
    Cria uma lista encadeada
    A classe LinkedList será responsável por armazenar a referência ao primeiro nó (head) e manter o
    controle do tamanho da lista. Com apenas a referência ao nó cabeça, conseguimos acessar todos os
    outros nós da estrutura.
    """

    def __init__(self):
        self.length = 0
        self.head = None

    def setHead(self, Node):
        self.head = Node

    def getHead(self):
        return self.head

    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.data = data
        if self.length == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertAtGivenPosition(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.data = data
                    count = 1
                    current = self.head
                    while count < pos - 1:
                        count += 1
                        current = current.next
                    newNode.next = current.next
                    current.next = newNode
                    self.length += 1

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.data = data
        if self.length == 0:
            self.head = newNode
            self.length += 1
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        self.length += 1

    def deleteAtPosition(self, pos):
        count = 0
        currentNode = self.head
        previousNode = self.head

        if pos > self.length or pos < 0:
            return None
        else:
            while currentNode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousNode.next = currentNode.next
                    self.length -= 1
                    return
                else:
                    previousNode = currentNode
                    currentNode = currentNode.next

    def deleteFromBeginning(self):
        if self.length != 0:
            self.head = self.head.next
            self.length -= 1

    def deleteFromEnd(self):
        if self.length != 0:
            currentNode = self.getHead()
            previousNode = self.getHead()
            while currentNode.next != None:
                previousNode = currentNode
                currentNode = currentNode.next
            previousNode.next = None
            self.length -= 1

    def print(self):
        if self.length != 0:
            pos = 0
            current = self.head
            while current != None:
                print("Node %d has value %s" % (pos, current.data))
                pos += 1
                if pos == self.length:
                    return
                current = current.next

    def getNodeAtPosition(self, index):
        if self.length != 0:
            current = self.head
            i = 0
            while (current != None) and (i < index):
                current = current.next
                i += 1
            return current
        else:
            return None
