'''
Projete um algoritmo recursivo para determinar o maior elemento 
em uma sequência de inteiros S com n elementos. 
Qual é a complexidade do seu algoritmo? 
'''
def encontrar_maior_elemento(lista, n):
    if n == 1:
        return lista[0]
    
    maior_do_resto = encontrar_maior_elemento(lista, n-1)
    elemento_atual = lista[n-1]

    if elemento_atual > maior_do_resto:
        return elemento_atual
    else:
        return maior_do_resto
    

print(encontrar_maior_elemento([3, 7, 2], 3))

'''
Escreva um algoritmo recursivo que organize uma sequência de inteiros
 de tal forma que os valores pares apareçam antes do que os ímpares.
'''

def pares_primeiro(lista, n):
    if n == 1:
        return [lista[0]]
    elemento_atual = lista[n-1]
    pares = pares_primeiro(lista, n-1)
    
    if elemento_atual % 2 == 0:
        return [elemento_atual] + pares
    else:
        return pares + [elemento_atual]
    

print(pares_primeiro([3, 7, 2], 3))

'''
Escreva as funções recursivas listas a seguir, todas recebem um inteiro e devolvem um inteiro.
a - maiorDigito
retorna o maior dígito de um inteiro
b - menorDigito
retorna o menor dígito de um inteiro
c - contaDigito
retorna a quantidade de dígitos de um inteiro
d - somaDigito
retorna a soma dos dígitos de um inteiro
e - zeraPares
retorna um inteiro com os dígitos pares em zero
f - zeraImpares
retorna um inteiro com os dígitos ímpares em zero
g - removePares
remove os dígitos pares de um inteiro
h - removeImpares
remove os dígitos ímpares de um inteiro
i - inverteNumero
inverte os dígitos de um número inteiro
'''

def maiorDigito(n):
    if n < 10:
        return n
    maior_resto = maiorDigito(n // 10) #numero sem o ultimo digito
    ultimo_digito = n % 10 #ultimo digito
    if ultimo_digito > maior_resto:
        return ultimo_digito
    else:
        return maior_resto
    
print(maiorDigito(1234))

def menorDigito(n):
    if n < 10:
        return n
    print(n // 10)
    menor_resto = menorDigito(n // 10)
    ultimo_digito = n % 10
   
    if ultimo_digito < menor_resto:
        return ultimo_digito
    else:
        return menor_resto
    
print(menorDigito(1234))
    
def contaDigito(n):
    if n < 10:
        return 1
    return 1 + contaDigito(n // 10)

print(contaDigito(5678))

def somaDigito(n):
    if n<10:
        return n 
    return n % 10 + somaDigito(n // 10)

print(somaDigito(123))

def zeraPares(n):
    if n < 10:
        return n
    menor_resto = zeraPares(n // 10) #numero sem o ultimo digito
    ultimo_digito = n % 10 #ultimo digito
    if ultimo_digito % 2 == 0:
        return menor_resto * 10 # Se par, zera (multiplica por 10)
    else:
        return menor_resto * 10 + ultimo_digito # Se ímpar, mantém

print(zeraPares(1234))

def zeraImpares(n):
    if n < 10:
        return n
    menor_resto = zeraImpares(n // 10) #numero sem o ultimo digito
    ultimo_digito = n % 10 #ultimo digito
    if ultimo_digito % 2 == 1:
        return menor_resto * 10 # Se ímpar, zera (multiplica por 10)
    else:
        return menor_resto * 10 + ultimo_digito # Se par, mantém

print(zeraImpares(1234))


'''
removePares
remove os dígitos pares de um inteiro
'''
def removePares(n):
    if n < 10:
        if n % 2 == 0:
            return 0
        return n
    menor_resto = removePares(n // 10)
    ultimo_digito = n % 10

    if ultimo_digito % 2 ==0:
       return menor_resto  # Ignora este dígito
    else:
      return menor_resto * 10 + ultimo_digito # Adiciona ao número reconstruído
    
print(removePares(2222))

def removeImpares(n):
    if n < 10:
        if n % 2 == 1:
            return 0
        return n
    menor_resto = removeImpares(n // 10)
    ultimo_digito = n % 10

    if ultimo_digito % 2 == 1:
       return menor_resto  # Ignora este dígito
    else:
      return menor_resto * 10 + ultimo_digito # Adiciona ao número reconstruído
    
print(removeImpares(2222))



def inverterNumero(n, n_invertido = 0):
     if n == 0:
         return n_invertido

     ultimo_digito = n % 10
     novo_invertido = n_invertido * 10 + ultimo_digito

     return inverterNumero(n // 10, novo_invertido)

print(inverterNumero(1234))

'''bonus: SomaImpares'''
def somaImpares(n):  
  if n < 10:
    if n % 2 == 1:
      return n
    else:
      return 0
  menor_resto = somaImpares(n//10)
  ultimo_digito = n % 10
  if ultimo_digito % 2 == 1:
    return ultimo_digito + menor_resto
  else:
    return menor_resto
  
print(somaImpares(2234))

'''Crie uma função recursiva para verificar 
se uma string tem mais vogais do que consoantes.'''

def maisVogais(lista, n):
    if n == 0:
        return 0
    
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    menor_resto = maisVogais(lista, n-1)
    lista_atual = lista[n-1].lower()

    if lista_atual in vogais:
        total = 1 + menor_resto
    else:
        total = menor_resto
    
    if n == len(lista):
     if total > len(lista) - total:
        return "Mais vogais"
     else:
        return "Não tem mais vogais"
     
    return total
     

print(maisVogais('amandaa', 7))

'''
Implemente o algoritmo de busca binária em um vetor de inteiros ordenado.
'''

def busca_binaria(lista, elemento, inicio, fim):
    if inicio > fim:
        return False
    meio = (inicio + fim) // 2
    
    if lista[meio] == elemento:
        return meio
    elif elemento < lista[meio]:
        return busca_binaria(lista, elemento, inicio, meio - 1)
    else:
        return busca_binaria(lista, elemento, meio + 1, fim)
    
print(busca_binaria([1, 2, 3, 4, 5], 3, 0, 4))

'''
 Dados um vetor de inteiros distintos e ordenados de maneira crescente e um inteiro target, 
 crie um algoritmo recursivo que determine se existem dois inteiros no vetor que a soma seja igual a target.
'''

def existeSoma(lista,inicio, fim, target):
    if inicio >= fim: # Caso base: ponteiros se cruzaram
        return False
    
    soma = lista[inicio] + lista[fim]

    if soma == target:
        return True
    elif soma < target:
        return existeSoma(lista, inicio + 1, fim, target)  # Move inicio para direita
    else:
        return existeSoma(lista, inicio, fim - 1, target)  # Move fim para esquerda
    
print(existeSoma([1, 2, 3, 4, 5], 0, 4, 7))
    
'''
Dado um array S não ordenado de inteiros e um inteiro k, crie um algoritmo recursivo para 
reorganizar os elementos de S tal que todos os elementos menores ou iguais a K 
apareçam antes do que os elementos maiores.
'''
def reorganizar(lista, k):
    if len(lista) == 0:
        return []
    elif lista[0] <= k:
        # Coloca o elemento no INÍCIO e processa o resto da lista
        return [lista[0]] + reorganizar(lista[1:], k) 
    else:
        # Coloca o elemento no FINAL e processa o resto da lista
        return reorganizar(lista[1:], k) + [lista[0]] 
    
print(reorganizar([3, 1, 4, 2, 5], 3))
  





   