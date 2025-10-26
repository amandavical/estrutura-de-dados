class Node:
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

class Stack():
  def __init__(self,data=None):
    self.head = None
    if data:
      for data in data:
        self.push(data)
  def push(self, data):
    temp = Node()
    temp.data = data
    temp.next = self.head
    self.head = temp
  def pop(self):
    if self.head is None:
      raise IndexError
    temp = self.head.data
    self.head = self.head.next
    return temp
  def peek(self):
    if self.head is None:
      raise IndexError
    return self.head.data
  def isEmpty(self):
    return self.head == None