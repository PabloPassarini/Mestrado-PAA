class MinStack():
    def __init__(self):
        self.data = list()
        self.min_stack = list()

    def get_s(self):
        return self.data

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None

    def push(self, x):
        self.data.append(x)
        if not self.min_stack or x <= self.min_stack[-1]: self.min_stack.append(x)
    
    def pop(self):
        if self.data:
            top = self.data.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.data: #Verifica se n está vazia
            return self.data[-1]
        return None



ms = MinStack()
ms.push(1)
ms.push(-1)
ms.push(2)
print(ms.get_s(), ms.get_min())
ms.pop()
print(ms.get_s(), ms.get_min())