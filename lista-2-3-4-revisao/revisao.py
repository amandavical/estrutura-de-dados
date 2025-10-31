from stack import Stack
from queue import Queue
'''
1 - . Dada a expressão pós-fixa 8 3 2 * + 5 1 - / 4 +, avalie o resultado usando uma pilha. 
a) Mostre o estado da pilha após cada operação (push de operandos e aplicação de 
operadores). 
b) Informe o resultado final. 

a)
[8] empilha
[8, 3] empilha
[8, 3, 2] empilha
* -> desempilha 2 e 3, calcula 3 x 2 = 6
[8, 6] empilha
+ -> desempilha 8 e 6, calcula 8 + 6 = 14
[14] empilha
[14, 5] empilha
[14, 5, 1] empilha
- -> desempilha 1 e 5, calcula 5 - 1 = 4
[14, 4] empilha
/ -> desempilha 4 e 14, calcula 14 / 4 = 3.5
[3.5] empilha
[3.5, 4] empilha
+ -> desempilha 4 e 3.5, calcula 3.5 + 4 = 7.5
[7.5] empilha 

b) 7.5
'''

'''
2 - Considere uma pilha inicialmente vazia, mostre o estado da pilha e os valores retornados após a execução de cada uma das operações abaixo:
push(5), push(3), pop(), size(), push(2), push(8), pop(), pop(), push(9), push(1), 
push(1), pop(), push(7), peek(), push(6), pop(), pop(), push(4), pop(), pop().

Operação        Pilha           Retorno
-               []              -
push(5)         [5]             -
push(3)         [5, 3]          -
pop()           [5]             3
size()          [5]             1
push(2)         [5, 2]          -
push(8)         [5, 2, 8]       -
pop()           [5, 2]          8
pop()           [5]             2
push(9)         [5, 9]          -
push(1)         [5, 9, 1]       -
push(1)         [5, 9, 1, 1]    -
pop()           [5, 9, 1]       1
push(7)         [5, 9, 1, 7]    -
peek()          [5, 9, 1, 7]    7
push(6)         [5, 9, 1, 7, 6] -
pop()           [5, 9, 1, 7]    6
pop()           [5, 9, 1]       7
push(4)         [5, 9, 1, 4]    -
pop()           [5, 9, 1]       4
pop()           [5, 9]          1

10 push - 8 pop = 2 valores na pilha

'''

'''
3 - Escreva uma função que verifica se uma string com parênteses e colchetes/chasves 
()[]{} está balanceada usando uma pilha. 
a) Se estiver desbalanceada, retorne a primeira posição (índice) onde ocorre o erro 
e qual símbolo era esperado. 
b) Teste com: 
"{[()]}()" (válida) 
"[({)]}" (inválida) 
"((())" (inválida) 
"{[a+b*(c-d)] + 2}" (válida)
'''


def verificaFechamento(f):
    if f == "":
        return True  # ✅ String vazia é balanceada
    
    abert = {'{', '[', '('}
    fech = {'}', ']', ')'}
    pares = {')': '(', ']': '[', '}': '{'}
    s = Stack()
    
    for char in f:
        if char in abert:
            s.push(char)
        elif char in fech:  # ✅ Use 'elif' em vez de outro 'if'
            if s.isEmpty():
                return False
            topo = s.pop()
            if topo != pares[char]:
                return False
        # ✅ Outros caracteres são ignorados (OK)
    
    return s.isEmpty()
    
''''Considere um deque inicialmente vazio, mostre o estado do deque e os valores retornados após a execução de cada uma das operações abaixo:
addFirst(4), addLast(8), addLast(9), addLast(5), rear(), deleteFirst(), deleteLast(), size(), addFirst(10), first(), rear(), addFirst(6)
-, 4
-, 4 8 
-, 4 8 9 
-, 4 8 9 5
5, 4 8 9 5
4, 8 9 5
5, 8 9 
2, 8 9 
-, 10 8 9 
10, 10 8 9 
9, 10 8 9 
-, 6 10 8 9 
'''
'''
Escreva uma função em Python para determinar se uma palavra é palíndromo. 
Você pode usar qualquer combinação de pilha, fila ou deque, mas apenas uma de cada tipo. 
Por exemplo: uma pilha; uma pilha e uma fila; uma pilha e um deque; assim por diante.
'''
def palindromo(p):
    s = Stack()
    for char in p:
        s.push(char)
    for char in p:
        if s.pop() != char:
            return False
    return True
    
'''
Implemente uma pilha usando apenas uma fila.
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
Crie uma função que inverta os últimos k elementos de uma fila de inteiros.
'''
def invert(q, k):
    if q.isEmpty():
        return None
    s = Stack()
    for i in range(k):
        s.push(q.deQueue())
    while not s.isEmpty():
        q.enQueue(s.pop())
    for i in range(q.size - k):
        q.enQueue(q.deQueue())
    return q

'''
Considere uma árvore binária própria na qual todas as folhas estão no último ou no penúltimo nível, responda as questões:
Qual é o número mínimo de folhas, caso a árvore tenha altura h?
Qual é o número máximo de folhas, caso a árvore tenha altura h?
Para árvore própria com folhas nos últimos 2 níveis:

MÍNIMO de folhas = 2^(h-1)

Quando TODAS as folhas estão no PENÚLTIMO nível

MÁXIMO de folhas = 2^h

Quando TODAS as folhas estão no ÚLTIMO nível
'''

'''
Escreva uma função para determinar o número de nós de uma árvore binária.
'''

def verificarNósInterativo(r:BinTree):
    if r is None:
        return False 
    s = Stack()
    s.push(r)
    count = 0
    while not s.isEmpty():
        n = s.pop()
        count += 1
        if n.left:
            s.push(n.left)
        if n.right:
            s.push(n.right)
    return count

def verificarNós(r:BinTree):
    if r is None:
        return 0
    return 1 + verificarNós(r.left) + verificarNós(r.right)

'''
Crie uma função que implemente o percurso em pré-ordem em uma árvore binária usando uma pilha de dados.
'''
def preorder_iterative(root):
    """
    Percurso pré-ordem (raiz-esquerda-direita) usando pilha
    """
    if root is None:
        return []
    
    result = []        # Lista para armazenar a ordem dos nós
    stack = [root]     # Pilha inicia com a raiz
    
    while stack:
        node = stack.pop()         # Remove o nó do topo
        result.append(node.data)   # Visita a RAIZ
        
        # Empilha DIREITA primeiro (será processada depois da ESQUERDA)
        if node.right:
            stack.append(node.right)
        # Empilha ESQUERDA por último (será processada primeiro)
        if node.left:
            stack.append(node.left)
    
    return result