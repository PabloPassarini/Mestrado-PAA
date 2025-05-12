class SimpleStack:
    def __init__(self):
        self.data = list()

    def get_stack(self):
        return self.data

    def push(self, x):
        self.data.append(x)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def top(self):
        return self.data[len(self.data) - 1]
    
    def pop(self):
        if self.is_empty(): raise IndexError("Pop from empty stack")
        value = self.top()
        self.data.pop()
        return value
    
    def is_balanced(self):
        brackets = SimpleStack()
        pares = {')': '(', ']': '[', '}': '{'}
        for char in self.data:
            if char in '([{':
                brackets.push(char)
            elif char in ')]}':
                if brackets.is_empty(): return False

                primeiro = brackets.pop()
                if pares[char] != primeiro:
                    return False
        return True
    
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