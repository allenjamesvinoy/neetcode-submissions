# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        if head.next is None or head.next.next is None:
            return False

        slow_ptr = head.next
        fast_ptr = head.next.next

        while slow_ptr != fast_ptr:
            if fast_ptr is None: 
                break

            if slow_ptr == fast_ptr:
                break
            
            fast_ptr = fast_ptr.next.next if fast_ptr.next and fast_ptr.next.next else None
            slow_ptr = slow_ptr.next if slow_ptr.next else None

        if slow_ptr == fast_ptr:
            return True

        return False
