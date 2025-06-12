class Queue:
    def __init__(self):
        self.data_in = list()
        self.data_out = list()

    def is_empty(self):
        return not self.data_in and not self.data_out

    def enqueue(self, x):
        self.data_in.append(x)

    def dequeue(self):
        if self.is_empty(): return None
        
        if not self.data_out: #len(self.data_out) == 0
            while self.data_in:
                self.data_out.append(self.data_in.pop())
        return self.data_out.pop()
    
    def front(self):
        if self.is_empty(): return None
        if not self.data_out:
            while self.data_in:
                self.data_out.append(self.data_in.pop())
        return self.data_out[-1]

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.front())     # 10
print(q.dequeue())   # 10
print(q.front())     # 20
q.enqueue(30)
print(q.dequeue())   # 20
print(q.dequeue())   # 30
print(q.is_empty())  # True