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


        

        

    