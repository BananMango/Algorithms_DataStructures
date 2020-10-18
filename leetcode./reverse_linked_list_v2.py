class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        prev = None
        curr = head
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
