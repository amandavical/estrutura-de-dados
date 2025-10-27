'''
LISTA - ÁRVORES BINÁRIAS
RESPOSTAS TEÓRICAS E ALGORITMOS
'''

# =============================================================================
# CONCEITOS FUNDAMENTAIS
# =============================================================================

'''
1. ÁRVORE BINÁRIA PRÓPRIA (Strict Binary Tree)
   - Todo nó tem 0 ou 2 filhos (NUNCA 1 filho)
   - Nós internos: SEMPRE têm subárvore esquerda E direita
   - Folhas: não têm nenhum filho

   Exemplo:
        A
       / \
      B   C    ← B e C têm 2 filhos cada
     / \   \
    D   E   F   ← D, E, F são folhas (0 filhos)
'''

'''
2. ÁRVORE BINÁRIA CHEIA (Full Binary Tree)
   - "Perfeita" ou "Lotada"
   - Todos os níveis COMPLETAMENTE preenchidos
   - Não tem espaços vazios em nenhum nível
   - Forma de triângulo perfeito
   - Altura = h → SEMPRE tem 2ʰ - 1 nós

   Exemplo (altura 2):
        A
       / \
      B   C

   Exemplo (altura 3):
          A
         / \
        B   C
       / \ / \
      D  E F  G
'''

'''
3. ÁRVORE BINÁRIA COMPLETA (Complete Binary Tree)
   - "Compacta" ou "Aproveitada"
   - Último nível pode estar incompleto
   - Mas os nós estão TODOS À ESQUERDA (sem "buracos" no meio)

   Exemplos VÁLIDOS:
        A          A
       / \        / \
      B   C      B   C
     /          / \
    D          D   E

   Exemplo INVÁLIDO:
        A
       / \
      B   C
       \ 
        E    ❌ (E à direita, deixou buraco)
'''

'''
4. ALTURA MÁXIMA com n nós
   - Ocorre quando a árvore é uma "lista encadeada"
   - Altura máxima = n - 1

   Exemplo (5 nós → altura 4):
        A
         \
          B
           \
            C
             \
              D
               \
                E
'''

'''
5. ALTURA MÍNIMA com n nós
   - Ocorre quando a árvore é CHEIA
   - Altura mínima = ⌊log₂(n)⌋

   Exemplo (7 nós → altura 2):
        A
       / \
      B   C
     / \ / \
    D  E F  G
'''

'''
6. ÁRVORE BINÁRIA IMPRÓPRIA
   - Qualquer árvore que não segue as regras acima
   - Pode ter nós com 1 filho, buracos, etc.

   Estatísticas:
   - Máximo nós internos: n-1
   - Mínimo nós internos: 0
   - Máximo folhas: n
   - Mínimo folhas: 1
'''

'''
7. MÍNIMO de FOLHAS (altura h)
   - 1 folha (árvore degenerada em lista)
'''

'''
8. MÁXIMO de FOLHAS (altura h)
   - 2ʰ folhas (árvore CHEIA)
'''

'''
9. ÁRVORE BINÁRIA BALANCEADA
   - Para cada nó: |altura(esquerda) - altura(direita)| ≤ 1
   - As subárvores têm alturas parecidas

   Exemplo:
        A
       / \
      B   C
     /   / \
    D   E   F
'''

'''
10. ÁRVORE PERFEITAMENTE BALANCEADA
    - Número de nós nas subárvores difere no máximo em 1
    - Mais balanceada que a balanceada comum

    Exemplo:
        A
       / \
      B   C
     /   / 
    D   E
'''

# =============================================================================
# DICA PARA DECORAR
# =============================================================================
'''
CHEIA = CHEva → CHEga até embaixo (todos níveis cheios)
COMPLETA = COMPacta → COM todos os nós juntinhos à esquerda
PRÓPRIA = Precisa ter Pares (0 ou 2 filhos)

Toda árvore CHEIA é COMPLETA e PRÓPRIA
Toda árvore COMPLETA é PRÓPRIA (mas nem sempre CHEIA)
'''

# =============================================================================
# ALGORITMOS RECURSIVOS E NÃO-RECURSIVOS
# =============================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# a) Número de nós
def count_nodes_recursivo(node):
    """Versão recursiva para contar número de nós"""
    if not node:
        return 0
    return 1 + count_nodes_recursivo(node.left) + count_nodes_recursivo(node.right)

def count_nodes_iterativo(root):
    """Versão iterativa para contar número de nós"""
    if not root:
        return 0
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        count += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count

# b) Soma do conteúdo de todos os nós
def sum_nodes_recursivo(node):
    """Versão recursiva para somar todos os nós"""
    if not node:
        return 0
    return node.data + sum_nodes_recursivo(node.left) + sum_nodes_recursivo(node.right)

def sum_nodes_iterativo(root):
    """Versão iterativa para somar todos os nós"""
    if not root:
        return 0
    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        total += node.data
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return total

# c) Nível com maior soma
def nivel_maior_soma(root):
    """Encontra o nível com maior soma"""
    if not root:
        return 0
    
    from collections import deque
    queue = deque([root])
    max_soma = root.data
    nivel_max = 0
    nivel_atual = 0
    
    while queue:
        nivel_atual += 1
        tamanho_nivel = len(queue)
        soma_nivel = 0
        
        for _ in range(tamanho_nivel):
            node = queue.popleft()
            soma_nivel += node.data
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if soma_nivel > max_soma:
            max_soma = soma_nivel
            nivel_max = nivel_atual
    
    return nivel_max

# d) Altura da árvore
def altura_recursivo(node):
    """Versão recursiva para calcular altura"""
    if not node:
        return -1
    return 1 + max(altura_recursivo(node.left), altura_recursivo(node.right))

def altura_iterativo(root):
    """Versão iterativa para calcular altura"""
    if not root:
        return -1
    
    from collections import deque
    queue = deque([(root, 0)])
    altura_max = 0
    
    while queue:
        node, nivel = queue.popleft()
        altura_max = max(altura_max, nivel)
        
        if node.left:
            queue.append((node.left, nivel + 1))
        if node.right:
            queue.append((node.right, nivel + 1))
    
    return altura_max

# e) Profundidade de um nó
def profundidade(root, alvo):
    """Calcula a profundidade de um nó específico"""
    if not root:
        return -1
    
    from collections import deque
    queue = deque([(root, 0)])
    
    while queue:
        node, profundidade = queue.popleft()
        
        if node == alvo:
            return profundidade
        
        if node.left:
            queue.append((node.left, profundidade + 1))
        if node.right:
            queue.append((node.right, profundidade + 1))
    
    return -1  # Nó não encontrado

# =============================================================================
# ALGORITMOS DE VERIFICAÇÃO
# =============================================================================

# a) Verificar se é própria
def is_propria(node):
    """Verifica se a árvore é própria (0 ou 2 filhos)"""
    if not node:
        return True
    
    # Se é folha → OK
    if not node.left and not node.right:
        return True
    
    # Se é nó interno → deve ter AMBAS as subárvores
    if node.left and node.right:
        return is_propria(node.left) and is_propria(node.right)
    
    # Tem só esquerda OU só direita → NÃO é própria
    return False

# b) Verificar se é cheia
def is_cheia(node):
    """Verifica se a árvore é cheia (todos níveis completos)"""
    if not node:
        return True
    
    # Se é folha → OK
    if not node.left and not node.right:
        return True
    
    # Se tem ambos os filhos, verifica recursivamente
    if node.left and node.right:
        return is_cheia(node.left) and is_cheia(node.right)
    
    # Se tem apenas um filho → NÃO é cheia
    return False

# c) Verificar se é completa
def is_completa(root):
    """Verifica se a árvore é completa (último nível à esquerda)"""
    if not root:
        return True
    
    from collections import deque
    queue = deque([root])
    encontrou_vazio = False
    
    while queue:
        node = queue.popleft()
        
        if node:
            if encontrou_vazio:
                return False  # Encontrou nó depois de vazio
            queue.append(node.left)
            queue.append(node.right)
        else:
            encontrou_vazio = True
    
    return True

'''
13. EXPRESSÃO PREFIXADA: + / 4 - 3 1 - * 8 / 6 2 7
REGRA: OPERADOR antes dos OPERANDOS
- Leitura: DA ESQUERDA para DIREITA
-  Operador → cria nó e busca 2 filhos recursivamente

ÁRVORE BINÁRIA CORRESPONDENTE:

        +
       / \
      /   \
     /     \
    /       \
   /         -
  /         / \
 /         *   7
/         / \
/         8   /
/           / \
/           6   2
/
/ \
4   -
   / \
  3   1

PASSO A PASSO DA CONSTRUÇÃO:
+ → operador raiz
├── / → filho esquerdo de +
│   ├── 4 → filho esquerdo de /
│   └── - → filho direito de /
│       ├── 3 → filho esquerdo de -
│       └── 1 → filho direito de -
└── - → filho direito de +
    ├── * → filho esquerdo de -
    │   ├── 8 → filho esquerdo de *
    │   └── / → filho direito de *
    │       ├── 6 → filho esquerdo de /
    │       └── 2 → filho direito de /
    └── 7 → filho direito de -

EXPRESSÃO COMPLETA: (4 / (3 - 1)) + ((8 * (6 / 2)) - 7)
'''

'''
14. EXPRESSÃO POSFIXADA: 5 7 / 3 * 1 - 8 2 4 6 + / * +
REGRA: OPERANDOS antes do OPERADOR  
- Leitura: DA ESQUERDA para DIREITA
- Usamos PILHA: empilha operandos, quando acha operador, desempilha 2 e faz operação

ÁRVORE BINÁRIA CORRESPONDENTE:

          +
         / \
        /   \
       /     \
      /       \
     /         *
    /         / \
   /         /   \
  /         /     \
 /         /       \
-         8        /
/ \              / \
/   \            /   \
*     1         2     +
      / \              / \
     /   3            4   6
    / \
   5   7

PASSO A PASSO DA CONSTRUÇÃO (USANDO PILHA):
5 → empilha
7 → empilha
/ → desempilha 7 e 5, cria /(5,7), empilha
3 → empilha
* → desempilha 3 e /, cria *(/,3), empilha  
1 → empilha
- → desempilha 1 e *, cria -(*,1), empilha
8 → empilha
2 → empilha
4 → empilha
6 → empilha
+ → desempilha 6 e 4, cria +(4,6), empilha
/ → desempilha + e 2, cria /(2,+), empilha
* → desempilha / e 8, cria *(8,/), empilha
+ → desempilha * e -, cria +(-,*), empilha

EXPRESSÃO COMPLETA: (((5 / 7) * 3) - 1) + (8 * (2 / (4 + 6)))
'''

'''
15. EXPRESSÃO INFIXADA: (8 - ((2+7)/4)) + (((5 / 6)*3)-1)
REGRA: OPERADOR entre os OPERANDOS
- Mais difícil de construir diretamente
- Precisamos respeitar a PRECEDÊNCIA e PARÊNTESES

ÁRVORE BINÁRIA CORRESPONDENTE:

          +
         / \
        /   \
       /     \
      /       \
     -         -
    / \       / \
   /   \     /   \
  8     /   *     1
       / \   / \
      +   4 /   3
     / \   / \
    2   7 5   6

PASSO A PASSO DA CONSTRUÇÃO:
+ → operador principal (raiz)
├── - → lado esquerdo: (8 - ((2+7)/4))
│   ├── 8 → primeiro operando
│   └── / → divisão: ((2+7)/4)
│       ├── + → adição: (2+7)
│       │   ├── 2
│       │   └── 7
│       └── 4
└── - → lado direito: (((5/6)*3)-1)
    ├── * → multiplicação: ((5/6)*3)
    │   ├── / → divisão: (5/6)
    │   │   ├── 5
    │   │   └── 6
    │   └── 3
    └── 1

EXPRESSÃO COMPLETA: (8 - ((2+7)/4)) + (((5/6)*3)-1)
'''

'''
16. ANÁLISE DE RELAÇÕES EM ÁRVORES BINÁRIAS

DEFINIÇÕES:
- G: Árvore binária genérica não vazia
- P: Árvore binária própria não vazia (todo nó tem 0 ou 2 filhos)
- e₉, eₚ: Número de nós externos (folhas)
- i₉, iₚ: Número de nós internos  
- n₉, nₚ: Número total de nós
- h₉, hₚ: Altura da árvore

VERDADEIRO OU FALSO:

i. 2hₚ + 1 ≤ nₚ → ✅ VERDADEIRO
   Justificativa: Em árvore própria, o mínimo de nós ocorre na árvore degenerada
   onde cada nó interno tem um filho interno e um folha. Nesse caso: nₚ = 2hₚ + 1

ii. hₚ + 1 ≤ eₚ → ✅ VERDADEIRO
   Justificativa: Em árvore própria, o mínimo de folhas é hₚ + 1 (árvore degenerada)

iii. n₉ = 2e₉ - 1 → ❌ FALSO
   Justificativa: Esta relação só vale para árvores próprias. Para árvore genérica:
   Exemplo: árvore com raiz e um filho → n₉ = 2, e₉ = 1 → 2 ≠ 2×1 - 1 = 1

iv. 1 ≤ e₉ ≤ 2ʰ₉ → ✅ VERDADEIRO
   Justificativa: 
   - Mínimo: 1 folha (árvore degenerada em lista)
   - Máximo: 2ʰ₉ folhas (árvore cheia)

v. h₉ ≤ i₉ ≤ 2ʰ₉ - 1 → ✅ VERDADEIRO
   Justificativa:
   - Mínimo: h₉ nós internos (árvore degenerada)
   - Máximo: 2ʰ₉ - 1 nós internos (árvore cheia sem folhas do último nível)

RESUMO:
| Item | Proposição | Resultado | Explicação |
|------|------------|-----------|------------|
| i | 2hₚ + 1 ≤ nₚ | ✅ Verdadeiro | Mínimo em árvore própria degenerada |
| ii | hₚ + 1 ≤ eₚ | ✅ Verdadeiro | Mínimo de folhas em árvore própria |
| iii | n₉ = 2e₉ - 1 | ❌ Falso | Só vale para árvores próprias |
| iv | 1 ≤ e₉ ≤ 2ʰ₉ | ✅ Verdadeiro | Limites de folhas |
| v | h₉ ≤ i₉ ≤ 2ʰ₉ - 1 | ✅ Verdadeiro | Limites de nós internos |
'''

# =============================================================================
# EXEMPLOS DE USO
# =============================================================================
if __name__ == "__main__":
    # Exemplo de criação de árvore
    raiz = Node(1)
    raiz.left = Node(2)
    raiz.right = Node(3)
    raiz.left.left = Node(4)
    raiz.left.right = Node(5)
    
    print("Número de nós:", count_nodes_recursivo(raiz))
    print("Altura:", altura_recursivo(raiz))
    print("É própria?", is_propria(raiz))
    print("É cheia?", is_cheia(raiz))
    print("É completa?", is_completa(raiz))