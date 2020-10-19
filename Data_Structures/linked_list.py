class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self,head=None):
        """
        Initialize your data structure here.
        """
        self.head=head
        self.size = 0

    def get(self, index):
        if index >= self.size:
            return -1
        else:
            curr = self.head
            curr_idx = 0
        while curr_idx in range (0,self.size):
            if curr_idx == index:
                return curr.val
            curr = curr.next
            curr_idx += 1

    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        return 
    
    def addAtTail(self, val):     
        curr = self.head
        if not self.head:
            self.head = Node(val)
            self.size += 1
            return 
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1
        return
    
    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
        elif index > self.size:
            return
        elif index <= self.size:
            prev = self.head
            curr = self.head
            i = 0
            while i in range(0, self.size+1):      
                if i == index:
                    node = Node(val)
                    prev.next = node
                    node.next = curr
                    self.size += 1
                    return
                else:
                    i += 1
                    prev = curr
                    curr = curr.next
            return
        
    def deleteAtIndex(self, index):
        curr_idx = 0
        curr = self.head
        last = self.head
        
        if index >= self.size:
            return             
        if index == 0:
            self.head = curr.next
        while curr_idx in range (0, self.size):         
            if curr_idx == index:
                last.next = curr.next
                self.size -= 1
                return
            curr_idx += 1
            last = curr
            curr = curr.next
        return
