class Solution:
    
    def reverseListRecursively(self, prev, curr):
        head = curr
        if curr.next is not None:
            head = self.reverseListRecursively(curr, curr.next)
        curr.next = prev
        return head
        
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        return self.reverseListRecursively(None, head)
