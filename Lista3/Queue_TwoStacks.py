class QueueTwoStacks:
    def __init__(self):
        self._stackIn = []
        self._stackOut = []
        self._ultIn = -1
        self._ultOut = -1


    def enqueue(self, x):
        self._ultIn += 1
        self._stackIn += [x]
    
    def _moveIn_to_Out(self):
        if self._ultOut == -1:
            while self._ultIn != -1:
                elemento = self._stackIn[self._ultIn]
                self._stackIn = self._stackIn[:self._ultIn]

                self._ultIn -= 1
                self._ultOut += 1

                self._stackOut += [elemento]
    
    def is_empty(self):
        return self._ultIn == -1 and self._ultOut == -1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        self._moveIn_to_Out()
        elemento = self._stackOut[self._ultOut]
        self._stackOut = self._stackOut[:self._ultOut]
        self._ultOut -= 1
        return elemento
    
    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        self._moveIn_to_Out()
        return self._stackOut[self._ultOut]

    