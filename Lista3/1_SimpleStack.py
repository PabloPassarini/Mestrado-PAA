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
        elemento = self.get_top()
        self._data = self._data[:self._ult-1]
        self._ult -= 1
        return elemento
    
    def top(self):
        if self.is_empty(): raise IndexError("Top from empty stack")
        return self._data[self._ult]

    def reverse_string(self):
        reverse_str = SimpleStack()
        for i in range(self._ult , -1, -1):
            reverse_str.push(self._data[i])
        
        return reverse_str.get_stack()

    def is_balanced(self):
        brackets = SimpleStack()
        pares = {')': '(', ']': '[', '}': '{'}
        if self.is_empty(): raise IndexError("Balanced Parentheses from empty stack")
        for i in range(self._ult):
            char = self._data[i]
            if char in '([{':
                brackets.push(char)
            elif char in ')]}':
                if brackets.is_empty():
                    return False
                
                primeiro = brackets.top()
                if pares[char] != primeiro:
                    return False
        
        return True

s = SimpleStack()
print(s.is_empty())
s.push(10)
s.push(20)
s.push(30)
print(s.reverse_string())
print(s.get_stack())
print(s.is_empty())
print(s.pop())

print(s.top())



s2 = SimpleStack()
s2.push('(')
s2.push('[')
s2.push(']')
s2.push(')')
print(s2.is_balanced())  # True

s2 = SimpleStack()
s2.push('(')
s2.push('[')
s2.push(')')
s2.push(']')

print(s2.is_balanced())  # False


s2 = SimpleStack()
s2.push('[')
s2.push('(')
s2.push(']')
s2.push(')')
print(s2.is_balanced())  # False

s2 = SimpleStack()
s2.push('(')
s2.push(')')
print(s2.is_balanced())  # True