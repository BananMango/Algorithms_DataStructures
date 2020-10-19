class Node:
    def __init__(self, val):
				self.next = None
        self.val = val
				
				
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def get(self, idx):
        if idx > self.size:
            return -1
        curr = self.head
        for i in range(idx - 1):
            curr = curr.next
        return curr.val
    
    def addAtHead(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.size += 1
        else:
            node.next = self.head
            self.head = node
            self.size += 1
        
    def addAtTail(self, val):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        node = Node(val)
        curr.next = node
        self.size += 1
        
    def addAtIndex(self, val, idx):
        if idx > self.size:
            return
        else:
            curr = self.head
            for i in range(idx - 1):
                curr = curr.next
            
            node = Node(val)
            curr_next = curr.next
            curr.next = node
            node.next = curr_next
            self.size += 1
        
    def deleteAtIndex(self, idx):
        if idx > self.size:
            return
        else:
            curr = self.head
            for i in range(idx - 1):
                curr = curr.next
            
            curr_next = curr.next
            curr.next = curr_next.next
            self.size -= 1
