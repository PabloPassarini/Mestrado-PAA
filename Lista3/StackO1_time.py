class StackMinimum:
    def __init__(self):
        self._data = []
        self._min = []
        self._ultmin = -1
        self._ult = -1

    def is_empty(self):
        return self._ult == -1

    def push(self, x):
        if self._ultmin == -1 or x <= self._min[self._ultmin]:
            self._min += [x]
            self._ultmin += 1

        self._data += [x]
        self._ult += 1

    def get_min(self):
        if self._ultmin == -1:
            raise IndexError("Get_min from empty stack")
        return self._min[self._ultmin]

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        elemento = self.get_top()

        if elemento == self._min[self._ultmin]:
            self._ultmin -= 1
            self._min = self._min[:self._ultmin + 1]

        self._ult -= 1
        self._data = self._data[:self._ult + 1]

        return elemento

    def get_top(self):
        if self.is_empty():
            raise IndexError("Top from empty stack")
        return self._data[self._ult]

    def get_stack(self):
        return self._data[:self._ult + 1]
