class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearch:
    def __init__(self):
        self.root = None

    def insert(self, value):

        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if not node.right:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
  

    def search(self, value):
        if not self.root:
            return False
        else:
            return self._search(self.root, value)
    
    def _search(self, node, value):
        if not node:
            return False
        elif node.value == value:
            return True
        else:
            if value < node.value:
                return self._search(node.left, value)
            elif value > node.value:
                return self._search(node.right, value)


    def height(self):
        if not self.root:
            return 0
        else:
            return self._height(self.root)
    
    def _height(self, node):
        if not node: return 0
        else: return max(self._height(node.left), self._height(node.right)) + 1

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if not node:
            return None
        
        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            # Caso 1: Nó sem filhos
            if not node.left and not node.right:
                return None
            # Caso 2: Um filho
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Caso 3: Dois filhos
            else:
                # Encontrar o menor valor da subárvore direita
                successor = self._min_value_node(node.right)
                node.value = successor.value
                # Remover o sucessor
                node.right = self._remove(node.right, successor.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Função auxiliar para visualizar a árvore (percurso em ordem)
    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print() # Para pular uma linha no final

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.value, end=' ')
            self._inorder_traversal(node.right)



if __name__ == '__main__':

    tree = BinarySearch()

    tree.insert(15)
    tree.insert(5)
    tree.insert(21)
    tree.insert(4)
    tree.insert(12)
    tree.insert(11)
    tree.insert(10)
    tree.insert(9)
    tree.insert(16)
    
    print("Árvore original (em ordem):")
    tree.inorder_traversal() # Saída: 4 5 9 10 11 12 15 16 21 

    # --- Testando a remoção ---

    # 1. Removendo um nó folha (9)
    print("\nRemovendo 9 (nó folha)...")
    tree.remove(9)
    print("Árvore após remover 9:")
    tree.inorder_traversal() # Saída: 4 5 10 11 12 15 16 21 

    # 2. Removendo um nó com um filho (11)
    print("\nRemovendo 11 (nó com um filho)...")
    tree.remove(11)
    print("Árvore após remover 11:")
    tree.inorder_traversal() # Saída: 4 5 10 12 15 16 21

    # 3. Removendo um nó com dois filhos (15 - a raiz)
    print("\nRemovendo 15 (nó com dois filhos)...")
    tree.remove(15)
    print("Árvore após remover 15:")
    tree.inorder_traversal() # Saída: 4 5 10 12 16 21 
    
    print(f"\nNova raiz da árvore: {tree.root.value}") # A nova raiz deve ser 16
    print(f'Altura da árvore final: {tree.height()}')

