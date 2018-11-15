class LinkedListQueue:

    class _Node:
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception
        res = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return res

    def enqueue(self, item):
        new = self._Node(item, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1

