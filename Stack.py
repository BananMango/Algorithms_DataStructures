"A stack is a collection of objects that are inserted and removed according to the last-in, first-out (LIFO) principle."

class ArrayStack:
    "Array stack implementation"
    def __init__(self): 
        "creates an empty Stack"
        self._data = []

    def __len__(self):
        "returns lenght of a Stack
        return len(self._data)

    def is_empty(self):
        "checks if stack is empty"
        return len(self._data) == 0

    def push(self, a):
        "adds element to the end "
        self._data.append(a)

    def peek(self):
        "returns element at the end"
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]

    def pop(self):
        "deleted element at the end"
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()

    
