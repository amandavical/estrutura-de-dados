class Stack:
    """
    Classe que implementa uma pilha dinâmica usando array.
    - Suporta crescimento automático (quando cheia)
    - Suporta redução automática (quando metade vazia)
    - Segue a lógica LIFO (Last In, First Out)
    """
    
    def __init__(self, Capacity=1):
        """
        Inicializa a pilha.
        :param Capacity: capacidade inicial do array
        """
        self.top = -1               # índice do topo da pilha (-1 significa vazia)
        self.Capacity = Capacity    # capacidade atual do array
        self.A = [None] * Capacity  # array que guarda os elementos da pilha

    def resize(self, dir):
        """
        Ajusta a capacidade da pilha.
        :param dir: 1 -> dobra a capacidade, 0 -> reduz à metade
        """
        if dir == 1:  # dobra a capacidade
            self.Capacity *= 2
        else:         # reduz a capacidade pela metade
            self.Capacity //= 2
        
        newArray = [None] * self.Capacity
        # copia elementos antigos para o novo array
        for i in range(self.top + 1):
            newArray[i] = self.A[i]
        self.A = newArray

    def push(self, data):
        """
        Adiciona um elemento no topo da pilha.
        Cresce a pilha se estiver cheia.
        """
        if self.Capacity == self.top + 1:  # pilha cheia
            self.resize(1)
        self.top += 1
        self.A[self.top] = data

    def pop(self):
        """
        Remove e retorna o elemento do topo da pilha.
        Reduz a pilha se estiver menos da metade cheia.
        """
        if self.top == -1:
            print("Stack Underflow")
            return
        temp = self.A[self.top]
        self.top -= 1
        if self.top < self.Capacity // 2:  # metade vazia, reduzir
            self.resize(0)
        return temp

    def peek(self):
        """
        Retorna o elemento do topo sem removê-lo.
        """
        if self.top == -1:
            print("Stack Underflow")
            return
        return self.A[self.top]

    def isEmpty(self):
        """
        Retorna True se a pilha estiver vazia.
        """
        return self.top == -1

    def mostrar_pilha(self):
        """
        Retorna uma lista com os elementos da pilha do topo para a base.
        """
        elementos = []
        for i in range(self.top, -1, -1):
            elementos.append(self.A[i])
        return elementos
