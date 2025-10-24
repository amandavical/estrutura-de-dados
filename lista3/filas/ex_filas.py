from ...lista2.pilhas.stack import *
from lista3.filas.queue import * 

'''Implemente um algoritmo para inverter uma fila usando uma pilha'''

def inverter_fila_com_pilha(q: Queue ):
    if q.isEmpty():
        return None
    s = Stack()
    while not q.isEmpty():
        s.push(q.deQueue())
    while not s.isEmpty():
        q.enQueue(s.pop())
        
    return q 

'''Implemente um algoritmo para inverter uma pilha usando uma fila.'''
def inverter_pilha_com_fila(s: Stack):
   while s.isEmpty():
       return None 
   q = Queue()

   while not s.isEmpty():
       q.enQueue(s.pop())
   while not q.isEmpty():
       s.push(q.deQueue())
    
   return s

'''Dado um inteiro k e uma fila de inteiros, implemente um algoritmo
que inverta a ordem os primeiros k elementos da fila'''
def inverter_primeiros_k(q: Queue, k:int): # 1 2 3 4 5 , 3
    if q.isEmpty(): 
        return None 
    s = Stack()
    for i in range(k): 
        s.push(q.deQueue()) # s 3 2 1 , q 4 5 
    while not s.isEmpty():
        q.enQueue(s.pop()) # 4 5 3 2 1 
    for i in range(q.size - k): #coloca o resto do inicio para o fim de novo, 5 - 3 = 2 
        q.enQueue(q.deQueue()) # 3 2 1 4 5
    return q


    
    