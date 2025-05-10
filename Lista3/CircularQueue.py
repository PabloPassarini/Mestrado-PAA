class CircularQueue:
    def __init__(self, n):
        self._lenght = n
        self._data = [None] * self._lenght #Iniciando uma lista com o tamanho informado inicialmento, com os valores dessa lista como None
        self._front = 0 #Indice do elemento da frente
        self._rear = 0  # Indice do último elemento
        self._size = 0  #Quantidade de elementos na fila

    def is_full(self):
        return self._size == self._lenght
    
    def is_empty(self):
        return self._size == 0
    
    def get_queue(self):
        return self._data
    
    def enqueue(self, x):
        if self.is_full(): raise OverflowError('Queue is full')
        
        self._data[self._rear] = x
        self._rear = (self._rear + 1) % self._lenght
        self._size += 1

    def dequeue(self):
        if self.is_empty(): raise IndexError("Dequeue from empty queue")
        val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._lenght
        self._size -= 1
        return val

    def front(self):
        if self.is_empty(): raise IndexError("Front from empty queue")
        return self._data[self._front]

    def rear(self):
        if self.is_empty(): raise IndexError("Rear from empty queue")
        return self._data[(self._rear - 1 + self._lenght) % self._lenght]
    
