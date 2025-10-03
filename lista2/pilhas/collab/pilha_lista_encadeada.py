from stack_node import *

'''
Verificação de delimitadores em expressões
Este problema consiste em verificar se os delimitadores de uma expressão matemática (parênteses,
colchetes e chaves) estão corretamente balanceados.
• Exemplo:
(A+B)*(A-B): OK
(A+B]-A: NOK
((A+B)+(C-D): NOK
'''
def verifica_delimitadores(expressao):
    s = Stack()   # cria uma pilha vazia
    for c in expressao:
        # Se for delimitador de abertura, empilha
        if c == '(' or c == '[' or c == '{':
            s.push(c)

        # Se for delimitador de fechamento
        elif c == ')' or c == ']' or c == '}':
            if s.isEmpty():  # pilha vazia = erro
                return False

            # verifica se fecha corretamente
            elif c == ')' and s.peek() == '(':
                s.pop()
            elif c == ']' and s.peek() == '[':
                s.pop()
            elif c == '}' and s.peek() == '{':
                s.pop()
            else:
                return False

    # No final, a pilha precisa estar vazia
    return s.isEmpty()

print(verifica_delimitadores("(A+B)*(A-B)"))
print(verifica_delimitadores("(A+B]-A"))
print(verifica_delimitadores("((A+B)+(C-D)"))

'''
Verificação de tags HTML balanceadas
O problema é verificar se um código HTML possui as tags corretamente abertas e fechadas.
• Exemplo:
<h1>Ola</h1>: OK
<body><h1>Mundo</body>: NOK
</body><p>Oi</p>: NOK
'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # adiciona no topo da pilha

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()  # remove e retorna o topo da pilha
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]  # retorna o topo sem remover
        return None

    def isEmpty(self):
        return len(self.items) == 0  # True se a pilha estiver vazia

def verifica_tags(html):
    """
    Função para verificar se as tags HTML estão balanceadas usando pilha.
    
    Passo a passo explicado:
    - A pilha guarda as tags de abertura enquanto percorremos o HTML.
    - Quando encontramos uma tag de fechamento, conferimos com o topo da pilha.
    - Se bater, desempilhamos. Se não bater, HTML inválido.
    - No final, a pilha deve estar vazia.
    
    Explicações importantes:
    1) j = html.find('>', i) 
       → procura onde termina a tag começando na posição i (caractere '<').
       → retorna -1 se não encontrar '>', ou seja, a tag está aberta mas não fechada.
       
    2) if j == -1:
       → se não há '>', a tag está mal formada → retornamos False
    
    3) i = j
       → depois de processar a tag inteira (de '<' até '>'), avançamos i
         para pular os caracteres da tag e continuar fora dela.
    """
    pilha = Stack()
    i = 0
    while i < len(html):
        if html[i] == '<':
            j = html.find('>', i)  # encontra o '>' que fecha a tag
            if j == -1:  # se não encontrou, tag mal formada
                return False

            tag = html[i+1:j]  # pega o conteúdo da tag sem os sinais <>
            
            if not tag.startswith('/'):  # se for tag de abertura
                pilha.push(tag)          # empilha
                print(f"Empilha: {tag}, Pilha agora: {pilha.items}")
            else:  # se for tag de fechamento
                topo = pilha.pop()       # desempilha topo
                print(f"Tentando fechar: {tag[1:]}, topo da pilha: {topo}")
                if topo != tag[1:]:      # verifica correspondência
                    return False
            i = j  # avançamos i para o final da tag
        i += 1

    return pilha.isEmpty()  # se pilha vazia, HTML está correto


print(verifica_tags("<h1>Ola</h1>"))
print(verifica_tags("<body><h1>Mundo</body>"))
print(verifica_tags("</body><p>Oi</p>"))

'''
Avaliação de Expressões Pós-fixas

Escreva um programa que faça a avaliação de expressões pós-fixas. Uma expressão pós-fixa é avaliada uti-
lizando uma pilha: operandos são empilhados e, ao encontrar um operador, os dois últimos operandos

são desempilhados para aplicar a operação.
Exemplo: Avaliação da expressão 123 ∗ +5−.
'''
def avalia_posfixa(expressao):
    pilha = Stack()
    for c in expressao:
        if c.isdigit():
            pilha.push(int(c))
        else:
            op2 = pilha.pop()
            op1 = pilha.pop()
            if c == '+':
                pilha.push(op1 + op2)
            elif c == '-':
                pilha.push(op1 - op2)
            elif c == '*':
                pilha.push(op1 * op2)
            elif c == '/':
                pilha.push(op1 / op2)
    return pilha.pop()

print(avalia_posfixa("123*+5-"))
            


    
