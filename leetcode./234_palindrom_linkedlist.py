def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        stack = []
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next
        
        if len(stack) == 1:
            return True
        if len(stack) % 2 == 0:
            mid = len(stack) // 2
            return stack[:mid] == stack[mid:][::-1]
        else:
            mid = len(stack) // 2
            return stack[:mid] == stack[mid+1:][::-1]
            


def reverseList(self, curr):
    prev = None
    while(curr):
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev
        
def isPalindrome(self, head: ListNode) -> bool:
    if head is None or head.next is None:
        return True
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    rev = self.reverseList(slow)
    curr = head
    while rev:
        if curr.val != rev.val:
            return False
        curr = curr.next
        rev = rev.next
    return True
