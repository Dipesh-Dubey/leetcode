# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        gprev = dummy
        p = None

        for _ in range(left - 1):
            if not gprev.next:
                return dummy.next
            gprev = gprev.next

        kth = gprev
        for _ in range(right - left + 1):
            if not kth.next:
                return dummy.next
            kth = kth.next
        
        gnext = kth.next
        
        c = gprev.next
        p = gnext
        for _ in range(right-left+1):
            n = c.next
            c.next = p
            p = c
            c = n
        
        temp = gprev.next
        gprev.next = kth
        gprev = temp
            
        return dummy.next 
