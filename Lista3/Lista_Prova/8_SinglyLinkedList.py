class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        atual = self.head
        while atual.next:
            atual = atual.next
        atual.next = new_node
    
    def delete_by_value(self, value):
        if not self.head: return

        if self.head.value == value:
            self.head = self.head.next
            return
        
        atual = self.head
        while atual.next and atual.next.value != value:
            atual = atual.next
        if atual.next:
            atual.next = atual.next.next


    def search(self, value):
        atual = self.head
        while atual:
            if atual.value == value: return True
            atual = atual.next
        return False
    
    def display(self):
        atual = self.head
        elementos = list()
        while atual:
            elementos.append(str(atual.value))
            atual = atual.next
        print(" -> ".join(elementos) if elementos else "Empty list")

    def reverse(self):
        ant = None
        atual = self.head
        while atual:
            prox_node = atual.next
            atual.next = ant
            ant = atual
            atual = prox_node
        self.head = ant

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    

def merge_sorted(l1, l2):
    aux = Node(None)
    tail = aux

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Liga o restante da lista que ainda não terminou
    tail.next = l1 or l2

    
    elementos = list()
    while aux:
        elementos.append(str(aux.value))
        aux = aux.next
    print(" -> ".join(elementos) if elementos else "Empty list")


ll = SinglyLinkedList()

# 1. Inserções no início
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.display()  # Esperado: 20 -> 10

# 2. Inserções no fim
ll.insert_at_tail(30)
ll.insert_at_tail(40)
ll.display()  # Esperado: 20 -> 10 -> 30 -> 40

# 3. Buscar valores
print(ll.search(10))  # Esperado: True
print(ll.search(50))  # Esperado: False

# 4. Remoção de valor
ll.delete_by_value(10)
ll.display()  # Esperado: 20 -> 30 -> 40

# 5. Remoção de valor inexistente e da cabeça
ll.delete_by_value(100)  # Nada acontece
ll.delete_by_value(20)
ll.display()  # Esperado: 30 -> 40


ll = SinglyLinkedList()
ll.insert_at_tail(1)
ll.insert_at_tail(2)
ll.insert_at_tail(3)
ll.insert_at_tail(4)
ll.display()      # Saída esperada: 1 -> 2 -> 3 -> 4

ll.reverse()
ll.display()      # Saída esperada: 4 -> 3 -> 2 -> 1



ll = SinglyLinkedList()
ll.insert_at_tail(1)
ll.insert_at_tail(2)
ll.insert_at_tail(3)
ll.insert_at_tail(4)



# Criando ciclo: último nó aponta para o segundo nó
ll.head.next.next.next.next = ll.head.next

print(ll.has_cycle())  # Saída: True


ll = SinglyLinkedList()
ll.insert_at_tail(1)
ll.insert_at_tail(2)
ll.insert_at_tail(3)
ll.insert_at_tail(4)

# Encontrar o meio
middle = ll.find_middle()
print("Middle:", middle.value)


# Criando outra lista
ll2 = SinglyLinkedList()
ll2.insert_at_tail(2)
ll2.insert_at_tail(4)
ll2.insert_at_tail(6)

# Mesclar listas
merge_sorted(ll.head, ll2.head)
