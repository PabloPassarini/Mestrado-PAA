class Heap():
    def __init__(self):
        self.arr = list()

    def insert(self, value):
        self.arr.append(value)
        self.upheap(len(self.arr)-1)
    

    def upheap(self, position):
        if position == 0: return
        else:
            pos_father = (position-1) // 2
            if self.arr[position] < self.arr[pos_father]:
                self.arr[pos_father], self.arr[position] = self.arr[position], self.arr[pos_father]
                self.upheap(pos_father)
    
    def get_heap(self):
        return self.arr
    
    def search_value(self, value):
        return self.arr.index(value)
    
    def remove(self, value):
        pos = self.search_value(value)
        if pos == -1: return

        self.arr[pos], self.arr[-1] = self.arr[-1], self.arr[pos]
        self.arr.pop()
        self.downheap(pos)

    def downheap(self, pos):
        if (len(self.arr ) -1) //2  <= pos: return

        filho_esq = (pos*2) + 1
        filho_dir = (pos*2) + 2

        if self.arr[pos] < self.arr[filho_esq] or self.arr[pos] < self.arr[filho_dir]:

            if self.arr[filho_esq] > self.arr[filho_dir]:
                self.arr[pos], self.arr[filho_esq] = self.arr[filho_esq], self.arr[pos]
                self.downheap(filho_esq)
            else:
                self.arr[pos], self.arr[filho_dir] = self.arr[filho_dir], self.arr[pos]
                self.downheap(filho_dir)

teste = [10, 2, 7, 5, 8, 1, 15]
h = Heap()
for val in teste:
    h.insert(val)
print(h.get_heap())
h.remove(8)    

print(h.get_heap())