from linkedList import *

"""
Dada uma lista simplesmente encadeada que armazena apenas números inteiros,
crie uma função em Python que remova todos os números pares. 
Exemplo L = [1->2->6->13->34->None] Saída L=[1->13->None].
"""


def remove_pares(head):
    if head is None:
        return 0

    current = prev = head

    while current is not None:
        if current.data % 2 == 0:
            if head == current:  # remove par do inicio
                prev = head = current.next
            else:
                prev.next = current.next
        else:
            prev = current
        current = current.next

    return head


# Montando a lista [1 -> 2 -> 6 -> 13 -> 34 -> None]
ll = LinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(6)
ll.insertAtEnd(13)
ll.insertAtEnd(34)

print("Antes de remover pares:")
ll.print()

# Chama a função remove_pares passando o head da lista
ll.setHead(remove_pares(ll.getHead()))

print("Depois de remover pares:")
ll.print()

"""
Dada uma lista simplesmente encadeada que armazena apenas números inteiros, 
crie uma função em Python que devolva a soma de todos os números ímpares.

"""


def SomaImpares(head):
    if head is None:
        return 0

    current = head
    total = 0

    while current != None:
        if current.data % 2 == 1:
            total = total + current.data
        current = current.next

    return total


l2 = LinkedList()
l2.insertAtEnd(1)
l2.insertAtEnd(2)
l2.insertAtEnd(6)
l2.insertAtEnd(13)
l2.insertAtEnd(34)

print("Soma dos impares:")
print(SomaImpares(l2.getHead()))

"""
Crie uma função que dada uma lista simplesmente encadeada, devolva duas listas circulares com metade dos elementos da primeira. 
Exemplo: L=[1->2->6->13->34->None] Saída: L1=[1->2->]; L2=[6->13->34->].
"""


def quebrarLista(head):
    if head is None:
        return LinkedList(), LinkedList()  # duas listas vazias

    if head.next is None:
        l1 = LinkedList()
        l1.insertAtEnd(head.data)
        return l1, LinkedList()  # segunda lista vazia

    slow = head
    fast = head
    prev_slow = None

    # Encontra o meio
    while fast is not None and fast.next is not None:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next

    # Divide a lista em duas partes
    L1_head = head
    L2_head = slow
    prev_slow.next = None  # separa a primeira metade da segunda

    # Cria LinkedList para cada metade
    l1 = LinkedList()
    current = L1_head
    while current is not None:
        l1.insertAtEnd(current.data)
        current = current.next

    l2 = LinkedList()
    current = L2_head
    while current is not None:
        l2.insertAtEnd(current.data)
        current = current.next

    # Torna circulares
    if l1.head:
        last = l1.getNodeAtPosition(l1.length - 1)
        last.next = l1.head

    if l2.head:
        last = l2.getNodeAtPosition(l2.length - 1)
        last.next = l2.head

    return l1, l2


l3 = LinkedList()
for x in [1, 2, 6, 13, 34]:
    l3.insertAtEnd(x)

l1, l2 = quebrarLista(l3.getHead())

print("L1 (circular):")
l1.print()

print("L2 (circular):")
l2.print()

"""
Dada duas listas simplesmente encadeadas,
crie uma função em python que as entrelace. 
Exemplo: L1=[1->2->3->None] L2=[4->5->6->None] 
Saída: L3=[1->4->2->5->3->6->None].
"""


def entrelacarListas(l1, l2):
    if l1.head is None:
        return l2
    if l2.head is None:
        return l1

    l3 = LinkedList()
    current1 = l1.head
    current2 = l2.head
    while current1 is not None and current2 is not None:
        l3.insertAtEnd(current1.data)
        l3.insertAtEnd(current2.data)
        current1 = current1.next
        current2 = current2.next
    if current1 is not None:
        l3.insertAtEnd(current1.data)
    if current2 is not None:
        l3.insertAtEnd(current2.data)
    return l3


l4 = LinkedList()
l4.insertAtEnd(1)
l4.insertAtEnd(2)
l4.insertAtEnd(3)

l5 = LinkedList()
l5.insertAtEnd(4)
l5.insertAtEnd(5)
l5.insertAtEnd(6)

l6 = entrelacarListas(l4, l5)

print("L3:")
l6.print()
