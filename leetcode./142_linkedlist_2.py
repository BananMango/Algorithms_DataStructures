 def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None
        
        curr = head
        while curr != slow:
            curr = curr.next
            slow = slow.next
        return curr
