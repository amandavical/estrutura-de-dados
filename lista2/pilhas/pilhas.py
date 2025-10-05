from stack import Stack
'''
Implemente uma função que transfira os dados de uma pilha S para uma pilha T, de tal forma que o topo da pilha S seja o primeiro elemento da pilha T, e o último elemento de S seja o topo da pilha T.
'''
def mostrar_pilha(S):
    """Retorna uma lista com os elementos da pilha do topo para baixo."""
    elementos = []
    for i in range(S.top, -1, -1):  # do topo até a base
        elementos.append(S.A[i])
    return elementos

def transferir(S, T):
    while not S.isEmpty():
        T.push(S.pop())
        print(f"Pilha T agora: {mostrar_pilha(T)}") 
        
    return T

S = Stack()
S.push(1)
S.push(2)
S.push(3)  # topo = 3
print(f"Pilha S: {mostrar_pilha(S)}")

T = Stack()

T = transferir(S, T)

'''
Elabore uma função recursiva que remova todos os elementos de uma pilha.
'''
def remover_pilha(S):
    if not S.isEmpty():
        S.pop()
        remover_pilha(S)
        return

'''
Implemente uma função que inverta a ordem dos elementos de um vetor usando uma pilha.
'''
def inverter_vetor(vetor):
    s = Stack()
    for i in range(len(vetor)):
        s.push(vetor[i])
        print(f"vetor[{i}] = {vetor[i]} empilhado -> Pilha agora: {s.mostrar_pilha()}")
    for i in range(len(vetor)): 
        vetor[i] = s.pop()
        print(f"vetor[{i}] recebe {vetor[i]} -> Vetor agora: {vetor}")
    
    print("\nVetor invertido:", vetor)
    
vet = [1, 2, 3]
inverter_vetor(vet)

'''
Seja P uma pilha de inteiros não negativos ocupando um array A com N posições, de modo que:
Números empilhados em P ocupam posições crescentes de A a partir de A[1]
A[0] contém o índice em A do número empilhado por último (topo da pilha)
A pilha pode crescer enquanto houver posições em A.
Implemente as funções de acesso às pilhas: push, pop, peek, len, isEmpty, isFull, empty( esvazia a pilha).

A pilha é representada por um array A de tamanho N.

Os elementos começam em A[1], A[0] guarda o índice do topo (quantos elementos há).

Então:

Quando a pilha está vazia, A[0] == 0.

O topo está em A[A[0]].

O tamanho máximo é N - 1 (já que A[0] é usado para o índice).
'''

def create_stack(N):
    """Cria uma pilha vazia com capacidade N-1"""
    A = [0] * N  # A[0] guarda o índice do topo
    return A

def push(A, x):
    """Empilha o elemento x"""
    if isFull(A):
        print("Erro: pilha cheia!")
        return
    A[0] += 1
    A[A[0]] = x

def pop(A):
    """Desempilha e retorna o elemento do topo"""
    if isEmpty(A):
        print("Erro: pilha vazia!")
        return None
    x = A[A[0]]
    A[0] -= 1
    return x

def peek(A):
    """Retorna o elemento do topo sem remover"""
    if isEmpty(A):
        print("Erro: pilha vazia!")
        return None
    return A[A[0]]

def isEmpty(A):
    """Verifica se a pilha está vazia"""
    return A[0] == 0

def isFull(A):
    """Verifica se a pilha está cheia"""
    return A[0] == len(A) - 1

def empty(A):
    """Esvazia a pilha"""
    A[0] = 0

def length(A):
    """Retorna o número de elementos da pilha"""
    return A[0]

# Criar pilha com 6 posições (5 para dados)
P = create_stack(6)

push(P, 10)
push(P, 20)
push(P, 30)

print("Topo:", peek(P))        # 30
print("Tamanho:", length(P))   # 3
print("Desempilhado:", pop(P)) # 30
print("Agora o topo:", peek(P))# 20
empty(P)
print("Está vazia?", isEmpty(P)) # True

'''
Considere duas pilhas de inteiros não negativos P1 e P2 ocupando um único array A com N posições, de modo que:
Números empilhados em P1 ocupam posições crescentes a partir de A[0]
Números empilhados em P2 ocupam posições decrescentes de A partir de A[N-1]
t1 contém o índice em A do número empilhado por último em P1
t2 contém o índice em A do número empilhado por último em P2
As pilhas podem crescer enquanto houver posições livres
Implemente as funções de acesso às pilhas: push, pop, peek, len, isEmpty, isFull, empty

Temos um único vetor A com N posições.

Pilha P1 começa no início do vetor:

Cresce em direção aos índices maiores (0 → 1 → 2 → ...)

Seu topo é t1

Quando está vazia: t1 = -1 (vai somando)

Pilha P2 começa no final do vetor:

Cresce em direção aos índices menores (N-1 → N-2 → N-3 → ...)

Seu topo é t2

Quando está vazia: t2 = N (vai subtraindo)

As pilhas podem crescer enquanto t1 < t2 - 1.
'''

def create_double_stack(N):
    """Cria duas pilhas (P1 e P2) em um mesmo array"""
    A = [0] * N
    t1 = -1       # topo da pilha 1
    t2 = N        # topo da pilha 2
    return A, t1, t2


# ---- Funções de P1 ----

def push1(A, x, t1, t2):
    """Empilha em P1"""
    if isFull(t1, t2):
        print("Erro: pilhas cheias!")
        return t1, t2
    t1 += 1
    A[t1] = x
    return t1, t2

def pop1(A, t1, t2):
    """Desempilha de P1"""
    if isEmpty1(t1):
        print("Erro: P1 vazia!")
        return None, t1, t2
    x = A[t1]
    t1 -= 1
    return x, t1, t2

def peek1(A, t1):
    """Olha o topo de P1"""
    if isEmpty1(t1):
        print("Erro: P1 vazia!")
        return None
    return A[t1]

def isEmpty1(t1):
    return t1 == -1

def length1(t1):
    return t1 + 1


# ---- Funções de P2 ----

def push2(A, x, t1, t2):
    """Empilha em P2"""
    if isFull(t1, t2):
        print("Erro: pilhas cheias!")
        return t1, t2
    t2 -= 1
    A[t2] = x
    return t1, t2

def pop2(A, t1, t2):
    """Desempilha de P2"""
    if isEmpty2(t2, len(A)):
        print("Erro: P2 vazia!")
        return None, t1, t2
    x = A[t2]
    t2 += 1
    return x, t1, t2

def peek2(A, t2):
    """Olha o topo de P2"""
    if isEmpty2(t2, len(A)):
        print("Erro: P2 vazia!")
        return None
    return A[t2]

def isEmpty2(t2, N):
    return t2 == N

def length2(t2, N):
    return N - t2


# ---- Funções gerais ----

def isFull(t1, t2):
    """Verifica se não há espaço entre as pilhas"""
    return t1 + 1 == t2

def empty1():
    """Topo inicial de P1"""
    return -1

def empty2(N):
    """Topo inicial de P2"""
    return N

'''
Imagine um processador que possui um único registrador e seis instruções.
	LD A coloca o operando A no registrador
	ST A coloca o conteúdo do registrador na variável A
	AD A soma o conteúdo da variável A ao registrador
	SB A subtrai o conteúdo do registrador pela variável A
	ML A multiplica o conteúdo do registrador pela variável A
	DV A divide o conteúdo do registrador pela variável A

Escreva um programa que aceite uma expressão posfixa contendo operando de uma única letra e os operadores +,-,*, e/, imprima uma sequência de instruções para avaliar a expressão e deixe o resultado no registrador. Use variáveis da forma TEMPn como variáveis temporárias. Por exemplo, usar a expressão posfixa ABC*+DE-/ deverá imprimir o seguinte:

LD B
ML C
ST TEMP1
LD A
AD TEMP1
ST TEMP2
LD D
SB E
ST TEMP3
LD TEMP2
DV TEMP3
ST TEMP4
'''

def gerar_codigo_posfixa(expr):
    pilha = []
    temp_count = 1
    instrucoes = []

    for c in expr:
        if c.isalpha():  # se for letra (operando)
            pilha.append(c)
        else:  # operador
            op2 = pilha.pop()
            op1 = pilha.pop()

            temp = f"TEMP{temp_count}"
            temp_count += 1

            if c == '+':
                instrucoes += [f"LD {op1}", f"AD {op2}", f"ST {temp}"]
            elif c == '-':
                instrucoes += [f"LD {op1}", f"SB {op2}", f"ST {temp}"]
            elif c == '*':
                instrucoes += [f"LD {op1}", f"ML {op2}", f"ST {temp}"]
            elif c == '/':
                instrucoes += [f"LD {op1}", f"DV {op2}", f"ST {temp}"]

            pilha.append(temp)

    return instrucoes


# Exemplo de uso
expr = "ABC*+DE-/"
codigo = gerar_codigo_posfixa(expr)
print("\n".join(codigo))




        

        

    