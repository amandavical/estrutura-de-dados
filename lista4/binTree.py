
from filaArvore import *
from stackArvore import *

class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None
        self.father = None
        self.isLeft = False

    def setLeft(self, data):
        self.left = Node(data)
        self.left.isLeft = True
        self.left.father = self

    def setRight(self, data):
        self.right = Node(data)
        self.right.isLeft = False
        self.right.father = self

class BinTree:
    def __init__(self, root = None):
        self.root =root

    def preOrder(self, root):
        if root == None:
            return
        print(root.data,sep="-->", end="-->")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inverseLevelOrder(self,root):
        if not root: return
        s = Stack()
        q = Queue()
        q.enQueue(root)
        while not q.isEmpty():
            n = q.deQueue()
            s.push(n)
            if n.left: q.enQueue(n.left)
            if n.right: q.enQueue(n.right)
        while not s.isEmpty():
            n = s.pop()
            print(n.data,sep="-->", end="-->")


    def levelOrder(self, root):
        if not root: return
        q = Queue()
        q.enQueue(root)
        while not q.isEmpty():
            n = q.deQueue()
            print(n.data,sep="-->", end="-->")
            if n.left: q.enQueue(n.left)
            if n.right: q.enQueue(n.right)

    def preOrderIterative(self,root, result):

        if not root:
            return
        s = Stack()
        s.push(root)
        while not s.isEmpty():
            n = s.pop()
            result.append(n.data)
            if n.right: s.push(n.right)
            if n.left: s.push(n.left)


    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        print(root.data,sep="-->", end="-->")
        self.inOrder(root.right)

    def inOrderIterative(self,root,result):
        if not root:
            return
        s = Stack()
        n = root
        while n or not s.isEmpty():
            if n:
                s.push(n)
                n = n.left
            else:
                n = s.pop()
                result.append(n.data)
                n = n.right

    def postOrder(self, root):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data,sep="-->", end="-->")

    def postOrderIterative(self, root, result):
        if root == None:
            return
        visited = []
        s = Stack()
        n = root
        while n or not s.isEmpty():
            if n:
                s.push(n)
                n = n.left
            else:
                n = s.pop()
                if n.right and not n.right in visited:
                    s.push(n)
                    n = n.right
                else:
                    visited.add(n)
                    result.append(n.data)
                    n = None

    def morris_inorder_traversal(root):
      current = root 
      while current:
        if not current.left:
            print(current.data, end = " ")
            current = current.right 
        else:
            predecessor = current.left 
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right 
            
            if not predecessor.right:
                predecessor.right = current 
                current = current.left 
            else:
                predecessor.right = None
                print(current.data, end=" ")
                current = current.right
