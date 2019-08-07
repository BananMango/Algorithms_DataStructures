class ArrayQueue:

    default_size = 10

    def __init__(self):
        self._data = [None]* ArrayQueue.default_size
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Exception
        res = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size += -1
        return res

    def enqueue(self, item):
        if self._size == len(self._data):
            self.resize(2*len(self._data))
        i = (self._front + self._size)%len(self._data)
        self._data[i] = item
        self._size += 1

    def resize(self, c):
        old = self._data
        self._data = [None] * c
        step = self._front
        for i in range(self._size):
            self._data[i] = old[step]
            step = (1 + step) % len(old)
        self._front = 0
