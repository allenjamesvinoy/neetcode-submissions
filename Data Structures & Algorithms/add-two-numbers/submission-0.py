# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1 = 0
        len2 = 0

        curr = l1
        while curr:
            len1+=1
            curr = curr.next
        
        curr = l2
        while curr:
            len2+=1
            curr = curr.next

        if len1 < len2:
            temp = l1
            l1 = l2
            l2 = temp

            temp_len = len1
            len1 = len2
            len2 = temp_len

        carry = 0
        curr_l1 = l1
        curr_l2 = l2
        res = None
        curr_res = None
        for _ in range(0, len1):
            new_val = curr_l1.val + carry
            if curr_l2:
                new_val += curr_l2.val

            carry = new_val // 10
            new_val = new_val % 10
            node = ListNode(new_val)
            if not res:
                res = node
                curr_res = node
            else:
                curr_res.next = node
                curr_res = node

            curr_l2 = curr_l2.next if curr_l2 else None
            curr_l1 = curr_l1.next

        if carry > 0:
            extra_node = ListNode(carry)
            curr_res.next = extra_node

        return res

        
        
        