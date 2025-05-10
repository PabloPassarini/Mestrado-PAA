class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.primeiro = -1
        self.ult = -1

    def is_full(self):
        return (self.ult + 1) % self.size == self.primeiro #verifica se o próximo espaço após 'ult' é igual a 'primeiro'
    
    def is_empty(self):
        return self.primeiro == -1
    
    def enqueue(self, x):
        if self.is_full(): return False
        if self.is_empty(): self.primeiro = 0

        self.ult = (self.ult + 1) % self.size
        self.queue[self.ult] = x
        return True
    
    def dequeue(self):
        if self.is_empty(): return False
        if self.primeiro == self.ult:
            self.primeiro = -1
            self.ult = -1
        else:
            self.primeiro = (self.primeiro + 1) % self.size
        return True

    def front_element(self):
        if self.is_empty(): return None
        return self.queue[self.primeiro]

    def rear_element(self):
        if self.is_empty(): return None
        return self.queue[self.ult]
    
cq = CircularQueue(3)
print(cq.enqueue(1))  # True
print(cq.enqueue(2))  # True
print(cq.enqueue(3))  # True
print(cq.enqueue(4))  # False, fila cheia
print(cq.rear_element())  # 3
print(cq.is_full())  # True
print(cq.dequeue())  # True
print(cq.enqueue(4))  # True 
print(cq.front_element())  # 2
print(cq.rear_element())  # 4