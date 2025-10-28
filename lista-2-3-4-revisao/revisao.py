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

def verificar_balanceamento(expressao):
    """
    Verifica se uma string com (), [], {} está balanceada.
    Retorna (True, -1, "") se balanceada, ou (False, posicao, esperado) se inválida.
    """
    
    # Pilha para guardar os símbolos de abertura que encontramos
    pilha = []
    
    # Dicionário que mapeia cada símbolo de FECHAMENTO para seu correspondente de ABERTURA
    # Exemplo: quando encontramos ')', sabemos que deveria ter um '(' no topo da pilha
    pares = {')': '(', ']': '[', '}': '{'}
    
    # Percorre cada caractere da string, i = posição, char = caractere
    for i, char in enumerate(expressao):
        
        # SE É SÍMBOLO DE ABERTURA: (, [, {
        if char in '([{':
            # Empilha o símbolo de abertura E sua posição (para poder reportar erro depois)
            # Guardamos a posição para saber onde estava o símbolo que ficou sem fechar
            pilha.append((char, i))
        
        # SE É SÍMBOLO DE FECHAMENTO: ), ], }
        elif char in ')]}':
            
            # ERRO 1: Fechamento sem abertura correspondente
            # Se a pilha está vazia, significa que encontramos um fechamento sem abertura antes
            if not pilha:
                return (False, i, f"abertura para '{char}'")
            
            # Tira o último símbolo de abertura da pilha
            # topo = símbolo, pos_topo = posição onde ele estava
            topo, pos_topo = pilha.pop()
            
            # Pega qual símbolo de abertura esperamos para este fechamento
            # Exemplo: para ')', esperamos '('
            esperado = pares[char]
            
            # ERRO 2: Fechamento do tipo errado
            # Se o símbolo no topo não é o que esperávamos
            if topo != esperado:
                return (False, i, f"'{esperado}' em vez de '{char}'")
    
    # ERRO 3: Sobraram aberturas sem fechamento
    # Se depois de processar toda a string ainda tem símbolos na pilha
    if pilha:
        # Pega o primeiro símbolo que ficou sem fechar (e sua posição)
        char, pos = pilha[0]
        
        # Descobre qual fechamento era esperado para esta abertura
        fechamento_esperado = {'(': ')', '[': ']', '{': '}'}[char]
        
        return (False, pos, f"'{fechamento_esperado}' para fechar '{char}'")
    
    # SE CHEGOU ATÉ AQUI: tudo certo! String balanceada
    return (True, -1, "")

# TESTES COM OS EXEMPLOS DO ENUNCIADO
testes = [
    "{[()]}()",        # ✅ Válida - todos os pares abrem/fecham corretamente
    "[({)]}",          # ❌ Inválida - fechamento errado na posição 3
    "((())",           # ❌ Inválida - sobra abertura na posição 0  
    "{[a+b*(c-d)] + 2}" # ✅ Válida - ignora letras e números, só verifica ()[]{}
]

# Testa cada caso
for expressao in testes:
    # Chama a função para verificar
    valido, posicao, esperado = verificar_balanceamento(expressao)
    
    # Mostra o resultado
    if valido:
        print(f"'{expressao}' → ✅ VÁLIDA")
    else:
        print(f"'{expressao}' → ❌ INVÁLIDA")
        print(f"    Erro na posição {posicao}: '{expressao[posicao]}'")
        print(f"    Era esperado: {esperado}")
    print()  # Linha em branco entre os testes