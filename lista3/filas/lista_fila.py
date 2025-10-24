from deque import Deque
from stack import *
from queue import Queue
'''
4 - Considere um deque D que contém os números (1,2,3,4,5,6,7,8), nessa ordem. Suponha ainda que há uma fila Q, inicialmente vazia. 
Elabore um trecho de código que usando apenas D e Q (sem variáveis adicionais) e resulte em Q armazenando os elementos na ordem (1,2,3,4,5,6,7,8).
'''
def transferir_deque_para_fila(d: Deque, q: Queue):
    while not d.isEmpty():
        elem = d.delete_first()
        q.enQueue(elem)
    
    
# TESTE
print("=== TESTE TRANSFERIR DEQUE → FILA ===")

# Criar deque com (1,2,3,4,5,6,7,8)
D = Deque()
for i in range(1, 9):
    D.add_last(i)

print("Deque D inicial:", D)

# Criar fila vazia
Q = Queue(10)

# Transferir
transferir_deque_para_fila(D, Q)

print("Deque D após transferência:", D)
print("Fila Q após transferência:", end=" ")

# Mostrar conteúdo da fila
while not Q.isEmpty():
    print(Q.deQueue(), end=" ")

'''
5 - Implemente uma fila através de duas pilhas. 
Não crie variáveis, use apenas as operações das pilhas e não use recursão.
'''
class QueueTwoStacks:
    def __init__(self, capacity=10):
        self.S1 = Stack(capacity)  # Pilha de entrada - onde novos elementos chegam
        self.S2 = Stack(capacity)  # Pilha de saída - de onde atendemos os elementos

    def enQueue(self, item):
        # Simples: sempre empilha em S1
        # Exemplo: enQueue(1) → S1 = [1]
        #          enQueue(2) → S1 = [1, 2]  
        #          enQueue(3) → S1 = [1, 2, 3]
        self.S1.push(item)

    def deQueue(self):
        # Se S2 estiver vazia, transfere tudo de S1 para S2
        # Exemplo: S1 = [1, 2, 3], S2 = []
        # while: S1.pop() = 3 → S2.push(3) → S2 = [3]
        #        S1.pop() = 2 → S2.push(2) → S2 = [3, 2]  
        #        S1.pop() = 1 → S2.push(1) → S2 = [3, 2, 1]
        # Agora S1 = [], S2 = [3, 2, 1] (1 no topo - que era o primeiro da fila!)
        if self.S2.isEmpty():
            while not self.S1.isEmpty():
                self.S2.push(self.S1.pop())
        
        # Agora o mais antigo está no topo de S2
        # Exemplo: S2.pop() → remove 1 (que foi o primeiro a entrar)
        if self.S2.isEmpty():
            print("Fila vazia")
            return None
        return self.S2.pop()

# === EXEMPLO COMPLETO ===
# Vamos simular passo a passo:

# Criar fila
fila = QueueTwoStacks()

# enQueue(1): S1 = [1], S2 = []
# enQueue(2): S1 = [1, 2], S2 = []  
# enQueue(3): S1 = [1, 2, 3], S2 = []

# deQueue() - primeiro atendimento:
#   S2 vazia? SIM → transfere S1 para S2
#   S1 = [], S2 = [3, 2, 1] (1 no topo)
#   S2.pop() → retorna 1 ✅ (primeiro que entrou)

# deQueue() - segundo atendimento:
#   S2 vazia? NÃO → S2 = [3, 2] (2 no topo)  
#   S2.pop() → retorna 2 ✅ (segundo que entrou)

# enQueue(4): S1 = [4], S2 = [3]

# deQueue() - terceiro atendimento:
#   S2 vazia? NÃO → S2 = [3] (3 no topo)
#   S2.pop() → retorna 3 ✅ (terceiro que entrou)

# deQueue() - quarto atendimento:
#   S2 vazia? SIM → transfere S1 para S2: S1 = [4] → S2 = [4]
#   S2.pop() → retorna 4 ✅ (quarto que entrou)

'''
6 - Implemente um deque através de duas pilhas. Não crie variáveis, use apenas as 
operações das pilhas e não use recursão. 
'''
class Deque:
    def __init__(self, capacity):
        self.frontStack = Stack(capacity)  # Pilha para elementos do início do deque
        self.backStack = Stack(capacity)   # Pilha para elementos do final do deque

    def push_front(self, data):
        # Inserir na frente → empilha direto em frontStack
        # Exemplo: push_front(1) → frontStack = [1], backStack = []
        #          push_front(2) → frontStack = [2, 1], backStack = []
        self.frontStack.push(data)

    def push_back(self, data):
        # Inserir no fim → empilha direto em backStack
        # Exemplo: push_back(3) → frontStack = [2, 1], backStack = [3]
        #          push_back(4) → frontStack = [2, 1], backStack = [3, 4]
        self.backStack.push(data)

    def pop_front(self):
        # Se frontStack está vazio, move tudo de backStack pra frontStack
        # Exemplo: frontStack = [], backStack = [3, 4, 5] 
        #          → frontStack = [5, 4, 3], backStack = []
        if self.frontStack.isEmpty():
            while not self.backStack.isEmpty():
                self.frontStack.push(self.backStack.pop())

        # Agora o elemento da frente está no topo de frontStack
        # Exemplo: frontStack.pop() → remove 3 (que era o primeiro de backStack)
        if self.frontStack.isEmpty():
            print("Deque Underflow (vazio na frente)")
            return None
        return self.frontStack.pop()

    def pop_back(self):
        # Se backStack está vazio, move tudo de frontStack pra backStack
        # Exemplo: frontStack = [2, 1], backStack = []
        #          → backStack = [1, 2], frontStack = []
        if self.backStack.isEmpty():
            while not self.frontStack.isEmpty():
                self.backStack.push(self.frontStack.pop())

        # Agora o elemento do final está no topo de backStack
        # Exemplo: backStack.pop() → remove 2 (que era o primeiro de frontStack)
        if self.backStack.isEmpty():
            print("Deque Underflow (vazio atrás)")
            return None
        return self.backStack.pop()

    def peek_front(self):
        # Garante que o elemento da frente esteja em frontStack
        # Exemplo: frontStack = [], backStack = [3, 4]
        #          → frontStack = [4, 3], backStack = []
        if self.frontStack.isEmpty():
            while not self.backStack.isEmpty():
                self.frontStack.push(self.backStack.pop())

        # Retorna o elemento da frente sem remover
        # Exemplo: frontStack.peek() → 3
        if self.frontStack.isEmpty():
            print("Deque vazio (peek_front)")
            return None
        return self.frontStack.peek()

    def peek_back(self):
        # Garante que o elemento de trás esteja em backStack
        # Exemplo: frontStack = [2, 1], backStack = []
        #          → backStack = [1, 2], frontStack = []
        if self.backStack.isEmpty():
            while not self.frontStack.isEmpty():
                self.backStack.push(self.frontStack.pop())

        # Retorna o elemento do final sem remover
        # Exemplo: backStack.peek() → 2
        if self.backStack.isEmpty():
            print("Deque vazio (peek_back)")
            return None
        return self.backStack.peek()

    def isEmpty(self):
        # Deque está vazio se ambas as pilhas estão vazias
        return self.frontStack.isEmpty() and self.backStack.isEmpty()
    
'''
7 - Implemente uma pilha usando filas.
'''
class StackUsingQueues:
    def __init__(self, limit=5):
        self.q1 = Queue(limit)  # Fila principal que armazena os elementos
        self.q2 = Queue(limit)  # Fila auxiliar para operações de push
        self.limit = limit

    def push(self, item):
        # Adiciona o novo elemento na fila vazia (q2)
        # Exemplo: push(1) → q2 = [1], q1 = []
        self.q2.enQueue(item)

        # Move todos os elementos de q1 para q2 (mantém a ordem de pilha)
        # Exemplo: q1 = [2, 1], q2 = [3] 
        #          → q1 = [], q2 = [3, 2, 1] (3 no início - topo da pilha)
        while not self.q1.isEmpty():
            self.q2.enQueue(self.q1.deQueue())

        # Troca as referências: q1 vira a fila com todos os elementos
        # q2 vazia fica pronta para o próximo push
        # Exemplo: q1 = [3, 2, 1], q2 = []
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        # Remove do início de q1 (que é o topo da pilha)
        # Exemplo: q1 = [3, 2, 1] → deQueue() retorna 3
        if self.q1.isEmpty():
            print("Stack Underflow")
            return None
        return self.q1.deQueue()

    def peek(self):
        # Retorna o elemento do início de q1 (topo da pilha) sem remover
        # Exemplo: q1 = [3, 2, 1] → retorna 3
        if self.q1.isEmpty():
            print("Stack vazia")
            return None
        return self.q1.que[self.q1.front] 

    def isEmpty(self):
        # Pilha está vazia se q1 está vazia
        return self.q1.isEmpty()

    def size(self):
        # Tamanho da pilha é o tamanho de q1
        return self.q1.size
    
'''
8 - Inverta os primeiros k elementos de uma fila.
'''
def inverter_k_primeiros(q: Queue, k:int): #1 2 3 4 5, 3
    if not q.isEmpty():
       return None 
    
    s = Stack()

    for i in range(k): 
       s.push(q.deQueue()) #3 2 1, 4 5 
    while not s.isEmpty():
        q.enQueue(s.pop()) #[], 4 5 3 2 1
    for i in range (q.size - k):
        q.enQueue(q.deQueue) # 3 2 1 4 5 

    
    
    