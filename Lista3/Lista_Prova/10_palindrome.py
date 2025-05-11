class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def is_palindrome(head):
    stack = []
    current = head

    while current:
        stack.append(current.value)
        current = current.next

    current = head
    while current:
        if current.value != stack.pop():
            return False
        current = current.next

    return True

# Criando a lista 1 -> 2 -> 2 -> 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

print(is_palindrome(head))  #True
