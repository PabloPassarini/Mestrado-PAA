class SimpleStack:
    def __init__(self):
        self._data = []
        self._ult = -1
    
    def get_stack(self):
        return self._data[:self._ult + 1]
    
    def is_empty(self):
        return self._ult == -1 #Ao iniciar a lista com tamanho -1 significa que iniciamos ela vazia, ou seja, quando o atributo _ult for -1 significa q a lista ta vazia


    def push(self, x):
        self._ult += 1
        self._data = self._data + [x]

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        elemento = self._data[self._ult]
        self._ult -= 1
        return elemento
    
    def top(self):
        if self.is_empty(): raise IndexError("Top from empty stack")
        return self._data[self._ult]





s = SimpleStack()
print(s.is_empty())
s.push(10)
s.push(20)
s.push(30)
print(s.is_empty())
print(s.pop())
print(s.get_stack())
print(s.top())