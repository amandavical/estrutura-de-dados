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