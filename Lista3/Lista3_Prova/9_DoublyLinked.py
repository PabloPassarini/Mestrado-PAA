class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_tail(self, value):
        new_node = DoublyNode(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_by_value(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True  # Valor encontrado e removido
            current = current.next
        return False  # Valor não encontrado

    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")


# Instanciando a lista duplamente ligada
dll = DoublyLinkedList()

# Inserções
dll.insert_at_head(3)
dll.insert_at_head(2)
dll.insert_at_head(1)
print("Após insert_at_head 3, 2, 1:")
dll.display_forward()    # Esperado: 1 <-> 2 <-> 3 <-> None
dll.display_backward()   # Esperado: 3 <-> 2 <-> 1 <-> None

dll.insert_at_tail(4)
dll.insert_at_tail(5)
print("\nApós insert_at_tail 4, 5:")
dll.display_forward()    # Esperado: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> None
dll.display_backward()   # Esperado: 5 <-> 4 <-> 3 <-> 2 <-> 1 <-> None

# Deleção
dll.delete_by_value(3)
print("\nApós delete_by_value(3):")
dll.display_forward()    # Esperado: 1 <-> 2 <-> 4 <-> 5 <-> None
dll.display_backward()   # Esperado: 5 <-> 4 <-> 2 <-> 1 <-> None

dll.delete_by_value(1)
print("\nApós delete_by_value(1) (remover head):")
dll.display_forward()    # Esperado: 2 <-> 4 <-> 5 <-> None

dll.delete_by_value(5)
print("\nApós delete_by_value(5) (remover tail):")
dll.display_forward()    # Esperado: 2 <-> 4 <-> None
dll.display_backward()   # Esperado: 4 <-> 2 <-> None

# Testar remoção de valor inexistente
result = dll.delete_by_value(42)
print(f"\nTentando remover valor inexistente (42): {result}")  # Esperado: False
