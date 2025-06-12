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
    

st = SimpleStack()
st.push(1)
st.push(2)
st.push(3)
print(st.get_stack())
st.pop()
print(st.get_stack())
print(st.top())
    
